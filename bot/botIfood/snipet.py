       # def verifica_usuario(self, usuario):
    #     profile_link = self.chrome.find_element(By.NAME, 'user-profile-link')
    #     profile_link_html = profile_link.get_attribute('innerHTML')
    #     assert usuario in profile_link_html

    # def faz_login(self):
    #     try:
    #         input_login = self.chrome.find_element(By.ID, 'login_field')
    #         input_password = self.chrome.find_element(By.ID, 'password')
    #         btn_login = self.chrome.find_element(By.ID, 'commit')
    #
    #         input_login.send_keys('rlcunha')
    #         input_password.send_keys('cesabe01@@')
    #         sleep(3)
    #         btn_login.click()
    #
    #     except Exception as e:
    #         print('Erro ao fazer login:', e)
    # Def scroll_browser(self, browser, num):
    #     '''Improve browser scrolling to ensure that js is fully executed '''
    #     For i in range(1, num+1):
    #         Browser.execute_script(
    #             "window.scrollTo(0, document.body.scrollHeight/%d*%d);"% (
    #                 Num, i)
    #         )
    #         Time.sleep(0.5)



    # class ChromeAuto:

#     def __init__(self):
#         global df
#         self.driver_path = 'chromedriver'
#         self.options = webdriver.ChromeOptions()
#         self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
#         self.options.add_argument("start-maximized")
#         # self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         self.options.add_experimental_option('useAutomationExtension', False)        

#         #self.options.add_argument('--headless')
#         # self.options.add_argument('user-data-dir=Perfil')
#         self.chrome = webdriver.Chrome(
#             self.driver_path,
#             options=self.options

#         # self.chrome.execute_script("window.location.reload()") 

#         )

#     def digita_endereco(self):
#         print('digita_endereco')
#         try:
#             self.chrome.refresh()

#             btn_localiza = self.chrome.find_element(By.CLASS_NAME, 'address-search-input__button')
#             btn_localiza.send_keys(f' Bragança Paulista,centro')              

#         except Exception as e:
#             print('Erro ao clicar em Localizacao:', e)
#             return None 

#     def seleciona_endereco(self):
#         print('seleciona_endereco')
#         try:    
#             btn_endereco = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/button')
#             btn_endereco.click()  

#         except Exception as e:
#             print('Erro ao endereco:', e)            

#     def confirma_endereco(self):
#         print('confirma_endereco')
#         try:
#             btn_confirma = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[3]/div[2]/button/span')
#             btn_confirma.click()

#         except Exception as e:
#             print('Erro ao confirma_endereco:', e)   

#     def salva_endereco(self):
#         print('salva_endereco')
#         try:
#             btn_confirma = self.chrome.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[4]/button/span')
#             btn_confirma.click()

#         except Exception as e:
#             print('Erro ao salva_endereco:', e)  

#     def acessa(self, site):
#         try:
#             print('acessa')
#             self.chrome.get(site)
#         except Exception as e:
#             print('Erro acessa site:', e) 
#             return None  

#     def sair(self):
#         try:
#             print('sair')
#             self.chrome.quit()
#         except Exception as e:
#             print('Erro sair do site:', e) 
#             return None  

#     def listar(self):
#         try:
#             print('listar')
#             print(df.groupby(['frete', 'titulo']).head(50))

#         except Exception as e:
#             print('Erro listar restaurantes:', e)         
#             return None  

#     def gravar(self):
#         try:
#             print('gravar')
#             # js = json.dumps(df)
#             # fp = open('example.json', 'w')
#             # fp.write()
#             # fp.close()
#             df.to_json('lista_restaurante_ifood.json', orient='records')

#         except Exception as e:
#             print('Erro gravar dataframe:', e) 
#             return None  

#     def gravar_dados_cloud(self):
#         try:
#             print('gravar_dados_cloud')
#             CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=sagestaoloja;AccountKey=3S3nL4/twTrFrwDIK+6PssQepK/1Ra0/7KmPdXNgsMGP6y2KjAxwijBRePXzrEJUROD/QuEpnIYnN5ZAR5JBjA==;EndpointSuffix=core.windows.net"
#             CONTAINER_NAME = "landing"
#             input_file_path = "lista_restaurante_ifood.json"
#             output_blob_name = "lista_restaurante_ifood.json"

#             container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

#             # Upload file
#             with open(input_file_path, "rb") as data:
#                 container_client.upload_blob(name=output_blob_name, data=data)

#         except Exception as e:
#             print('Erro gravar blob restaurantes:', e) 
#             return None  

#     def excluir_dados_cloud(self):
#         try:
#             CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=sagestaoloja;AccountKey=3S3nL4/twTrFrwDIK+6PssQepK/1Ra0/7KmPdXNgsMGP6y2KjAxwijBRePXzrEJUROD/QuEpnIYnN5ZAR5JBjA==;EndpointSuffix=core.windows.net"
#             CONTAINER_NAME = "landing"
#             blob_name = "output_blob.csv"

#             container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

#             # Delete blob
#             container_client.delete_blob(blob=blob_name)
       
#         except Exception as e:
#             print('Erro ao excluir_dados_cloud :', e)
#             return None

#     def ver_mais(self):
#         print('ver_mais')
#         try:
#             btn_ver_mais = self.chrome.find_element(By.CLASS_NAME, 'cardstack-nextcontent')
#             btn_ver_mais.click()

#         except Exception as e:
#             print('Erro ao clicar no ver mais:', e)
#             return None

#     def carrega_restaurante(self):
#         print('carrega_restaurante')
#         try:
#             conteudo = self.chrome.find_element(By.CLASS_NAME, 'merchant-list-v2__wrapper').get_attribute('outerHTML')

#             soup = BeautifulSoup(conteudo, 'html.parser')

#             titulo = str(50)
#             rodape = str(50)
#             info = str(50)
#             context = str(50)            

#             df = pd.DataFrame(columns=['titulo', 'frete', 'entregaDe', 'entregaAte', 'data', 'cliente','aberto','pontos','tipo','distancia','abertura','fechamento'])

#             for foo in soup.find_all('div', attrs={'class': 'merchant-list-v2__wrapper'}):
#                 foo_descendants = foo.descendants
#                 for d in foo_descendants:
#                     if d.name == 'div':
#                         if d.get('class', '') == ['merchant-v2__context']:
#                             context = d.text
#                         if d.get('class', '') == ['merchant-v2__info']:
#                             info = d.text
#                         if d.get('class', '') == ['merchant-v2__header']:
#                             titulo = d.text.replace("'","")
#                         if d.get('class', '') == ['merchant-v2__footer']:
#                             rodape = d.text.replace("´","").replace("`","").replace("'","").replace("á","a").replace(",",".")
#                             print(info) 

#                             df = df.append({'titulo': titulo, 
#                             'frete': ChromeAuto.extrair_subtitulo(rodape,'frete'), 
#                             'entregaDe': ChromeAuto.extrair_subtitulo(rodape,'entregaDe'),
#                             'entregaAte':  ChromeAuto.extrair_subtitulo(rodape,'entregaAte'), 
#                             'pontos':  ChromeAuto.extrair_subtitulo(info,'pontos'), 
#                             'tipo':  ChromeAuto.extrair_subtitulo(info,'tipo'), 
#                             'distancia':  ChromeAuto.extrair_subtitulo(info,'distancia'), 
#                             'aberto':  "" , 
#                             'data': datetime.datetime.utcnow(), 
#                             'cliente': 'Inverno Ditalia'}, ignore_index=True)
#             return df

#         except Exception as e:
#             print('Erro carregar restaurantes:', e)
#             return None

#     def extrair_subtitulo(dados,tipo):
#         ret = ""
#         try:
#             if tipo == 'frete':
#                 if dados.find("Gratis"):
#                     ret = Decimal(dados.replace("Gratis", "R$ 0.00")[-5:]) 
#             if tipo == 'entregaDe':
#                 ret = pd.to_numeric(dados[:2])
#             if tipo == 'entregaAte':
#                 ret = pd.to_numeric(dados[3:5])
#             if tipo == 'pontos':
#                 ret = dados[:3]
#             if tipo == 'tipo':
#                 ret = dados[6:-9]                
#             if tipo == 'distancia':
#                 ret = dados[-6:]               

#             return ret

#         except Exception as e:
#             print('Erro ao extrair_subtitulo:', e)
#             return None

#         # def verifica_usuario(self, usuario):
#     #     profile_link = self.chrome.find_element(By.NAME, 'user-profile-link')
#     #     profile_link_html = profile_link.get_attribute('innerHTML')
#     #     assert usuario in profile_link_html

#     # def faz_login(self):
#     #     try:
#     #         input_login = self.chrome.find_element(By.ID, 'login_field')
#     #         input_password = self.chrome.find_element(By.ID, 'password')
#     #         btn_login = self.chrome.find_element(By.ID, 'commit')
#     #
#     #         input_login.send_keys('rlcunha')
#     #         input_password.send_keys('cesabe01@@')
#     #         sleep(3)
#     #         btn_login.click()
#     #
#     #     except Exception as e:
#     #         print('Erro ao fazer login:', e)
#     # Def scroll_browser(self, browser, num):
#     #     '''Improve browser scrolling to ensure that js is fully executed '''
#     #     For i in range(1, num+1):
#     #         Browser.execute_script(
#     #             "window.scrollTo(0, document.body.scrollHeight/%d*%d);"% (
#     #                 Num, i)
#     #         )
#     #         Time.sleep(0.5)

    # chrome.grava_resultado_json()
    # sleep(delay)

    # chrome.clica_sign_in()
    # chrome.faz_login()
    #
    # chrome.clica_perfil()
    # chrome.verifica_usuario('otaviomirandabr')

        # def gravar(self):
        # try:
        #     print('gravar')
        #     # js = json.dumps(df)
        #     # fp = open('example.json', 'w')
        #     # fp.write()
        #     # fp.close()
        #     # t = datetime.utcnow
        #     # t.strftime('%Y%m%d%H%M')
        #     t = time.strftime(r"%Y%m%d%H%M", time.localtime())
        #     self.df.to_json(f'ifood-{t}-{self.cidade.replace(" ", "")}-{self.bairro.replace(" ", "")}.json', orient='records')