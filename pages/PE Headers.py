import streamlit as st
import numpy as np
import re
from Extract.PE_app import PE_scanner
from tensorflow import keras
import os


st.markdown('## PE scanner:')
upload_files = st.file_uploader(
            'Choose files: ', accept_multiple_files=True, type=None)
pe_scanner = PE_scanner()
if len(upload_files):
            if not os.path.exists('TestFile\\temp'):
                os.mkdir('TestFile\\temp')
            with st.spinner("Checking files..."):
                for i in upload_files:
                    with open(f'TestFile\\temp\\temp_{i.id}', 'wb') as file:
                        file.write(i.getvalue())
                        legitimate = pe_scanner.PE_scan(
                            f'TestFile\\temp\\temp_{i.id}')
                        if legitimate:
                            st.success(
                                f"File {i.name} is safe.", icon="✅")
                        else:
                            mal_class = pe_scanner.PE_mal_classify(
                                f'TestFile\\temp\\temp_{i.id}')
                            st.warning(
                                f"File {i.name} is malicious. The malware is most likely belongs to {mal_class}", icon='🚨')
                    file.close()
                # shutil.rmtree(f'TestFile\\temp')

st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <p style='color: #494848;'>Made by Jaynam</p>
    </div>
    """, unsafe_allow_html=True)