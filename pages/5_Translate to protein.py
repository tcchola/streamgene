from io import StringIO
import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *
import biotite.sequence as seq

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - Translation",
    layout="centered"
)

########## INPUT FILED ##########
st.header("Enter DNA to Translate to protein")

# sequence_input = ">Name\n"
# sequence = st.text_area("DNA Sequence", sequence_input, height = 250)
# sequence = sequence.splitlines()
# sequence = sequence[1:]
# sequence = ''.join(sequence)

########### CHOOSE HOW YOU WANT TO INPUT THE SEQUENCE ###########
enter_option = "Enter a sequence"
upload_option = "Upload a file (FASTA)"

option = st.radio("Choose method of submitting a DNA sequence:", [enter_option, upload_option])

if option == enter_option:
    sequence_input = ">Name\n"
    sequence = st.text_area("DNA Sequence", sequence_input, height = 250)
    sequence = sequence.splitlines()
    sequence = sequence[1:]
    sequence = ''.join(sequence)

    dna = seq.NucleotideSequence(sequence)
    proteins, pos = dna.translate()
    protein = dna.translate(complete=True)

elif option == upload_option:
    uploaded_file = st.file_uploader("Choose a FASTA file", type=["fasta"], accept_multiple_files=False)

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        string_data = string_data.splitlines()
        string_data = string_data[1:]
        string_data = ''.join(string_data)
    else:
        st.warning('☝ Please choose a file!')
    
    dna = seq.NucleotideSequence(string_data)
    proteins, pos = dna.translate()
    protein = dna.translate(complete=True)


with st.expander("What is a protein?"):
    st.info("""
            Proteins are large biomolecules and macromolecules that comprise one or more 
            long chains of amino acid residues. Proteins perform a vast array of functions 
            within organisms, including catalysing metabolic reactions, DNA replication, 
            responding to stimuli, providing structure to cells and organisms, and transporting 
            molecules from one location to another. Proteins differ from one another primarily 
            in their sequence of amino acids, which is dictated by the nucleotide sequence of 
            their genes, and which usually results in protein folding into a specific 3D structure 
            that determines its activity.
    """)
    st.image("./assets/myoglobin.png", caption="Myoglobin protein")

st.write("***")

st.header("Protein")

st.write(str(protein))

st.info("If you encounter the 'ValueError' it means the genetic code does not include the rigth amount of nucleotides for translation. ⚠️")

