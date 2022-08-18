from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date
from os import X_OK, replace
from time import sleep, strftime
import time
from bs4 import BeautifulSoup
import pandas as pd
from azure.storage.blob import ContainerClient

from decimal import Decimal

class ChromeAuto:
   
    def __init__(self, cidade, bairro):

        global df

        self.cidade = cidade
        self.bairro = bairro
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("start-maximized")
        # self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)        
        # self.options.add_argument('--headless')
        # self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options)
        # self.chrome.execute_script("window.location.reload()") 

    def digita_endereco(self):
        print('digita_endereco')
        try:
            self.chrome.refresh()

            btn_localiza = self.chrome.find_element(By.CLASS_NAME, 'address-search-input__button')
            btn_localiza.send_keys(f'  {self.cidade},{self.bairro}')              

        except Exception as e:
            print('Erro ao clicar em Localizacao:', e)
 
    def seleciona_endereco(self):
        print('seleciona_endereco')
        try:    
            btn_endereco = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/button')
            btn_endereco.click()  

        except Exception as e:
            print('Erro ao endereco:', e)            

    def confirma_endereco(self):
        print('confirma_endereco')
        try:
            btn_confirma = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[3]/div[2]/button/span')
            btn_confirma.click()

        except Exception as e:
            print('Erro ao confirma_endereco:', e)   

    def salva_endereco(self):
        print('salva_endereco')
        try:
            btn_confirma = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[4]/button/span')
            btn_confirma.click()

        except Exception as e:
            print('Erro ao salva_endereco:', e)  

    def acessa(self, site):
        try:
            print('acessa')
            self.chrome.get(site)
 
        except Exception as e:
            print('Erro acessa site:', e) 


    def sair(self):
        try:
            print('sair')

            self.chrome.quit()
        except Exception as e:
            print('Erro sair do site:', e) 

    def listar(self):
        try:
            print('listar')
            print(self.df.groupby(['frete', 'titulo']).head(50))

        except Exception as e:
            print('Erro listar restaurantes:', e)         

    def gravar(self):
        try:
            print('gravar')
            t = time.strftime(r"%Y%m%d%H%M", time.localtime())
            self.df.to_json(f'ifood-{t}-{self.cidade.replace(" ", "")}-{self.bairro.replace(" ", "")}.json', orient='records')

        except Exception as e:
            print('Erro gravar dataframe:', e) 

    def gravar_dados_cloud(self):
        try:
            print('gravar_dados_cloud')
            CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=sagestaoloja;AccountKey=3S3nL4/twTrFrwDIK+6PssQepK/1Ra0/7KmPdXNgsMGP6y2KjAxwijBRePXzrEJUROD/QuEpnIYnN5ZAR5JBjA==;EndpointSuffix=core.windows.net"
            CONTAINER_NAME = "landing"
            input_file_path = "lista_restaurante_ifood.json"
            output_blob_name = "lista_restaurante_ifood.json"

            container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

            # Upload file
            with open(input_file_path, "rb") as data:
                container_client.upload_blob(name=output_blob_name, data=data)

        except Exception as e:
            print('Erro gravar blob restaurantes:', e) 

    def excluir_dados_cloud(self):
        try:
            CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=sagestaoloja;AccountKey=3S3nL4/twTrFrwDIK+6PssQepK/1Ra0/7KmPdXNgsMGP6y2KjAxwijBRePXzrEJUROD/QuEpnIYnN5ZAR5JBjA==;EndpointSuffix=core.windows.net"
            CONTAINER_NAME = "landing"
            blob_name = "output_blob.csv"

            container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

            # Delete blob
            container_client.delete_blob(blob=blob_name)
       
        except Exception as e:
            print('Erro ao excluir_dados_cloud :', e)

    def ver_mais(self):
        print('ver_mais')
        try:
            btn_ver_mais = self.chrome.find_element(By.CLASS_NAME, 'cardstack-nextcontent')
            btn_ver_mais.click()

        except Exception as e:
            print('AVISO: Encontrou somente uma pagina:')
            return None

    def carrega_restaurante(self):
        print('carrega_restaurante')
        try:
            conteudo = self.chrome.find_element(By.CLASS_NAME, 'merchant-list-v2__wrapper').get_attribute('outerHTML')

            soup = BeautifulSoup(conteudo, 'html.parser')

            header = str(50)
            footer = str(50)
            info = str(50)
            context = str(50)            

            self.df = pd.DataFrame(columns=['titulo', 'frete', 'entregaDe', 'entregaAte', 'data', 'cliente','pontos','tipo','distancia','cidade','bairro','entreDe','entreAte'])

            for foo in soup.find_all('div', attrs={'class': 'merchant-list-v2__wrapper'}):
                foo_descendants = foo.descendants
                for d in foo_descendants:
                    if d.name == 'div':
                        if d.get('class', '') == ['merchant-v2__context']:
                            context = d.text
                        if d.get('class', '') == ['merchant-v2__info']:
                            info = d.text
                        if d.get('class', '') == ['merchant-v2__header']:
                            header = d.text.replace("'","")
                        if d.get('class', '') == ['merchant-v2__footer']:
                            footer = d.text.replace("´","").replace("`","").replace("'","").replace("á","a").replace(",",".").replace(r"\xa"," ")
                            self.df = self.df.append({'titulo': header, 
                            'frete': ChromeAuto.extrair_footer(footer,'frete'), 
                            'entregaDe': ChromeAuto.extrair_footer(footer,'entregaDe'),
                            'entregaAte':  ChromeAuto.extrair_footer(footer,'entregaAte'), 
                            'entreDe': ChromeAuto.extrair_footer(footer,'entreDe'), 
                            'entreAte': ChromeAuto.extrair_footer(footer,'entreAte'),  
                            'situacao': ChromeAuto.extrair_footer(footer,'situacao'),                                                      
                            'pontos':  ChromeAuto.extrair_info(info,'pontos'), 
                            'tipo':  ChromeAuto.extrair_info(info,'tipo'), 
                            'distancia':  ChromeAuto.extrair_info(info,'distancia'), 
                            'cidade': self.cidade,
                            'bairro': self.bairro,                                                            
                            'data': time.strftime(r"%Y%m%d%H%M", time.localtime()), 
                            'cliente': 'Mibitech'}, ignore_index=True)

        except Exception as e:
            print('Erro carregar restaurantes:', e)

    def extrair_footer(dados,tipo):
        ret = ""
        try:
            if tipo == 'frete':
                ret = Decimal(dados.replace("Gratis", "R$ 0.00")[-5:]) 
           
            if tipo == 'entregaDe':
                if 'Hoje' not in dados and 'Fechado' not in dados:
                    ret = pd.to_numeric(dados.split(sep=" ")[0].split(sep="-")[0])                   

            if tipo == 'entregaAte':
                if 'Hoje' not in dados and 'Fechado' not in dados:
                    ret = pd.to_numeric(dados.split(sep=" ")[0].split(sep="-")[1])  

            if tipo == 'entreDe':
                if 'Hoje' in dados:
                    ret = pd.to_numeric(dados.replace("h","").split(sep=" ")[0].split(sep="-")[0])   

            if tipo == 'entreAte':
                if 'Hoje' in dados:
                    ret = pd.to_numeric(dados.replace("h","").split(sep=" ")[0].split(sep="-")[1])   

            if tipo == 'situacao':
                if 'Fechado' in dados:
                    ret = 'fechado' 
                if 'Hoje' in dados:                     
                    ret = 'temporario'
                if 'Hoje' not in dados and 'Fechado' not in dados:
                    ret = 'aberto'

            return ret

        except Exception as e:
            print(f'Erro ao extrair_footer :{dados}-{tipo}', e)
    
    def extrair_info(dados,tipo):
        ret = ""
        try:
            if tipo == 'pontos':
                if 'Novo' in dados:
                    ret = 5.1 
                else:   
                    ret = pd.to_numeric(dados.split(sep=" ")[0])
            if tipo == 'tipo':
                ret = dados.split(sep=" ")[2]                
            if tipo == 'distancia':
                ret = dados.split(sep=" ")[4]               

            return ret

        except Exception as e:
            print(f'Erro ao extrair_info :{dados}-{tipo}', e)




 