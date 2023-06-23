import pygame
from pygame.locals import *
from tkinter import Tk, simpledialog
import json

# Função para salvar os pontos marcados em um arquivo JSON
def salvar_marcacoes(marcacoes):
    with open('marcacoes.json', 'w') as file:
        json.dump(marcacoes, file)

# Função para carregar os pontos marcados de um arquivo JSON
def carregar_marcacoes():
    try:
        with open('marcacoes.json', 'r') as file:
            marcacoes = json.load(file)
    except FileNotFoundError:
        marcacoes = {}
    return marcacoes

# Função para excluir todas as marcações
def excluir_marcacoes():
    marcacoes = {}
    salvar_marcacoes(marcacoes)
    return marcacoes

# Função para calcular a distância entre duas coordenadas
def calcular_distancia(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
# Carregando a imagem de fundo
fundo = pygame.image.load("bg.jpg")


# Carregamento do ícone
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

# Título da janela
pygame.display.set_caption("SPACE MARKER")

# Carregamento do som de fundo
pygame.mixer.music.load("som_de_fundo.mp3")
pygame.mixer.music.play(-1)  # -1 para loop infinito

# Carregamento das marcações
marcacoes = carregar_marcacoes()

# Variável para armazenar a primeira marcação
primeira_marcacao = None