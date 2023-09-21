import streamlit as st
from io import StringIO
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio

st.set_page_config(
    page_icon="⚛️",
    page_title="StreamGene - 3D Molecules",
    layout="wide"
)

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(True)
    showmol(pdbview, height=800, width=1000)

st.markdown("""
            # 3D Molecule View
            ### Open a .PDB file and view the molecular structure.
            You can find more structures on [RCSB PDB](https://www.rcsb.org/)
""")

with open('./example_pdb_files.zip', 'rb') as f:
   st.download_button('Download example PDB files', f, file_name='example_pdb_files.zip')

st.write("***")

uploaded_file = st.file_uploader("Choose a PDB file", type=["pdb"], accept_multiple_files=False)

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    protein_string = stringio.read()
    render_mol(protein_string)
else:
    st.warning('☝ Please choose a file!')
