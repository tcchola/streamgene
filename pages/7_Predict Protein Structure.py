# CREDIT: This app is inspired by https://huggingface.co/spaces/osanseviero/esmfold

import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import biotite.structure.io as bsio

st.set_page_config(
    page_icon="➰",
    page_title="StreamGene - Predict Protein Structure",
    layout="wide"
)

st.markdown("""
            # Predict a Protein Structure with [ESMFold](https://esmatlas.com/about)
            ESMFold is an end-to-end single sequence protein structure predictor based on the ESM-2 language model.  
            For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.
""")

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(True)
    showmol(pdbview, height = 500,width=800)

# Protein sequence input
DEFAULT_SEQ = ""
txt = st.text_area('Input a protein sequence', DEFAULT_SEQ, height=200)

# ESMFold
def update(sequence=txt):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
    name = sequence[:3] + sequence[-3:]
    pdb_string = response.content.decode('utf-8')

    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)

    struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
    b_value = round(struct.b_factor.mean(), 4)

    # Display protein structure
    st.markdown("# Protein has been predicted")
    render_mol(pdb_string)

    # plDDT value is stored in the B-factor field
    st.markdown("""
                # plDDT
                plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100.
    """)
    st.info(f'plDDT: {b_value}')

    st.download_button(
        label="Download PDB",
        data=pdb_string,
        file_name='predictedStructure.pdb',
        mime='text/plain',
    )

predict = st.button("Predict Structure", on_click=update)

if not predict:
    st.warning('☝ Enter protein sequence data!')
    