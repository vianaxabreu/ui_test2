import streamlit as st
import requests


st.write("Hello world")
url = "https://test2api-dpfs3q2bcq-uc.a.run.app/"

name = st.text_input('What is your name', 'Antonella')

if st.button('click me'):
    # print is visible in the server output, not in the page
    st.write('I was clicked 🎉')
    r = requests.get(f"{url}/predict?name={name}")
    if r.status_code == 200:
        st.write(r.json())
else:
    st.write('I was not clicked 😞')
