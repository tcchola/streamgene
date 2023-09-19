import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - GC Content and AT/GC ratio",
    layout="centered"
)

st.header("Calculate GC Content and AT/GC ratio of DNA Strand")

sequence_input = ">Name\n"
sequence = st.text_area("DNA Sequence", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write(f'Sequence Length: {len(sequence)}')

with st.expander("What is GC content?"):
    st.info("""
                In molecular biology and genetics, GC-content (or guanine-cytosine content) is the percentage of
                nitrogenous bases in a DNA or RNA molecule that are either guanine (G) or cytosine (C). This
                measure indicates the proportion of G and C bases out of an implied four total bases, also including
                adenine and thymine in DNA and adenine and uracil in RNA. GC-content may be given for a certain fragment
                of DNA or RNA or for an entire genome. When it refers to a fragment, it may denote the GC-content of an
                individual gene or section of a gene (domain), a group of genes or gene clusters, a non-coding region,
                or a synthetic oligonucleotide such as a primer.
    """)

with st.expander("Its applications in molecular biology..."):
    st.info("""
            In polymerase chain reaction (PCR) experiments, the GC-content of short oligonucleotides known as primers
            is often used to predict their annealing temperature to the template DNA. A higher GC-content level indicates
            a relatively higher melting temperature. Many sequencing technologies, such as Illumina sequencing, have trouble
            reading high-GC-content sequences. Bird genomes are known to have many such parts, causing the problem of
            "missing genes" expected to be present from evolution and phenotype but never sequenced — until improved methods were used.
    """)

with st.expander("Its applications in systematics..."):
    st.info("""
            The species problem in non-eukaryotic taxonomy has led to various suggestions in classifying bacteria, and the
            ad hoc committee on reconciliation of approaches to bacterial systematics of 1987 has recommended use of GC-ratios
            in higher-level hierarchical classification. For example, the Actinomycetota are characterised as "high GC-content
            bacteria". In Streptomyces coelicolor A3(2), GC-content is 72%. With the use of more reliable, modern methods of
            molecular systematics, the GC-content definition of Actinomycetota has been abolished and low-GC bacteria of this clade have been found.
    """)

st.write("***")

st.info("If you encounter the 'ZeroDivisionError' it just means that the input filed is empty. ⚠️")

col1, col2 = st.columns(2)

with col1:
    st.header(f"GC: {calculateGC(sequence)}%")
    st.markdown("#### Formula for GC content:")
    st.latex(r"""
             \frac{G + C}{A + T + G + C} * 100\%
    """)

with col2:
    st.header(f"AT/CG: {calculateATGCratio(sequence)}")
    st.markdown("#### Formula for AT/GC ratio:")
    st.latex(r"""
         \frac{A + T}{G + C}
    """)