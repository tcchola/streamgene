from io import StringIO
import streamlit as st
import pandas as pd
import altair as alt
from analisys.structures import *
import biotite.sequence as seq

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - Transcription",
    layout="centered"
)

st.markdown("""
            # Transcribe DNA to mRNA
""")

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

    st.write(f'Sequence Length: {len(sequence)}')
    
    if sequence:
        st.header("Transcribed RNA:")
        st.write(f'Sequence Length: {len(sequence)}')
        st.write(transcribe(sequence))
    else:
        st.warning("☝ Please enter a DNA sequence.")
    
elif option == upload_option:
    uploaded_file = st.file_uploader("Choose a FASTA file", type=["fasta"], accept_multiple_files=False)

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        string_data = string_data.splitlines()
        string_data = string_data[1:]
        string_data = ''.join(string_data)

        st.write(f'Sequence Length: {len(string_data)}')

        st.header("Transcribed RNA:")
        st.write(f'Sequence Length: {len(string_data)}')
        st.write(transcribe(string_data))

    else:
        st.warning('☝ Please choose a file.')

st.write("***")

with st.expander("What is RNA?"):
    st.info("""
            Ribonucleic acid (RNA) is a polymeric molecule that is essential for most biological functions, 
            either by performing the function itself (Non-coding RNA) or by forming a template for production 
            of proteins (messenger RNA). RNA and deoxyribonucleic acid (DNA) are nucleic acids. The nucleic 
            acids constitute one of the four major macromolecules essential for all known forms of life. 
            RNA is assembled as a chain of nucleotides. Cellular organisms use messenger RNA (mRNA) to convey 
            genetic information (using the nitrogenous bases of guanine, uracil, adenine, and cytosine, denoted 
            by the letters G, U, A, and C) that directs synthesis of specific proteins. Many viruses encode their 
            genetic information using an RNA genome.
    """)
    st.image("./assets/rna.png")

with st.expander("What is transcription?"):
    st.info("""
            Transcription is the process of copying a segment of DNA into RNA. The segments of DNA transcribed 
            into RNA molecules that can encode proteins are said to produce messenger RNA (mRNA). Other segments 
            of DNA are copied into RNA molecules called non-coding RNAs (ncRNAs). mRNA comprises only 1–3% of total 
            RNA samples. Less than 2% of the human genome can be transcribed into mRNA (Human genome#Coding vs. 
            noncoding DNA), while at least 80% of mammalian genomic DNA can be actively transcribed (in one or more 
            types of cells), with the majority of this 80% considered to be ncRNA.
    """)

with st.expander("Steps of transcription..."):
    st.info("""
            Transcription proceeds in the following general steps:  
            1. RNA polymerase, together with one or more general transcription factors, binds to promoter DNA.
            2. RNA polymerase generates a transcription bubble, which separates the two strands of the DNA helix. This is done by breaking the hydrogen bonds between complementary DNA nucleotides.
            3. RNA polymerase adds RNA nucleotides (which are complementary to the nucleotides of one DNA strand).
            4. RNA sugar-phosphate backbone forms with assistance from RNA polymerase to form an RNA strand.
            5. Hydrogen bonds of the RNA–DNA helix break, freeing the newly synthesized RNA strand.
            6. If the cell has a nucleus, the RNA may be further processed. This may include polyadenylation, capping, and splicing.
            7. The RNA may remain in the nucleus or exit the cytoplasm through the nuclear pore complex.
    """)
