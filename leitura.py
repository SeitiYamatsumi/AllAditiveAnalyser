import csv
import numpy as np


def leitura_amostras():
    with open("amostras.csv", 'r', encoding='utf-8', newline='') as amostras_csv:
        amostras = csv.DictReader(amostras_csv, delimiter=',')
        data_csv = [linha for linha in amostras]

    return data_csv

def leitura_pesos():
    # Leitura dos limiares de ativação da primeira camada
    with open("b1.csv", 'r', encoding='utf-8', newline='') as b1_csv:
        leitura = csv.reader(b1_csv)
        b1 = np.zeros(15)
        for k, linha in enumerate(leitura):
            b1[k] = float(linha[0])

    # Leitura dos pesos da primeira camada
    with open("W1.csv", 'r', encoding='utf-8', newline='') as W1_csv:
        leitura = csv.reader(W1_csv)
        W1 = np.zeros((15, 4))
        for i, linha in enumerate(leitura):
            for j in range(len(linha)):
                W1[i][j] = float(linha[j])

    # Leitura dos limiares de ativação da segunda camada
    with open("b2.csv", 'r', encoding='utf-8', newline='') as b2_csv:
        leitura = csv.reader(b2_csv)
        b2 = np.zeros(3)
        for k, linha in enumerate(leitura):
            b2[k] = float(linha[0])

    # Leitura dos pesos da segunda camada
    with open("W2.csv", 'r', encoding='utf-8', newline='') as W2_csv:
        leitura = csv.reader(W2_csv)
        W2 = np.zeros((3, 15))
        for i, linha in enumerate(leitura):
            for j in range(len(linha)):
                W2[i][j] = float(linha[j])

    return b1, W1, b2, W2


def salvar_amostra(nova_amostra):
    with open("amostras.csv", 'a', encoding='utf-8', newline='\r') as amostras_csv:
        escrever = csv.writer(amostras_csv, delimiter=',')
        escrever.writerow(nova_amostra)
