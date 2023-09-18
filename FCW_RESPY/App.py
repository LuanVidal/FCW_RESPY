import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import wifi
import requests

# Listar todas as redes Wi-Fi disponíveis
redes_disponiveis = wifi.Cell.all('wlan0')

# Nome da rede Wi-Fi à qual deseja se conectar
nome_da_rede = 'EGR-FIBRA_2.4G-ROSEMEIRE'
senha_da_rede = '11151821'

# Verificar se a rede está disponível na lista de redes disponíveis
rede_encontrada = None
for rede in redes_disponiveis:
    if rede.ssid == nome_da_rede:
        rede_encontrada = rede
        break

# Se a rede foi encontrada, conectar a ela
if rede_encontrada:
    print(f"Conectando à rede {nome_da_rede}...")
    scheme = wifi.Scheme.find('wlan0', nome_da_rede)
    if scheme is None:
        scheme = wifi.Scheme.for_cell('wlan0', nome_da_rede, rede_encontrada, senha_da_rede)
        scheme.save()
    
    scheme.activate()
    print(f"Conectado à rede {nome_da_rede}.")
else:
    print(f"A rede {nome_da_rede} não foi encontrada.")

# Agora, a Raspberry Pi deve estar conectada à rede especificada.

App = tk.Tk()
App.title("TCS - FCW")
App.geometry("800x480")

def carregar_tela(caminho_da_imagem):
    imagem = Image.open(caminho_da_imagem)
    imagem = ImageTk.PhotoImage(imagem)
    return imagem

# Caminhos das imagens para cada tela
caminho_tela_TCS = "./telas/00.bmp"
caminho_tela_matricula = "./telas/01.bmp"
caminho_tela_erro_matricula = "./telas/02.bmp"
caminho_tela_OrdProducao = "./telas/03.bmp"
caminho_tela_erro_OrdProducao = "./telas/04.bmp"
caminho_tela_ID = "./telas/05.bmp"
caminho_tela_erro_ID = "./telas/06.bmp"
caminho_tela_consumivel = "./telas/07.bmp"
caminho_tela_erro_consumivel = "./telas/08.bmp"
caminho_tela_aguarde = "./telas/09.bmp"
caminho_tela_rastreabilidade1 = "./telas/10.bmp"
caminho_tela_rastreabilidade2 = "./telas/11.bmp"
caminho_tela_rastreabilidade3 = "./telas/12.bmp"
caminho_tela_finaliza_processo = "./telas/13.bmp"
caminho_tela_processo_finalizado = "./telas/14.bmp"
caminho_tela_erro_timeout = "./telas/15.bmp"

# Carregar cada tela usando a função
tela_TCS = carregar_tela(caminho_tela_TCS)
tela_matricula = carregar_tela(caminho_tela_matricula)
tela_erro_matricula = carregar_tela(caminho_tela_erro_matricula)
tela_OrdProducao = carregar_tela(caminho_tela_OrdProducao)
tela_erro_OrdProducao = carregar_tela(caminho_tela_erro_OrdProducao)
tela_ID = carregar_tela(caminho_tela_ID)
tela_erro_ID = carregar_tela(caminho_tela_erro_ID)
tela_consumivel = carregar_tela(caminho_tela_consumivel)
tela_erro_consumivel = carregar_tela(caminho_tela_erro_consumivel)
tela_aguarde = carregar_tela(caminho_tela_aguarde)
tela_rastreabilidade1 = carregar_tela(caminho_tela_rastreabilidade1)
tela_rastreabilidade2 = carregar_tela(caminho_tela_rastreabilidade2)
tela_rastreabilidade3 = carregar_tela(caminho_tela_rastreabilidade3)
tela_finaliza_processo = carregar_tela(caminho_tela_finaliza_processo)
tela_processo_finalizado = carregar_tela(caminho_tela_processo_finalizado)
tela_erro_timeout = carregar_tela(caminho_tela_erro_timeout)


App.mainloop()