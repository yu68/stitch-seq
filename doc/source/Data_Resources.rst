.. _Resource:

==========================================================
Resources of strong interactions from two mouse cell types
==========================================================

Description of different samples
================================

E14-1
--------

:Cell line: ESC E14
:Barcode: ACCT
:Experimental Details: Actively growing E14 cells were UV irradiated (254 nm) at 200mJ/cm 
  to crosslink proteins to interacting RNAs. After cell lysis, we trim down RNAs into 
  1000-2000 nt using RNase I and remove DNA by TURBO DNase. To recover RNAs bound to 
  RNA-binding proteins, we biotin-labeled them with EZ-Link Iodoacetyl-PEG2-Biotin from 
  Pierce. RNA-protein complexes were next immobilized on Streptavidin-coated beads. The 
  beads are then saturated with free biotin, preventing it from interfering with following 
  ligation with biotin-tagged linker. A biotin-tagged RNA linker was ligated to the 5’-end 
  of immobilized RNAs. Proximity ligation was then carried out under diluted conditions 
  while the RNA-protein complexes are still bound on bead. After RNA purification by 
  Proteinase K and phenol-chloroform extraction, we specifically removed the unligated 
  biotin by first anneal a complementary DNA oligo to the biotin-tagged linker by using 
  the annealing protocol: 70oC for 5 min, 25oC for 20 min, T7 Exo for 30 min. Exonuclease 
  T7 was added to remove terminal unligated biotin at the double-stranded RNAlinker-DNAoligo 
  hybrid. T7 Exonuclease acts in the 5' to 3' direction, catalyzing the removal of 5' 
  mononucleotides from duplex DNA and RNA/DNA hybrids in the 5’ to 3’ direction. The resulted 
  RNAs were fragmented again into ~200 nt using RNase III RNA Fragmentation Module from NEB 
  (1ul of RNase III in 6 min at 37C). The RNAs were purified by column and ligated with 
  sequencing adapter, then reverse-transcribed and PCR for library construction. We applied 
  an rRNA removal step after constructing cDNA by using an rRNA removal protocol based on 
  the Duplex-Specific thermostable nuclease (DSN) enzyme using the protocol recommended by 
  `Illumina <http://supportres.illumina.com/documents/myillumina/7836bd3e-3358-4834-b2f7-80f80acb4e3f/dsn_normalization_sampleprep_application_note_15014673_c.pdf>`_. 
  The constructed cDNAs were quality-checked by Bioanalyzer. The cDNAs were next 
  subjected paired-end sequencing on HiSeq-2500 platform.
:Linker: 
  *mL5*: 5' - rCrUrA rG/iBiodT/rA rGrCrC rCrArU rGrCrA rArUrG rCrGrA rGrGrA - 3'

E14-2
--------

:Cell line: ESC E14
:Barcode: GGCG
:Experimental Details: Same as E14_WP_1 but this time rRNA removal was performed right after 
  Proteinase K and phenol-chloroform treatment using the GeneRead rRNA Depletion Kit by 
  Qiagen. Furthermore, the annealing of RNA linker and complementary DNA oligo was changed 
  into: denature for 90 s at 90°C, and then anneal at -0.1°C/s to 25 °C and then incubate 
  for 25 min at 25 °C. Since after rRNA depletion the amount of RNA remained was less than 
  that obtained from E14 #1, we reduced the duration of RNA fragmentation by RNase III from 
  6 min to 3 min. However, this reduction in RNase III treatment led to large fragments than 
  desirable. 
:Linker:
  *mL5*: 5' - rCrUrA rG/iBiodT/rA rGrCrC rCrArU rGrCrA rArUrG rCrGrA rGrGrA - 3'

E14-indirect
------------

:Cell line: ESC E14
:Barcode: AATG
:Experimental Details: To detect interactions between RNAs that are not bound to the same protein 
  but to interacting proteins, we used formaldehyde in conjunction with a second crosslinker, EGS. 
  The combination of formaldehyde and EGS crosslinks both RNA-protein and protein-protein 
  interactions thereby maximize the detection of RNA-RNA interactions that are facilitated by 
  interacting proteins. Actively grown E14 cells was crosslinked with 1.5 mM of freshly prepared 
  EthylGlycol bis(SuccinimidylSuccinate) (EGS)) for 45 minutes at room temperature and then 1% of 
  formaldehyde for 10 minutes also at room temperature. Since crosslinking by formaldehyde makes 
  the cells very rigid and less amenable to be broken down lysis buffer. Therefore, we utilized 
  sonication to fragment the protein-bound RNA into ~1000 nt size range. The remaining steps were 
  performed similarly to E14_WP_2. 
  
  Another main difference between this sample and other samples is that we didn't remove the nuclei, 
  thus effectively including RNA-RNA interactions inside the nucleus into the sample. In other 
  samples, only the cytoplasm was enriched.
:Linker:
  *mL5*: 5' - rCrUrA rG/iBiodT/rA rGrCrC rCrArU rGrCrA rArUrG rCrGrA rGrGrA - 3'

MEF
---

:Cell line: MEF
:Barcode: GGCG
:Experimental Details: We irradiated actively grown 1E8 MEF cells (254 nm). This time, the RNAs 
  were fragmented into 300nt size range. RNase III fragmentation was also modified accordingly 
  to adjust for smaller amount of RNAs: instead of adding 1ul of RNase III, we added only 0.5uL 
  of RNase III and then incubated at 37C for 5 min. The subsequent steps were performed using 
  the same procedure as E14_WP_2.
:Linker:
  *mL5*: 5' - rCrUrA rG/iBiodT/rA rGrCrC rCrArU rGrCrA rArUrG rCrGrA rGrGrA - 3'


Resources of Strong Interactions
================================

From merged data of E14-1 and E14-2:
------------------------------------------

Strong interactions based on clustering of genomic locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
 * First seven column is for information of cluster in Part1 of interaction (5'side of linker); second seven column is for information of cluster in Part2 of interaction (3'side of linker)
 *  **Type**: RNA types or repeat types; **Name**: RNA or repeat names; **Subtype**: intron/utr3/utr5/exon for mRNA, intron/utr for lincRNA or repeat family; **Count**: number of supported reads in that cluster
 * Second last column is the number of mapped pairs that support this interaction.
 * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_clusters.xlsx>`_ (Include two sheets, one for all interactions, and another one for the interactions that are not involving rRNA)

`List of clusters (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_cluster_total_sort.xlsx>`_ (Removing rRNA/rRNA_repeats)

`Strong interactions noLeftRight (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_clusters_noLeftRight.xlsx>`_ (Clusters are generated by merging RNA1 and RNA2, The directions of RNA1 and RNA2 are ignored)

Strong interactions based on annotation of RNAs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
  * First six column is for information of RNA in Part1 of interaction (5'side of linker); second six column is for information of RNA in Part2 of interaction (3'side of linker)
  * **Type**: RNA or repeat types; **Name**: RNA or repeat names; **Count**: number of supported reads in that RNA
  * Second last column is the number of mapped pairs that support this interaction.
  * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions RNA (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_clusters_RNA.xlsx>`_

`Strong interactions RNA noLeftRight (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_clusters_RNA_noLeftRight.xlsx>`_ (The directions of RNA1 and RNA2 are ignored, and interactions involving introns are deleted)

.. _SIFDR:

Strong interactions based on annotation of RNAs (FDR and using ES-indirect as control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:Genome: mm9
:Explanation:
  * First six column is for information of RNA in Part1 of interaction (5'side of linker); second six column is for information of RNA in Part2 of interaction (3'side of linker)
  * **Type**: RNA or repeat types; **Name**: RNA or repeat names; **Count**: number of supported reads in that RNA
  * Column 15 is the number of mapped pairs that support this interaction.
  * Column 16 is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test, column 17 is p-value
  * Column 18 is the FDR. FDR is calculated using the Benjamini–Hochberg procedure
  * Column 19 is the fold change between merged data of ES14-1 and ES14-2 and dual crosslink data. The fold change is the ratio (# of interaction in merged data + 0.5)/(# of interaction in dual crosslink data + 0.5)

`Strong interactions RNA noLeftRight FDR and using ES-indirect as control (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_cluster_noLeftRight_RNA_DualCrosslinkControl_significant.xlsx>`_ (The directions of RNA1 and RNA2 are ignored, and interactions involving introns are deleted, using FDR cutoff and using ES-indirect as control)


From E14-indirect dual crosslinking:
------------------------------------

Strong interactions based on clustering of genomic locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
 * First seven column is for information of cluster in Part1 of interaction (5'side of linker); second seven column is for information of cluster in Part2 of interaction (3'side of linker)
 *  **Type**: RNA types or repeat types; **Name**: RNA or repeat names; **Subtype**: intron/utr3/utr5/exon for mRNA, intron/utr for lincRNA or repeat family; **Count**: number of supported reads in that cluster
 * Second last column is the number of mapped pairs that support this interaction.
 * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions (ES_indirect) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_interaction_clusters.xlsx>`_ (Include two sheets, one for all interactions, and another one for the interactions that are not involving rRNA)

`List of clusters (ES_indirect) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_cluster_total_sort.xlsx>`_ (Removing rRNA/rRNA_repeats)

`Strong interactions noLeftRight (ES_indirect) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_interaction_clusters_noLeftRight.xlsx>`_ (Clusters are generated by merging RNA1 and RNA2, The directions of RNA1 and RNA2 are ignored)


Strong interactions based on annotation of RNAs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
  * First six column is for information of RNA in Part1 of interaction (5'side of linker); second six column is for information of RNA in Part2 of interaction (3'side of linker)
  * **Type**: RNA or repeat types; **Name**: RNA or repeat names; **Count**: number of supported reads in that RNA
  * Second last column is the number of mapped pairs that support this interaction.
  * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions RNA (ES_indirect) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_interaction_clusters_RNA.xlsx>`_

`Strong interactions RNA noLeftRight (ES_indirect) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_interaction_clusters_RNA_noLeftRight.xlsx>`_ (The directions of RNA1 and RNA2 are ignored, and interactions involving introns are deleted)

From MEF sample:
----------------

Strong interactions based on clustering of genomic locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
 * First seven column is for information of cluster in Part1 of interaction (5'side of linker); second seven column is for information of cluster in Part2 of interaction (3'side of linker)
 *  **Type**: RNA types or repeat types; **Name**: RNA or repeat names; **Subtype**: intron/utr3/utr5/exon for mRNA, intron/utr for lincRNA or repeat family; **Count**: number of supported reads in that cluster
 * Second last column is the number of mapped pairs that support this interaction.
 * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions (MEF) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/GGCG_MEF_interaction_clusters.xlsx>`_ (Include two sheets, one for all interactions, and another one for the interactions that are not involving rRNA)

`List of clusters (MEF) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/GGCG_MEF_cluster_total_sort.xlsx>`_ (Removing rRNA/rRNA_repeats)

`Strong interactions noLeftRight (MEF) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/GGCG_MEF_interaction_clusters_noLeftRight.xlsx>`_ (Clusters are generated by merging RNA1 and RNA2, The directions of RNA1 and RNA2 are ignored)


Strong interactions based on annotation of RNAs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Genome: mm9
:Explanation:
  * First six column is for information of RNA in Part1 of interaction (5'side of linker); second six column is for information of RNA in Part2 of interaction (3'side of linker)
  * **Type**: RNA or repeat types; **Name**: RNA or repeat names; **Count**: number of supported reads in that RNA
  * Second last column is the number of mapped pairs that support this interaction.
  * Last column is the "ln(p_value)" for the significance of interaction. P_value is based on a hypergeometric test

`Strong interactions RNA (MEF) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/GGCG_MEF_interaction_clusters_RNA.xlsx>`_

`Strong interactions RNA noLeftRight (MEF) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/GGCG_MEF_interaction_clusters_RNA_noLeftRight.xlsx>`_ (The directions of RNA1 and RNA2 are ignored, and interactions involving introns are deleted)


Number of different types of interactions:
------------------------------------------

`Strong interactions based on clusters of genomic locations <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/Count_types_interaction_fragment.htm>`_ (There are three sheets, "All_interactions", "Inter-RNA_interactions", "Intra-RNA interactions") 

`Strong interactions based on annotations of RNAs <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/Count_types_interaction_fragment_wholeRNA.htm>`_

`Strong interactions based on annotations of RNAs noLeftRight no Intron <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/Count_types_interaction_fragment_wholeRNA_noLeftRight.htm>`_

 * For each cell type, there are two columns,
 * The first column gives the number of strong interactions with this interaction type,
 * the second column gives the number of mapped pairs that support this interaction type.


Target of miRNA in mir-290-295 clusters and mmu-mir-703
=======================================================

* The information of miRNAs are in columns 1-5;
* The information of target locations are in columns 6-11; 
* The the last column gives the count of supported mapped pairs.

From merged data of E14-1 and E14-2:
------------------------------------------

`Target of miRNA in mir-290-295 clusters and mmu-mir-703 (ES_UV) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/ACCT_GGCG_interaction_clusters_miRNA.xlsx>`_

From E14-indirect dual crosslinking:
------------------------------------

`Target of miRNA in mir-290-295 clusters and mmu-mir-703 (ES_dual) <http://systemsbio.ucsd.edu/RNA-Hi-C/Data/AATG_interaction_clusters_miRNA.xlsx>`_


