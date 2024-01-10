# --- Importar as bibliotecas --- #
import streamlit as st


def gerar_grafico(min_dis: int, max_dis: int, dados: dict):
    """
    Função responsável por mostrar o intervalo do gráfico.
    :param min_dis: Distância de Hamming mínima do cluster.
    :param max_dis: Distância de Hamming máxima do cluster.
    """
    # --- Criar o dicionário com as bactérias que pertencem ao intervalo da distância de Hamming --- #
    dic_intervalo = {}

    # --- Verificar se a distância de Hamming pertence ao intervalo --- #
    for bacteria, dist_hamm in dados.items():
        if min_dis <= dist_hamm <= max_dis:
            dic_intervalo[bacteria] = dist_hamm

    # --- Gerar o gráfico com os dados do intervalo --- #
    st.bar_chart(dic_intervalo)
