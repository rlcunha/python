from os import X_OK, replace
from time import sleep
import numpy as np
from mibicrhome import ChromeAuto


class CargaRestaurates:

    def __init__(self):
        global df


if __name__ == '__main__':
    try:
        delays = [2, 4, 6, 7, 3]
        delay = np.random.choice(delays)

        chrome = ChromeAuto('bragança paulista', 'Centro')
        chrome.acessa('https://www.ifood.com.br/restaurantes/')

        chrome.digita_endereco()
        sleep(delay)
        chrome.seleciona_endereco()
        sleep(delay)
        chrome.confirma_endereco()
        sleep(delay)
        chrome.salva_endereco()
        sleep(delay)
        chrome.ver_mais()
        sleep(delay)
        chrome.carrega_restaurante()
        sleep(delay)
        fileNameCloud = chrome.gravar()
        sleep(delay)
        chrome.gravar_dados_cloud(fileNameCloud)
        chrome.sair()

    except Exception as e:
        print('Erro carregar restaurantes:', e)
