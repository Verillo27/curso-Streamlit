import streamlit as st
import datetime

st.header("Nome")
st.text_input("", key="input_1")
st.header("Sobrenome")
st.text_input("", key="input_2")
st.header("nascimento")
d = st.date_input("Qual é seu aniversario", 
                  format="DD.MM.YYYY")
st.header("Estado Civil")
st.text_input("", key="input_3")
st.header("Sexo")
st.text_input("", key="input_4")
st.header("Salario")
st.text_input("", key="input_5")

# Título do aplicativo
st.title("Escolha uma opção")

# Lista de opções
opcoes = ["Opção 1", "Opção 2", "Opção 3"]

# Selectbox para escolher uma opção
escolha = st.selectbox("Selecione uma opção:", opcoes)
