from io import StringIO
import streamlit as st
import biotite.sequence as seq

st.set_page_config(
    page_icon="🧬",
    page_title="StreamGene - Second Strand",
    layout="centered"
)

########## INPUT FILED ##########
st.markdown("""
            # Get DNA Complement Strand
""")

sequence_input = ">Name\n"
sequence = st.text_area("Enter 5' - 3' DNA Strand", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write(f'Sequence Length: {len(sequence)}')

with st.expander("What is a reverse complement strand?"):
    st.info("""
            In genetics, complementary DNA (cDNA) is DNA synthesized from a single-stranded RNA 
            (e.g., messenger RNA (mRNA) or microRNA (miRNA)) template in a reaction catalyzed by 
            the enzyme reverse transcriptase. cDNA is often used to express a specific protein 
            in a cell that does not normally express that protein (i.e., heterologous expression), 
            or to sequence or quantify mRNA molecules using DNA based methods (qPCR, RNA-seq). 
            cDNA that codes for a specific protein can be transferred to a recipient cell for expression, 
            often bacterial or yeast expression systems. cDNA is also generated to analyze transcriptomic 
            profiles in bulk tissue, single cells, or single nuclei in assays such as microarrays, qPCR, and RNA-seq.
    """)
    st.image("./assets/reverse_strand.png")

reverse_strand = seq.NucleotideSequence(sequence).reverse().complement()
st.markdown("""
            ## 3' - 5' DNA Strand
""")
st.write(reverse_strand)

