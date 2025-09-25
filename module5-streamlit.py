import streamlit as st
from Bio import Blast
from Bio import Align
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from io import StringIO
from Bio import AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
import pandas as pd
import tempfile
import os

st.title('EvoScore Calculation')

st.header('Submit Sequences for PSA')

#can insert code here later that will allow file upload & do the alignment internally

#below is code to upload clustal psa (and hopefully the following steps)

psa_file = st.file_uploader("",type='aln')

if psa_file is not None:
    st.success("PSA file uploaded")
else:
    st.info("please upload your PSA file")

#temp = psa_file.read() ##adds 'b in front of file & other character issues (adds /n etc)
temp = psa_file.getvalue().decode("utf-8") ##decodes characters correctly but still has too long file name issue
#temp = psa_file.getvalue() ##adds 'b in front of file & other character issues (adds /n etc)
st.write(temp)

if st.button('read in PSA alignment'):
    #alignment = AlignIO.read(temp, 'clustal')
    alignment = AlignIO.read(StringIO(temp), "clustal")
    #alignment = AlignIO.read('ctei_clustal.aln', 'clustal')
    st.write(alignment)

#convert clustal alignment to pandas dataframe

#seq1 = alignment[0]
#seq2 = alignment[1]

seqs = alignment.sequences
st.write(seqs)

seq1 = seqs[0]
st.write(seq1)


#if st.button('create PSA alignment object'):
    #st.write(psa_file)
    #psa = psa_file.read()
    #st.write(psa)
    
    #alignment = Align.read(open(psa_file), "fasta")
    #st.write(alignment)
    #st.write(type(alignment.sequences))

consurf_file = st.file_uploader('',type='csv')

if consurf_file is not None:
    st.success('consurf file uploaded')
else:
    st.info('please upload the consurf file')

if st.button('create consurf dataframe'):
    df = pd.read_csv(consurf_file)

#code to convert alignment into pandas dataframe




#@st.fragment()
#def PSA_download():
 #   with open('clustalPSA.aln') as f:
  #      st.download_button('download PSA', f)
#PSA_download()
