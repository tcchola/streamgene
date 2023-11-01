from io import StringIO
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - Nucleotide Frequencey",
    layout="centered"
)

########## INPUT FILED ##########
st.markdown("""
            # Count Nucleotides in a Sequence
            ## Enter Sequence
""")

def NucleotideCounter(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('C', seq.count('C')),
        ('G', seq.count('G'))
    ])
    return d

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

    NucleotideOutput = NucleotideCounter(sequence)

elif option == upload_option:
    uploaded_file = st.file_uploader("Choose a FASTA file", type=["fasta", "fa"], accept_multiple_files=False)

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()

        NucleotideOutput = NucleotideCounter(string_data)

    else:
        st.warning('☝ Please choose a file!')

with st.expander("What are nucleotides?"):
    st.info("""
            Nucleotides are organic molecules composed of a nitrogenous base, a pentose sugar and a phosphate. 
            They serve as monomeric units of the nucleic acid polymers – deoxyribonucleic acid (DNA) and ribonucleic 
            acid (RNA), both of which are essential biomolecules within all life-forms on Earth. Nucleotides are obtained 
            in the diet and are also synthesized from common nutrients by the liver.
    """)
    st.image("./assets/nucleotides.png")

with st.expander("What is a FASTA file?"):
    st.info("""
            In bioinformatics and biochemistry, the FASTA format is a text-based format for representing either nucleotide 
            sequences or amino acid (protein) sequences, in which nucleotides or amino acids are represented using single-letter codes.
    """)
    st.markdown("""
                `>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
                MADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTID
                FPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREA
                DIDGDGQVNYEEFVQMMTAK*`
    """)

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
