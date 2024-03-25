import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.png")

with col2:
    st.title("Swapnil Acharjee")
    content = ("""
    Greetings! I am Swapnil Acharjee, an engineering student, pursuing a B.Tech degree in the field of Computer Science and Engineering (CSE).
    I am also a python programmer.
    
    I've made this website to serve as a potential portfolio of me.  It's purpose is to showcase some of the projects I've accomplished using python.
    It lists 20 real world applications that I have developed using python along with link to their source code.
    Along with that, the website itself is developed using python and is one of my python projects.
    """)
    st.info(content)