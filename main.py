# --- Importar as bibliotecas --- #
import pandas as pd
from json import load
import streamlit as st
from gerar_grafico import gerar_grafico

# --- Abrir o arquivo JSON --- #
with open('distancia_hamm.json', 'r') as doc:
    dados_json = load(doc)

# --- Criar uma caixa de seleção com as chaves --- #
chave_1 = st.selectbox(
    label='Escolha uma chave:',
    options=[
        'Bifidobacterium aemilianum',
        'Bifidobacterium pullorum'
    ],
    placeholder='Selecione uma bactéria',
    index=None
)

# --- Obter os dados da chave selecionada --- #
try:
    dados_1 = dados_json[chave_1]
except KeyError:
    pass
else:
    # --- Criar uma lista para armazenar os clusters que são as chaves --- #
    clusters = [cluster for cluster in dados_1]

    # --- Criar uma caixa de seleção para selecionar o cluster --- #
    chave_2 = st.selectbox(
        label='Escolha uma chave:',
        options=clusters,
        placeholder='Selecione um cluster',
        index=None
    )

    # --- Obter os dados da chave selecionada --- #
    try:
        dados_2 = dados_1[chave_2]
    except KeyError:
        pass
    else:
        # --- Colocar um slider para selecionar o mínimo e máximo da distância Hamming --- #
        lista_dis_hamm = [distancia for distancia in dados_2.values()]
        intervalo = st.slider(
            label='Escolha um intervalo:',
            min_value=min(lista_dis_hamm),
            max_value=max(lista_dis_hamm),
            value=(min(lista_dis_hamm), max(lista_dis_hamm))
        )

        # --- Chamar a função que gera os gráficos --- #
        gerar_grafico(intervalo[0], intervalo[1], dados_2)
