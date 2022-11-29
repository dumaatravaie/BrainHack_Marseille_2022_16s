#!/usr/bin/python
"""
This script enables us to downloads data from NCBI .

Example:

        $ python Download_From_NCBI.py


Attributes:
    cmmd (str): command to lauch the fastq_dump script

    output_dir(str) = path to the ouput directory 

    SraAccList.txt =  file created via the NCBI website tool, on the project page go to "Send to" top right corner, then
    "file" choose "accession list" click ok .

    Exemple of SraAccList.txt format :

    SRR14318724
    SRR14318725
    SRR14318726
    SRR14318727
    SRR14318728


Todo:
    * CMD line version
    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


import sys
import os.path
import os


cmmd="/sratoolkit.3.0.1-ubuntu64/bin/fastq-dump" # command to launch fastq_dump bin 
output_dir="/BrainHack_2022_project/Data"

input_file="SraAccList.txt" 
read_File=open(input_file,'r')

for line in read_File:
    SRA_Number=line.strip()
    if SRA_Number !="":
        os.sys(cmmd+" "+SRA_Number+" "+output_dir)
        print(cmmd+" "+SRA_Number+" "+output_dir)
read_File.close()
