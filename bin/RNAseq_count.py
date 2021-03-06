#!/usr/bin/env python
# Pengfei Yu yupf05@gmail.com

import sys,argparse,os
from xplib import TableIO
from xplib import DBI
from xplib.Annotation import Bed
from Annotation import *
import pysam

def ParseArg():
    p=argparse.ArgumentParser(description = "Count RPKM value of RNAseq/CLIPseq for clusters (genomic regions) in strong interaction",epilog="Library dependency: bam2x")
    p.add_argument("-i","--input",type=str,required=True,help="input strong interaction file")
    p.add_argument("-d","--data",type=str,nargs='+',required=True,help="RNA-seq/CLIP-seq data (bam/bed files)")
    p.add_argument("-n","--name",type=str,nargs='+',required=True,help="name for the RNA-seq/CLIP-seq data, to be specified in output txt file")
    p.add_argument("-f","--format",type=str,nargs='+',required=True,help="format for the RNA-seq/CLIP-seq data, can be bam or bed")
    p.add_argument("-o","--output",type=str,default="stdout",help="output txt file")
    if len(sys.argv)==1:
        print >>sys.stderr,p.print_help()
        exit(0)
    return p.parse_args()


def RPKM(bed,dbi,total_num,name):
    ''' bed: Bed object from xplib.Annotation (for genomic region)
        dbi: DBI object from xplib (for RNA-seq/CLIP-seq data) '''
    n=0
    start=bed.stop
    end=bed.start
    if name!="smRNA": 
        query_regions=dbi.query(bed,method='fetch')
    else:
        query_regions=dbi.query(bed)
    for i in query_regions:
        if not overlap(i,bed): continue
        n=n+1
        start=min(start,i.start)
        end=max(end,i.stop)
    length=min(end-end,bed.stop-bed.start)+1
    return (n*1000.0*1E6/(length*total_num))

def Main():
    args=ParseArg()
    
    if len(args.data)!=len(args.name):
        print >> sys.stderr, "ERROR: Number of data is not the same as number of names!"
        sys.exit(0)

    # store data information
    data={}
    total_reads={}
    for i in range(len(args.data)):
        temp_name=args.name[i]
        print >> sys.stderr, "\n Reading data file:"+temp_name+"..."
        total_reads[temp_name]=0
        if args.format[i]=="bam":
            total_reads[temp_name] = reduce(lambda x, y: x + y, [ int(l.rstrip('\n').split('\t')[2]) for l in pysam.idxstats(args.data[i])])
        else:
            Format="bed"
            for b in TableIO.parse(args.data[i],Format):
                total_reads[temp_name]+=1
                if total_reads[temp_name]%50000==0:
                    print >> sys.stderr, "  reading %d reads..\r"%(total_reads[temp_name]),
        data[temp_name]=DBI.init(args.data[i],args.format[i])
        
    
    output=open(args.output,'w')

    Input=open(args.input,'r')
    lines=Input.read().split("\n")

    # header
    header=["chr","start","end","type","name","subtype","count"]+data.keys()
    print >> output, "\t".join(g+"_%d"%(f) for f in [1,2] for g in header)+"\tinteraction\tp-value"

    num=0    
    print >> sys.stderr, "Start process interactions:"
    for l in lines:
        if l.strip()=='': continue
        l=l.strip().split('\t')
        num=num+1
        if l[0]=="chrM" or l[7]=="chrM": continue
        C1=Bed([l[0],int(l[1]),int(l[2])])
        C2=Bed([l[7],int(l[8]),int(l[9])])
        rpkm1="\t".join (str(f) for f in [RPKM(C1,data[n],total_reads[n],n) for n in data.keys()])
        rpkm2="\t".join (str(f) for f in [RPKM(C2,data[n],total_reads[n],n) for n in data.keys()])
        print >> output, "\t".join(str(f) for f in l[:7]+[rpkm1]+l[7:14]+[rpkm2,l[14],l[15]])
	if num%1000==0:
            print >> sys.stderr, "  Output interaction: %d\r"%(num),

if __name__ == '__main__':
    Main()
