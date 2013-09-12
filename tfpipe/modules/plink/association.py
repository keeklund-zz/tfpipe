""" """
from tfpipe.base import Job

class Plink(Job):
    """PLINK

    PLINK is a free, open-source whole genome association analysis toolset, 
    designed to perform a range of basic, large-scale analyses in a 
    computationally efficient manner.

    The focus of PLINK is purely on analysis of genotype/phenotype data, so 
    there is no support for steps prior to this (e.g. study design and planning, 
    generating genotype or CNV calls from raw data). Through integration with 
    gPLINK and Haploview, there is some support for the subsequent 
    visualization, annotation and storage of results.

    PLINK (one syllable) is being developed by Shaun Purcell at the Center for 
    Human Genetic Research (CHGR), Massachusetts General Hospital (MGH), and the 
    Broad Institute of Harvard & MIT, with the support of others.   

    http://pngu.mgh.harvard.edu/~purcell/plink/index.shtml

    """
    _module = 'plink/1.07'
    _cmd = 'plink'
