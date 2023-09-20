import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(
    page_icon="🦠",
    page_title="StreamGene - Welcome",
    layout="wide"
)

########## APP DESCRIPTION ##########
st.markdown('''
            # Welcome to StreamGene 🦠
            ### The all-in-one web application for analisys of genetic code.
            
            ***
                    
            # Q&A Section

            ## 1. How do I find the number of ACTGs? #️⃣
            Take a DNA sequence from any online library and copy it into the input box or open a .FASTA file  
            on the 'Nucleotide Frequency' page to find out the exact number of nucleotides in your sequence.

            ## 2. How can I find my reverse complemet strand? ⛓️
            Head to the 'Second Strand' page and copy your 5' - 3' strand into the input box.  
            As a result you will get the 3' - 5' complement strand.

            ## 3. How sticky are my strand ends? 🔗
            The more Gs and Cs a sequence has the stickier it is. We call this GC content. By going to  
            the 'GC Content' page you can copy your sequence into the input box and find your GC content in percentage [%].

            ## 4. How do I get RNA strand from DNA? 🧬
            Go to the 'Transcribe' page on the side menu and copy your DNA sequence into the input box.  
            This will show you the corresponding RNA strand.

            ## 5. How can I know what proteins my strand can make? 💪
            You can head over to the 'Translate to protein' page on the side menu and copy your DNA strand  
            into the input box or open a .FASTA file. The proteins will be displayed below.

            ## 6. Why am I getting inaccurate results? ❌
            The app automaticaly skips the first line of the input box (index 0). So when pasting your  
            sequence make sure it looks something like this:\n
            ```
                >Name_of_organism_
                ACTGACTGACTGACTGACTGACTGACTG
                GTCAGTCAGTCAGTCA...
            ```

            ## 7. Can I predict how my protein will fold? ➰
            Yes. Head over to the 'Predict Protein Structure' page and input the protein you transcribed.  
            The app will generate a 3D model along with the accuracy score of the prediction.

            ***

            # About the app 🧩
            ### This app was made using the Python web framework [streamlit](https://streamlit.io/). 🐍
            ### This app is published under the MIT open source license. 📂
            ### You can visit the [GitHub repository here.](https://github.com/tcchola/streamgene) 👾
''')
