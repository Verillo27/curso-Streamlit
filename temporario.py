import pandas as pd
import streamlit as st
st.button("botao salvar")
st.header("cabeçalho")
st.toggle("ligar se vc for massa")
st.text_input("")
st.text_area("enter text")
st.selectbox(
  "qual você prefere",
  ("marvel","dc", "nenhum"))
st.multiselect(
  "quais sao suas cores favoritas",
  ["verde","azul","roxo",],
  ["azul","roxo"])
st.checkbox("Sorvete")
st.checkbox("refri")
st.color_picker("pick a color", "#00F900")
st.feedback("stars")
df = pd.dataframe(
  [
    {"command" : "st.selectbox", "rating" : 4,"is_widget" : True},
     {"command" : "st.ballons", "rating" : 5,"is_widget" : False},
     {"command" : "st.time_input", "rating" : 3,"is_widget" : True},
  ]
)
edited_df = st.data_editor(df)
