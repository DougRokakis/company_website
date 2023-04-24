import streamlit as st
import pandas 

st.set_page_config(layout="wide")

st.header("SP Inc.")
company_blurb= """
    Changing the way you look at Streamlit one app at a time.
    """
st.write(company_blurb)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("company_website_photos/"+row['image']+"")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("company_website_photos/"+row['image']+"")
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("company_website_photos/"+row['image']+"")