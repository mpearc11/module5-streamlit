import streamlit as st
from Bio import Blast
from Bio import Align
from Bio.Seq import Seq
from Bio import SeqIO
from io import StringIO
#from Bio.Align.Applications import ClustalOmegaCommandLine
from Bio import AlignIO

st.title('EvoScore Calculation')

st.header('Submit Sequences for PSA')

target_file = st.file_uploader("",type='fasta')

if target_file is not None:
    st.success("target FASTA file uploaded")
else:
    st.info("please upload your target FASTA file")

ps_file = st.file_uploader("",type='fasta',key=2)

if ps_file is not None:
    st.success("project standard FASTA file uploaded")
else:
    st.info('please upload the project standard FASTA file')

if st.button('create PSA'):
    target_sio=StringIO(target_file.getvalue().decode('utf-8'))
    target_record=SeqIO.read(target_sio,'fasta')
    target=str(target_record.seq)
    query_sio=StringIO(ps_file.getvalue().decode('utf-8'))
    query_record=SeqIO.read(query_sio,'fasta')
    query=str(query_record.seq)

    aligner = Align.PairwiseAligner()
    
    alignment = aligner.align(target,query)
    st.write(alignment[0])
    #alignment = alignment[0]
    with open('clustalPSA.fasta', "w") as handle:
        AlignIO.write(alignment, handle, 'clustal')
    
    #clustalomega_cline=ClustalOmegaCommandLine(infile='PSA.fasta',outfile='culstalPSA.fasta')

@st.fragment()
def PSA_download():
    with open('clustalPSA.fasta') as f:
        st.download_button('download PSA', f)
PSA_download()
