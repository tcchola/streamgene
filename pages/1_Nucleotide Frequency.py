from io import StringIO
import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - Nucleotide Frequencey",
    layout="centered"
)

########## INPUT FILED ##########
st.markdown("""
            # Count Aminoacids in a Sequence
            ***
            ## Enter Sequence
""")

sequence_input = ">Name\n"
sequence = st.text_area("Sequence Input", sequence_input, height = 250)
sequence = sequence.splitlines() #split lines and view each one separately
sequence = sequence[1:] #skip index 0 and go to beginning of sequence
sequence = ''.join(sequence) #merge all lines

with st.expander("What are nucleotides?"):
    st.info("""
            Nucleotides are organic molecules composed of a nitrogenous base, a pentose sugar and a phosphate. 
            They serve as monomeric units of the nucleic acid polymers – deoxyribonucleic acid (DNA) and ribonucleic 
            acid (RNA), both of which are essential biomolecules within all life-forms on Earth. Nucleotides are obtained 
            in the diet and are also synthesized from common nutrients by the liver.
    """)
    st.image("./assets/nucleotides.png")

def NucleotideCounter(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('C', seq.count('C')),
        ('G', seq.count('G'))
    ])
    return d

NucleotideOutput = NucleotideCounter(sequence)

col1, col2 = st.columns(2)

########## OUTPUT TABLE ##########
with col1:
    st.markdown("""
            ***
            ### 1. Data Sheet View
    """)
    table = pd.DataFrame.from_dict(NucleotideOutput, orient = "index")
    table = table.rename({0: "Amount"}, axis = "columns")
    table.reset_index(inplace = True)
    table = table.rename(columns = {"index" : "Nucleotides"})
    st.write(table)

########## OUTPUT CHART ##########
with col2:
    st.markdown("""
                ***
                ### 2. Chart View
    """)

    plot = alt.Chart(table).mark_bar().encode(
        x = "Nucleotides",
        y = "Amount"
    )
    plot = plot.properties(
        width = alt.Step(50) # width of plot bars
    )
    st.write(plot)