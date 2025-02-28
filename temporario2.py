import streamlit as st
import datetime

st.header("CPF")
st.text_input("", key="input_1")
st.header("nome")
st.text_input("", key="input_2")
st.header("nascimento")
d = st.date_input("Qual seu aniversario", datetime.date(2019, 7, 6)
st.header("email")
st.text_input("", key="input_3")
st.header("telefone")
st.text_input("", key="input_4")
