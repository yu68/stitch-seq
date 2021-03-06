#!/usr/bin/env python
import sys, argparse
from time import time
from operator import attrgetter
from scipy.stats import hypergeom
from random import shuffle

from UnionFind import *
# include functions UF, find, merge, connected, count

class annotated_bed():
    def __init__(self,x=None,**kwargs):
        if type(x)==type("str"):
            x=x.split("\t")
        self.chr=str(x[0]).strip()
        self.start=int(x[1])
        self.end=int(x[2])
        try:
            self.seq=str(x[3]).strip()
            self.type=str(x[4]).strip()
            self.name=str(x[5]).strip()
            self.subtype=str(x[6]).strip()
        except:
            pass
        for key in kwargs.keys():
            setattr(self,key,kwargs[key])
    def __lt__(self, other): # for the purpose of ordering clusters
        if self.chr==other.chr:
            return ((self.start<other.start)&(self.end<other.end))
        else:
            return (self.chr<other.chr)
    def overlap(self,other): # for the purpose of finding overlap between regions
        return ((self.chr==other.chr)&(self.end>other.start)&(self.start<other.end))
    def Cluster(self,c):
        self.cluster=c
        #self.c_info=c_info
    def Update(self,S,E): # used for update or expand cluster locations
        self.start=min(self.start,S)
        self.end=max(self.end,E)
    def __str__(self):
        return "\t".join(str(f) for f in [self.chr,self.start,self.end,self.type,self.name,self.subtype,self.cluster])
    # self.cluster become number of regions within cluster for cluster_pool object



##########################################################
#cluster the regions together if they are connected (overlapped) using Union-find approach
def cluster_regions(part,min_clusterS):
    N=len(part)
    cluster_loc=part
    uf_object=UF(N) # union find object
    for i in range(N):
        for j in range(i+1,N):
            if part[i].overlap(part[j]):
                uf_object.merge(i,j)
                #update cluster location (expand)
                cluster_loc[uf_object.find(j)].Update(min(part[i].start,part[j].start),max(part[i].end,part[j].end))
            if part[i]<part[j]:
                break
        if i%10000==0: print >> sys.stderr, "  Merging segment for clusters (%d/%d)\r"%(i,N),
    
    c_pool=[] # cluster pool
    for i in range(N):
        c=uf_object.find(i)
        #c_info="%d:%d"%(cluster_loc[c].start,cluster_loc[c].end)
        part[i].Cluster(uf_object.find(i))
        c_pool.append(c)

    cluster_pool={}
    for c in set(c_pool):
        count=c_pool.count(c)
        if count>=min_clusterS:
            cluster_pool[c]=cluster_loc[c]
            cluster_pool[c].cluster=count
    return (cluster_pool)


def Random_strongInteraction(part1,part2,cluster_pool1,cluster_pool2):
    global min_interaction, p_value
    ''' This is for counputing FDR using random permutation '''
    c_interaction={}
    for i in range(len(part1)):
        region1=str(part1[i])
        region2=str(part2[i])
        inter="%d--%d"%(part1[i].cluster,part2[i].cluster)
        if c_interaction.has_key(inter):
            c_interaction[inter]+=1
        else:
            c_interaction[inter]=0

    k=0 # record for strong interactions
    n=0
    for interaction in c_interaction:
        n=n+1
        count=c_interaction[interaction]
        if count<min_interaction: continue
        i=int(interaction.split("--")[0])
        j=int(interaction.split("--")[1])
        try:  # we select clusters with size no less than 5, so some interactions cannot be found in clusters
            count1=cluster_pool1[i].cluster
            count2=cluster_pool2[j].cluster
        except:
            continue
        real_p=1-hypergeom.cdf(count,len(part1),count1,count2)
        if real_p<=p_value:
            k=k+1
    return [n,k]

#parameters

def ParseArg():
    p=argparse.ArgumentParser(description="find strong interactions from paired genomic location data",epilog="need Scipy for hypergeometric distribution")
    p.add_argument("-i","--input",type=str,required=True,help="input file which is the output file of Stitch-seq-Aligner.py")
    p.add_argument("-M","--min_clusterS",type=int,default=5,help="minimum number of segments allowed in each cluster, default:5")
    p.add_argument("-m","--min_interaction",type=int,default=3,help="minimum number of interactions to support a strong interaction, default:3")
    p.add_argument('-p',"--p_value",type=float,default=0.05,help="the p-value based on hypergeometric distribution to call strong interactions, default: 0.05")
    p.add_argument('-o','--output',type=str,help="specify output file")
    p.add_argument("-F","--FDR",action='store_true', help="Compute FDR if specified")
    if len(sys.argv)==1:
        print >>sys.stderr,p.print_help()
        sys.exit(0)
    return p.parse_args()


def Main():
    t1=time()
    
    global min_interaction, p_value
    args=ParseArg()
    inp = open(args.input, 'r')
    min_clusterS=args.min_clusterS
    min_interaction=args.min_interaction
    p_value=args.p_value
    output=open(args.output,'w')


    #store genomic location of part1 and part2
    part1=[]
    part2=[]


    k=0
    
    print >> sys.stderr,"# Inputing data..."
    for line in inp.read().split('\n'):
        if line=='': continue
        line=line.strip().split('\t')
        k=k+1
        part1.append(annotated_bed(line[0:7],id=k))
        part2.append(annotated_bed(line[8:],id=k))
        if k%20000==0: 
            print >> sys.stderr,"  Reading %d pairs of segments\r"%(k),
    print >> sys.stderr,"Get total %d pairs."%(k)
    
    if len(part1)!=len(part2):
        print >> sys.stderr, "## ERROR: number of regions in two part not match!!"
        sys.exit(0)

    # sort in genomic order, easy for clustering
    part1=sorted(part1, key=attrgetter('start'))
    part1=sorted(part1, key=attrgetter('chr'))
    part2=sorted(part2, key=attrgetter('start'))
    part2=sorted(part2, key=attrgetter('chr'))


    print >>sys.stderr,"# Generating clusters for two parts..."
    print >>sys.stderr,"  Part1:"
    cluster_pool1=cluster_regions(part1,min_clusterS)
    print >>sys.stderr,"   cluster number for part1 is %d          "%(len(cluster_pool1))
    print >>sys.stderr,"  Part2:"
    cluster_pool2=cluster_regions(part2,min_clusterS)
    print >>sys.stderr,"   cluster number for part2 is %d          "%(len(cluster_pool2))

    # sort back to pair two parts
    part1=sorted(part1, key=attrgetter('id'))
    part2=sorted(part2, key=attrgetter('id'))

    c_interaction={}
    for i in range(len(part1)):
        region1=str(part1[i])
        region2=str(part2[i])
        inter="%d--%d"%(part1[i].cluster,part2[i].cluster)
        if c_interaction.has_key(inter):
            c_interaction[inter]+=1
        else:
            c_interaction[inter]=0

    print >> sys.stderr,"# finding strong interactions from clusters..."
    k=0 # record for strong interactions
    n=0
    for interaction in c_interaction:
        n=n+1
        count=c_interaction[interaction]
        if count<min_interaction: continue
        i=int(interaction.split("--")[0])
        j=int(interaction.split("--")[1])
        try:  # we select clusters with size no less than 5, so some interactions cannot be found in clusters
            count1=cluster_pool1[i].cluster
            count2=cluster_pool2[j].cluster
        except:
            continue
        real_p=1-hypergeom.cdf(count,len(part1),count1,count2)
        if real_p<=p_value:
            k=k+1
            print >> output,str(cluster_pool1[i])+'\t'+str(cluster_pool2[j])+'\t%d\t%.5f'%(count,real_p)
        if n%1000==0: print >> sys.stderr, "  Progress ( %d / %d )\r"%(n,len(c_interaction)),

    print >> sys.stderr,"# Find %d strong interactions. Cost time: %.2f s"%(k,time()-t1)

    if args.FDR:
        print >> sys.stderr, "# Permutated results:"
        for i in range(10):
            shuffle(part2)
            [n_r_I,n_r_SI]=Random_strongInteraction(part1,part2,cluster_pool1,cluster_pool2)
            print >> sys.stderr, "  ",i, n_r_I, n_r_SI, n_r_SI*1.0/n_r_I
            

if __name__=="__main__":
    Main()
