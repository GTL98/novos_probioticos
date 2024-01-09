# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO
from json import dumps

# --- Lista com os "novos" probióticos --- #
bacterias = ['Bifidobacterium aemilianum', 'Bifidobacterium pullorum']

sequencias = {}

# --- Iterar sobre cada entrada dos arquivos FASTA --- #
for bacteria in bacterias:
    sequencias[bacteria] = {}
    for arquivo in os.listdir(f'./{bacteria}'):
        cluster = arquivo.split('_')[1].split('.')[0].strip()
        sequencias[bacteria][cluster] = {}
        for registro in SeqIO.parse(f'./{bacteria}/{arquivo}', 'fasta'):
            bacteria_fasta = registro.description.split('|')[1].split('[')[1].split(']')[0].strip()
            sequencias[bacteria][cluster][bacteria_fasta] = str(registro.seq)

# --- Criar o arquivo JSON com as sequências --- #
dados_json = dumps(
    obj=sequencias,
    indent=4
)
with open('./sequencias_json.json', 'w') as doc:
    doc.write(dados_json)
