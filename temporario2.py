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

# Função para calcular aumento
def calcular_aumento(salario):
    if salario < 2500:
        return "aumento"
    else:
        return "não aumento"

# Classe para gerenciar aumento
class Salario:
    def __init__(self, aumento=0):
        self.aumento = aumento

    def ajustar_salario(self, salario):
        while salario == 500:
            self.aumento += 100
            st.write("Aumento de salário:", salario)
            salario += self.aumento

salario = st.number_input("Digite o salário:", min_value=0)
resultado = calcular_aumento(salario)
st.write("Resultado:", resultado)

salario_obj = Salario()
salario_obj.ajustar_salario(salario)

def calcular_novo_salario(salario, aumento):
    novo_salario = salario + aumento
    return novo_salario


st.title("Calculadora de Aumento de Salário")
salario_inicial = st.number_input("Digite o salário inicial:", min_value=0)
aumento = st.number_input("Digite o valor do aumento:", min_value=0, value=500)

if st.button("Calcular novo salário"):
    novo_salario = calcular_novo_salario(salario_inicial, aumento)
    st.write(f"O novo salário após um aumento de {aumento} é {novo_salario}.")
