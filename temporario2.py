import streamlit as st
import datetime

st.header("Nome")
st.text_input("", key="input_1")
st.header("Sobrenome")
st.text_input("", key="input_2")
st.header("nascimento")
d = st.date_input("Qual é seu aniversario", 
 format="DD.MM.YYYY")
st.title("Estado Civil")
opcoes = ["Solteiro", "Casado", "Divorciado", "Viuvo"]
escolha = st.selectbox("Selecione uma opção:", opcoes)
st.title("Sexo")
opcoes = ["Mulher", "Homem"]
escolha = st.selectbox("Selecione uma opção:", opcoes)




