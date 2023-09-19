from io import StringIO
import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene",
    layout="centered"
)

########## INPUT FILED ##########
st.header("Enter DNA Sequence")

sequence_input = ""
sequence = st.text_area("Sequence Input", sequence_input, height = 250) #input box settings
sequence = sequence.splitlines() #split lines and view each one as separate entity
sequence = sequence[1:] #skip index 0 and go to beginning of sequence
sequence = ''.join(sequence) #merge all lines

st.write("***")
########## OUTPUT FIELD ##########
st.header("Output")
st.subheader("1. Data Sheet View")

def NucleotideCounter(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('C', seq.count('C')),
        ('G', seq.count('G'))
    ])
    return d

########## OUTPUT TABLE ##########
NucleotideOutput = NucleotideCounter(sequence)

table = pd.DataFrame.from_dict(NucleotideOutput, orient = "index")
table = table.rename({0: "Amount"}, axis = "columns")
table.reset_index(inplace = True)
table = table.rename(columns = {"index" : "Nucleotides"})
st.write(table)

########## OUTPUT CHART ##########
st.subheader("2. Chart View")
plot = alt.Chart(table).mark_bar().encode(
    x = "Nucleotides",
    y = "Amount"
)
plot = plot.properties(
    width = alt.Step(50) # width of plot bars
)
st.write(plot)

st.write("""
         ***
""")
