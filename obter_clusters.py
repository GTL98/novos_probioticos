# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO
from json import dumps

# --- Possíveis novos probióticos --- #
bacterias = ['Bifidobacterium aemilianum', 'Bifidobacterium pullorum']

# --- Dicionário para armazenar os clusters de cada bactéria --- #
dados = {}

# --- Caminho do diretório --- #
caminho = '../bacterias_probioticas/probioticos_50'
# --- Iterar sobre cada arquivo que possua a bactéria --- #
for bacteria in bacterias:
    dados[bacteria] = []
    for arquivo in os.listdir(caminho):
        for registro in SeqIO.parse(f'{caminho}/{arquivo}', 'fasta'):
            if bacteria in registro.description:
                cluster = arquivo.split('_')[1].split('.')[0]
                if cluster not in dados[bacteria]:
                    dados[bacteria].append(cluster)

# --- Escrever no arquivo JSON --- #
dados_json = dumps(dados, indent=4)
with open('probioticos.json', 'w') as doc:
    doc.write(dados_json)
