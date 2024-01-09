# --- Importar as bibliotecas --- #
from json import load
from Bio import SeqIO

# --- Caminho com os arquivos FASTA --- #
caminho = '../bacterias_probioticas/probioticos_50'

# --- Abrir o arquivo --- #
with open('probioticos.json', 'r') as doc:
    dados = load(doc)

# --- Lista com as "novas" bactérias probióticas --- #
bacterias = ['Bifidobacterium aemilianum', 'Bifidobacterium pullorum']

# --- Iterar sobre cada cluster em que a bactéria está presente --- #
for bacteria in bacterias:
    for cluster in dados[bacteria]:
        for registro in SeqIO.parse(f'{caminho}/Cluster_{cluster}.fasta', 'fasta'):
            # Criar um arquivo FASTA somente com o mesmo gênero dos "novos" probióticos
            genero = bacteria.split(' ')[0].strip()
            if genero in registro.description:
                if 'partial' not in registro.description:
                    with open(f'./{bacteria}/Cluster_{cluster}.fasta', 'a') as doc:
                        fasta = f'''>{registro.description}
{registro.seq}\n'''
                        doc.write(fasta)
