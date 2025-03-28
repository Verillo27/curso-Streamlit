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
opcoes = ["Solteiro", "Casado", "Divorciado", "Viuvo"]
st.header("Sexo")
opcoes = ["Mulher", "Homem"]
st.header("Salario")
st.text_input("", key="input_5")



# Lista de opções
opcoes = ["Opção 1", "Opção 2", "Opção 3"]

# Selectbox para escolher uma opção
escolha = st.selectbox("Selecione uma opção:", opcoes)
