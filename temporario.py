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
st.color_picker("pick a color", #ooF900")
st.feedback("stars")
