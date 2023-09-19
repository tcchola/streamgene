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
sequence = st.text_area("5' - 3' DNA Strand", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("***")

st.write(f'Sequence Length: {len(validateSequence(sequence))}')

reverse_strand = reverseComplement(sequence)
st.header("3' - 5' Complement DNA Strand")
st.subheader(reverse_strand)