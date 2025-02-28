import streamlit as st
import datetime

st.header("CPF")
st.text_input("", key="input_1")
st.header("nome")
st.text_input("", key="input_2")
st.header("nascimento")
st.date_input("Qual seu aniversario", datetime.date(1, 1, 2000))
st.header("email")
st.text_input("", key="input_3")
st.header("telefone")
st.text_input("", key="input_4")
