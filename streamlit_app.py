from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Valor Caronas

"""

gas_price = st.number_input('Valor Combustível')

pedro_rides_count = [None] * 6
carlos_rides_count = [None] * 6

col1, col2 = st.columns(2)

with col1:
    st.header("Caronas Pedro")
    pedro_rides_count[0] = st.number_input('GABRIEL', min_value=0, step=1, key="gabrielToPedro")
    st.write("Valor a pagar = ")
    pedro_rides_count[1] = st.number_input('GIOVANNA', min_value=0, step=1, key="giovannaToPedro")
    st.write("Valor a pagar = ")
    pedro_rides_count[2] = st.number_input('GIOVANA', min_value=0, step=1, key="giovanaToPedro")
    st.write("Valor a pagar = ")
    pedro_rides_count[3] = st.number_input('LUCAS', min_value=0, step=1, key="lucasToPedro")
    st.write("Valor a pagar = ")
    pedro_rides_count[4] = st.number_input('LEO', min_value=0, step=1, key="leoToPedro")
    st.write("Valor a pagar = ")
    pedro_rides_count[5] = st.number_input('CARLOS', min_value=0, step=1, key="carlosToPedro")
    st.write("Valor a pagar = ")

with col2:
    st.header("Caronas Carlos")
    carlos_rides_count[0] = st.number_input('GABRIEL', min_value=0, step=1, key="gabrielToCarlos")
    st.write("Valor a pagar = ")
    carlos_rides_count[1] = st.number_input('PEDRO', min_value=0, step=1, key="pedroToCarlos")
    st.write("Valor a pagar = ")
    carlos_rides_count[2] = st.number_input('LUCAS', min_value=0, step=1, key="lucasToCarlos")
    st.write("Valor a pagar = ")
    carlos_rides_count[3] = st.number_input('LEO', min_value=0, step=1, key="leoToCarlos")
    st.write("Valor a pagar = ")

st.button('SALVAR E ATUALIZAR')