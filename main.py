import os
import pandas as pd
import urllib




# Definindo as variáveis globais
ENDERECO_DOWNLOAD_LINK = "https://drive.google.com/u/0/uc?id=1L3r_eg4lUs-gkpfNPx3Fr-L4d2OY4DXa&export=download"
ENDERECO_FILE_NAME = "DadosEmpresa.csv"
ENDERECO_DATA_PATH = "data_raw/"

EMPRESA_DOWNLOAD_LINK = "https://drive.google.com/u/0/uc?id=18yeabRYTZXgknmsrtRAMWceed9UaAQ_Q&export=download/"
EMPRESA_FILE_NAME = "DadosEndereco.csv"
EMPRESA_DATA_PATH = "data_raw"



# Definindo a função de download, verifica se o arquivo FILE_NAME existe no DATA_PATH, se não, o baixa

class DesafioDriva(pd.DataFrame):
    def PrintarColunas(self):
        print("\nPrintando as colunas do data frame de Desafio Driva {}: \n")
        for col in self.columns:
            print(col)

    def PrimeirasLinhas(self):
        print("\n Printando as primeiras 5 linhas\n")
        print(self.head())

    def OptantesSimples(self):
        df = self[self['opcao_pelo_simples'] =='SIM']
        print("\n Total de clientes que optam pelo simples: {} \n".format(len(df.index)))

    def CapitalSocialTotal(self):
        total_capital = self['capital_social'].sum()
        print(total_capital)
    
    def CapitalSocialMedio(self):
        df = self[(self['capital_social'] > 10000) & (self['capital_social'] < 20000)]
        print(df)


def download_data(housing_url, data_path, file_name):
    file_path = os.path.join(data_path, file_name)
    if not os.path.isfile(file_path):
        os.makedirs(data_path)
        urllib.request.urlretrieve(housing_url, file_path)
        if os.path.isfile(file_path):
            return True
        else:
            # Download falhou
            raise Exception("Não foi possivel baixar o arquivo na URL solicitada, é possível fazê-lo manualmente?")
    else:
        # Não há necessidade de fazer download
        return False



download_data(ENDERECO_DOWNLOAD_LINK, ENDERECO_DATA_PATH, ENDERECO_FILE_NAME)

df_raw = pd.read_csv(os.path.join(EMPRESA_DOWNLOAD_LINK, ENDERECO_FILE_NAME))
df = DesafioDriva(df_raw)
df.PrintarColunas()
df.PrimeirasLinhas()
df.OptantesSimples()
df.CapitalSocialTotal()
df.CapitalSocialMedio()
