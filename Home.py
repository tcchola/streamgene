import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(
    page_icon="🦠",
    page_title="StreamGene",
    layout="centered"
)

########## APP DESCRIPTION ##########
st.write("""
         # Welcome to StreamGene 🧬
         The all-in-one web application for analisys of genetic code.
         ***
""")

st.header("Q&A Section")

st.subheader("1. How do I find the number of ACTGs?")
st.write("""
         Take a DNA sequence from any online library and copy it into the input box 
         on the 'Nucleotide Frequency' page to find out the exact number of nucleotides in your sequence.
""")

st.subheader("2. How do I get RNA strand from DNA?")
st.write("""
         Go to the 'Transcribe' page on the side menu and copy your DNA sequence 
         into the input box. This will show you the corresponding RNA strand.
""")

st.subheader("3. How can I know what proteins my strand can make?")
st.write("""
         You can head over to the 'Translate to protein' page on the side menu and 
         copy your RNA strand into the input box. You will be shown all possible proteins from the sequence.
""")

st.subheader("4. How can I get the complement strand of my DNA?")
st.write("""
         Go to the 'Second Strand' page on the side menu and copy your DNA sequence 
         into the input box. This will give you your complement strand.
""")

st.subheader("5. How sticky are my strand ends?")
st.write("""
         The more Gs and Cs a sequence has the stickier it is. We call this GC content. 
         By going to the 'GC Content' page you can copy your sequence into the input box 
         and find your GC content in percentage [%].
""")

st.subheader("6. Why am I getting inaccurate results?")
st.write("""
         The app automaticaly skips the first line of the input box (or index 0). 
         So when pasting your sequence make sure it looks something like this:\n
         >Name_of_organism_[...]\n
         >>ACTGACTGACTG...
""")

st.write("***")

st.header("About the app")

st.subheader("""
             This app was made using the Python web framework 'streamlit'. This app is completely free and open source. You can visit my GitHub repository here\n
""")
st.write("https://github.com/tcchola/streamgene ")
