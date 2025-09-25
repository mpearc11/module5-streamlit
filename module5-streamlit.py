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

st.title('EvoScore Calculation')

st.header('Submit Sequences for PSA')

#can insert code here later that will allow file upload & do the alignment internally

#below is code to upload clustal psa (and hopefully the following steps)

psa_file = st.file_uploader("",type='aln')

if psa_file is not None:
    st.success("PSA file uploaded")
else:
    st.info("please upload your PSA file")

temp = psa_file.read()
temp2 = psa_file.getvalue().decode("utf-8")
st.write(temp)
st.write(temp2)

if st.button('read in PSA alignment'):
    alignment = AlignIO.read(psa_file, 'clustal')


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
