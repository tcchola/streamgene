import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - GC Content",
    layout="centered"
)

st.header("Calculate GC Content of DNA Strand")

sequence_input = ""
sequence = st.text_area("DNA Sequence", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write(f'Sequence Length: {len(validateSequence(sequence))}')
st.write("***")

st.header(f"GC: {calculateGC(sequence)}%")

st.subheader("Formula")
st.latex(r"""
         \frac{nG + nC}{\vert string \vert} * 100
""")