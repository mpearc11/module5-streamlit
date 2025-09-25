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
import numpy as np

st.title('EvoScore Calculation')

st.header('Submit Sequences for PSA')

#can insert code here later that will allow file upload & do the alignment internally

#below is code to upload clustal psa (and hopefully the following steps)

psa_file = st.file_uploader("",type='aln')
if psa_file is not None:
    st.success("PSA file uploaded")
else:
    st.info("please upload your PSA file")


consurf_file = st.file_uploader('',type='csv')
if consurf_file is not None:
    st.success('consurf file uploaded')
else:
    st.info('please upload the consurf file')


#temp = psa_file.read() ##adds 'b in front of file & other character issues (adds /n etc)
temp = psa_file.getvalue().decode("utf-8") ##decodes characters correctly but still has too long file name issue
#temp = psa_file.getvalue() ##adds 'b in front of file & other character issues (adds /n etc)
st.write(temp)

#declaring variables outside of button if statement so i can access them after the button step
df = ''
df1 = ''
df2 = ''
df_exploded = ''

if st.button('read in PSA alignment'):
    #alignment = AlignIO.read(temp, 'clustal')
    alignment = AlignIO.read(StringIO(temp), "clustal")
    #alignment = AlignIO.read('ctei_clustal.aln', 'clustal')
    st.write(alignment)
    
    #convert clustal alignment to individual sequence strings
    
    seq1 = str(alignment[0].seq)
    seq2 = str(alignment[1].seq)
    
    st.write(seq1)
    st.write(seq2)
    
    #convert strings to pandas dataframe
    
    data = {'target seq': [seq1],
                'ps seq': [seq2]}
    df = pd.DataFrame(data)
    st.write(df)
    df1 = df['target seq'].str.split('').explode().reset_index(drop=True)
    st.write(df1)
    df2 = df['ps seq'].str.split('').explode().reset_index(drop=True)
    st.write(df2)
    df_exploded = pd.concat([df1, df2], axis=1)
    st.write(df_exploded)
    df_exploded['color'] = 0
    df_exploded = df_exploded.iloc[1:]
    st.write(df_exploded)
       
    #declaring more variables outside button if statement
    consurf_df = ''
    #df_combined = ''

    @st.fragment()
    def frag():
        if st.button('create consurf dataframe'):
            consurf_df = pd.read_csv(consurf_file)
            st.write(consurf_df)
            consurf_df = consurf_df[['SEQ','COLOR']]
            consurf_df = consurf_df.iloc[1:]
            st.write(consurf_df)
            
            #combine dataframes; can concat OR just create the new COLOR one based on presence/absence of letter in each row
            
            #df_combined = pd.concat([df_exploded, consurf_df], axis=1)
            #st.write(df_combined)

            for i in consurf_df['COLOR']:
                st.write(i)
                for aa in df_exploded['ps seq']:
                    st.write(aa)
                    #df_exploded['color'] = np.where(df_exploded.loc[aa,'ps seq'] != '-', i, 'no match')
                    #df_exploded['color'] = np.where(aa != '-', i, 'no match')
                    df_exploded['color'] = np.where(df_exploded['ps seq'] != '-', i, 'no match')
                    if aa != '-':
                        break
                st.write('out of loop')
                #aa = aa + 1
                #i = i + 1
            #for i in consurf_df['COLOR']:
                #st.write(i)
                #if row in df_exploded['ps seq'] is not '-' or '': #will need to edit bc i think using 'i' means that things will ony paste in the same row, need to be able to shift rows
                    #df_exploded.loc[row, 'color'] = i
            st.write(df_exploded)
    frag()


#@st.fragment()
#def PSA_download():
 #   with open('clustalPSA.aln') as f:
  #      st.download_button('download PSA', f)
#PSA_download()
