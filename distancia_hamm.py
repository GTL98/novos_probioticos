def distancia_hamm(seq_1: str, seq_2: str):
    """
    Função responsável pelo cálculo da distância de Hamming.
    :param seq_1: Sequência 1.
    :param seq_2: Sequência 2.
    :return: Valor da distância de Hamming.
    """
    # --- Distância total --- #
    distancia = 0

    # --- Comparar cada aminoácido entre as duas sequências --- #
    for aa_1, aa_2 in zip(seq_1, seq_2):
        if aa_1 != aa_2:
            distancia += 1

    return distancia
