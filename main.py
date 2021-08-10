import os
import pandas as pd
from six.moves import urllib




# Definindo as variáveis globais
ENDERECO_DOWNLOAD_LINK = "https://drive.google.com/u/0/uc?id=1L3r_eg4lUs-gkpfNPx3Fr-L4d2OY4DXa&export=download"
ENDERECO_FILE_NAME = "DadosEndereco.csv"
ENDERECO_DATA_PATH = "data_raw/"

EMPRESA_DOWNLOAD_LINK = "https://drive.google.com/u/0/uc?id=18yeabRYTZXgknmsrtRAMWceed9UaAQ_Q&export=download/"
EMPRESA_FILE_NAME = "DadosEmpresa.csv"
EMPRESA_DATA_PATH = "data_raw"



# Defino aqui a classe para o desafio, cada metodo foi feito para uma etapa especifica, em termos de reaplicacao do codigo essa classe nao e muito viavel
# porem o objetivo aqui nao foi reaplicar o codigo e sim otimiza-lo o máximo possivel para o desafio e facilitar sua leitura

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

    def SaveCuritiba(self):
        df = self[self['municipio'] == 'CURITIBA']
        df.to_csv('curitiba_clients.csv')

    def NextStep(self):
        if os.path.isdir('data_merged/'):
            pass
        else:
            os.makedirs('data_merged/')
        self.to_csv('data_merged/DadosEmpresasEndereco.csv')



# Funcao de download, vai baixar o arquivo file_name pela ulr e coloca-lo no path
# Achei mais facil baixar o arquivo por codigo, assim fica mais simples de rodar o codigo sem precisar de setups de arquivo (e também não pesa o repo do git)
def download_data(download_url, data_path, file_name):
    file_path = os.path.join(data_path, file_name)
    if not os.path.isfile(file_path):
        #Caso não encontre o arquivo, ele irá ser baixado
        if os.path.exists(data_path):
            pass
        else:
            os.makedirs(data_path)
        urllib.request.urlretrieve(download_url, file_path)
        if os.path.isfile(file_path):
            return True
        else:
            # Download falhou
            raise Exception("Não foi possivel baixar o arquivo na URL solicitada, é possível fazê-lo manualmente?")
    else:
        # Não há necessidade de fazer download
        return False



download_data(ENDERECO_DOWNLOAD_LINK, ENDERECO_DATA_PATH, ENDERECO_FILE_NAME)
download_data(EMPRESA_DOWNLOAD_LINK, EMPRESA_DATA_PATH, EMPRESA_FILE_NAME)


df_raw = pd.read_csv(os.path.join(EMPRESA_DATA_PATH, EMPRESA_FILE_NAME))
df_extra = pd.read_csv(os.path.join(ENDERECO_DATA_PATH, ENDERECO_FILE_NAME))
df_merged = df_raw.merge(df_extra, on='cnpj', how='outer')

print(df_merged)

df = DesafioDriva(df_merged)
df.PrintarColunas()
df.PrimeirasLinhas()
df.OptantesSimples()
df.CapitalSocialTotal()
df.CapitalSocialMedio()
df.SaveCuritiba()
df.NextStep()
