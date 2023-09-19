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
st.header("Enter RNA to be Trnaslated to a protein")

sequence_input = ""
sequence = st.text_area("RNA Sequence", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("***")

st.header("Proteins")

st.subheader(f'All proteins in 6 open reading frames')
for protein in all_proteins(sequence, 0, 0, True):
    st.write(protein)