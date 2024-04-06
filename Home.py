import streamlit as st
import pandas as pd

st.set_page_config(page_title='Company Website', layout='wide')

st.sidebar.header('Home')

st.header('The Best Company')

header_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla dapibus consequat felis, eu 
venenatis lectus fermentum vel. Suspendisse iaculis erat mi, at pulvinar risus cursus vel.
Etiam vitae semper quam, eget molestie mauris. Suspendisse placerat sit amet mi nec aliquam. 
Maecenas pellentesque mi quis tincidunt fermentum. In erat felis, sollicitudin non felis ac, 
porta consectetur urna. Vestibulum luctus libero mauris.
"""

st.write(header_text)

st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

df_data = pd.read_csv('data.csv')


with col1:
    for index, row in df_data[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row['role'])
        st.image('images/' + row['image'])


with col2:
    for index, row in df_data[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row['role'])
        st.image('images/' + row['image'])


with col3:
    for index, row in df_data[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row['role'])
        st.image('images/' + row['image'])
