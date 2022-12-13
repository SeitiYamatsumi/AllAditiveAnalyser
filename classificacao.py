import csv
import numpy as np
from leitura import leitura_pesos
from leitura import salvar_amostra


def classificação(dados, nova_amostra):
    def logistica(x):
        y = 1 / (1 + np.exp(-x))
        return y

        # Leitura dos Pesos e Limiares de Ativação

    b1, W1, b2, W2 = leitura_pesos()

    # Matrizes Auxiliares
    u1 = np.zeros(15)
    y1 = np.zeros(15)
    u2 = np.zeros(3)
    y2 = np.zeros(3)

    # Normalização dos dados de entrada
    dados_n = np.zeros(4)
    dados_n[0] = (dados[0] - 100.0) / (300.0 - 100.0)
    dados_n[1] = (dados[1] - 1.0) / (14.0 - 1.0)
    dados_n[2] = (dados[2] - 1.0) / (6.0 - 1.0)
    dados_n[3] = (dados[3] - 0.5) / (1 - 0.5)

    # Primeira Camada
    for i in range(15):
        for j in range(4):
            u1[i] = u1[i] + (W1[i][j] * dados_n[j])
        u1[i] = u1[i] + b1[i]
        y1[i] = logistica(u1[i])

    # Segunda Camada    
    for i in range(3):
        for j in range(15):
            u2[i] = u2[i] + (W2[i][j] * y1[j])
        u2[i] = u2[i] + b2[i]
        y2[i] = u2[i]

    # Pós-Processamento
    for k in range(len(y2)):
        if y2[k] >= 0.5:
            y2[k] = 1
        else:
            y2[k] = 0

    # Definir qual o Aditivo Utilizado
    Aditivo = ['Octanagem', 'Oxigenadores', 'Detergente']
    for k in range(len(y2)):
        if y2[k] == 1:
            saida = Aditivo[k]

    # Salvar a nova amostra
    nova_amostra.append(saida)
    salvar_amostra(nova_amostra)

    return saida
