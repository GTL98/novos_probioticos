# --- Importar as bibliotecas --- #
import json
from distancia_hamm import distancia_hamm

# --- Ler o arquivo JSON --- #
with open('./sequencias_json.json', 'r') as doc:
    sequencias = json.load(doc)

# --- Obter as sequências da chave "Bifidobacterium aemilianum" --- #
bifido_aemi = sequencias['Bifidobacterium aemilianum']

# --- Obter as sequências da chave "Bifidobacterium pullorum" --- #
bifido_pull = sequencias['Bifidobacterium pullorum']

# --- Criar um dicionário para armazenar a distância de Hamming --- #
dic_distancia = {}

# --- Distância HAMM de Bifidobacterium aemilianum --- #
for bifido in sequencias:
    dic_distancia[bifido] = {}
    for cluster in sequencias[bifido]:
        dic_distancia[bifido][cluster] = {}
        # Obter "seq_1"
        seq_1 = sequencias[bifido][cluster][bifido]
        for bacteria in sequencias[bifido][cluster]:
            if bacteria != bifido:
                # Obter "seq_2"
                seq_2 = sequencias[bifido][cluster][bacteria]
                distancia = distancia_hamm(seq_1, seq_2)
                dic_distancia[bifido][cluster][bacteria] = distancia

# --- Criar o arquivo JSON com as distâncias Hamming --- #
dados_json = json.dumps(
    obj=dic_distancia,
    indent=4
)
with open('distancia_hamm.json', 'w') as doc:
    doc.write(dados_json)
