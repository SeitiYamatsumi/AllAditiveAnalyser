
import numpy as np
import datetime
from leitura import leitura_amostras

def aquisicao_dados(x1,x2,x3,x4):
    # Aquisição de uma Nova Amostra
    dados = np.zeros(4)
    dados[0]=float(x1)
    dados[1]=float(x2)
    dados[2]=float(x3)
    dados[3]=float(x4)


    # Obter o Número da Amostra
    data_amostras = leitura_amostras()
    Nro_Amostra = len(data_amostras) + 1


    # Obter a Data
    Data = datetime.date.today().strftime("%d/%m/%y")

    # Nova amostra
    nova_amostra = [str(Nro_Amostra), str(dados[0]), str(dados[1]), str(dados[2]), str(dados[0]), Data]

    return dados, nova_amostra
