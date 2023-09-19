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

sequence_input = ">Name\n"
sequence = st.text_area("DNA Sequence", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

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

########## DNA TO PROTEIN OUTPUT ##########
st.info("If you encounter the 'ValueError' it means the genetic code does not include the rigth amount of nucleotides for translation. ⚠️")

dna = seq.NucleotideSequence(sequence)
proteins, pos = dna.translate()

for i in range(len(proteins)):
    print(
        f"Protein sequence {str(proteins[i])} "
        f"from base {pos[i][0]+1} to base {pos[i][1]}"
    )

protein = dna.translate(complete=True)

st.write(str(protein))