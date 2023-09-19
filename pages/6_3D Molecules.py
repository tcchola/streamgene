import streamlit as st
import glob
from io import StringIO
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx
from st_speckmol import speck_plot

st.set_page_config(
    page_icon="⚛️",
    page_title="StreamGene - 3D Molecules",
    layout="wide"
)

st.markdown("""
            # 3D Molecule View
            ### Open an .XYZ file and view the atomic structure.  
            Try oppening the files provided in the 'example_xyz_files' folder.  
            You can find more chemical structures on [ChemSpider](https://www.chemspider.com/)
            ***
""")

############ SIDEBAR SETTINGS ############
with st.sidebar.expander("Parameters", expanded=True):
    outl = st.checkbox('Outline', value=True)
    bond = st.checkbox('Bond', value=True)
    bond_scale = st.slider('BondScale', min_value=0.0, max_value=1.0, value=0.8)
    brightness = st.slider('Brightness', min_value=0.0, max_value=1.0, value=0.4)
    relativeAtomScale = st.slider('Relative atom scale', min_value=0.0, max_value=1.0, value=0.64)
    atomShade  = st.slider('Atom shade', min_value=0.0, max_value=1.0, value=0.5)

############ SAVE SIDEBAR SETTINGS ############
_PARAMETERS = {'outline': outl , 'bondScale': bond_scale,
                'bonds': bond ,'atomShade' : atomShade,
                'brightness': brightness, 'relativeAtomScale':relativeAtomScale,
                }

############ UPLOAD FIRST XYZ FILE ############
uploaded_file = st.file_uploader("Choose a chemical structure file", type=["xyz"], accept_multiple_files=False)
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
else:
    st.warning('☝ Please choose a file!')

############ RENDER THE STRUCTURE ############
mol  = speck_plot(string_data, _PARAMETERS = _PARAMETERS, wbox_height="500px", wbox_width="800px")