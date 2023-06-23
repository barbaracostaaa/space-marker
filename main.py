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