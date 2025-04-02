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
st.header("Salario")
st.number_input("", key="input_5")



# Interface do Streamlit
st.title("Calculadora de Aumento de Salário")
salario = st.number_input("Digite o salário:", min_value=0)
resultado = calcular_aumento(salario)
st.write("Resultado:", resultado)

# Instância da classe Salario
salario_obj = Salario()
salario_obj.ajustar_salario(salario)


