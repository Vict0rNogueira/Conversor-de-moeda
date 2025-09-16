import streamlit as st
from conversor import ConversorMoeda

st.title("💱 Conversor de Moedas Interativo")

moedas = ["USD", "EUR", "BRL", "JPY", ]

moeda_origem = st.selectbox("Moeda de origem:", moedas)
moeda_destino = st.selectbox("Moeda de destino:", moedas)

valor = st.number_input(f"Valor em {moeda_origem}:", min_value=0.0, format="%.2f")

if st.button("Converter"):
    conversor = ConversorMoeda()
    resultado = conversor.converter(valor, moeda_origem, moeda_destino)
    
    if resultado is not None:
        st.success(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
    else:
        st.error("Não foi possível obter a cotação.")
