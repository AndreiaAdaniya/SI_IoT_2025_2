import streamlit as st
st.title("Hello Massaki")
st.write("Opa! Eu sei fazer site!")

# streamlit 30 days - Day 3

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
