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

# Loop principal do jogo
rodando = True
while rodando:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # Salvando as marcações antes de fechar
            salvar_marcacoes(marcacoes)
            rodando = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                # Abrindo caixa de diálogo para obter o nome da estrela
                root = Tk()
                root.withdraw()
                nome_estrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
                root.destroy()

                # Obtendo a posição do clique do mouse
                posicao = pygame.mouse.get_pos()

                # Salvando a primeira marcação ou criando a linha entre as marcações
                if primeira_marcacao is None:
                    primeira_marcacao = (posicao, nome_estrela)
                else:
                    segunda_marcacao = (posicao, nome_estrela)
                    marcacoes[primeira_marcacao[1]] = primeira_marcacao[0]
                    marcacoes[segunda_marcacao[1]] = segunda_marcacao[0]
                    distancia = calcular_distancia(primeira_marcacao[0], segunda_marcacao[0])
                    marcacoes["linha"] = {"coordenadas": (primeira_marcacao[0], segunda_marcacao[0]),
                                          "distancia": distancia}
                    primeira_marcacao = None
                    # Desenhar as marcações na tela
    tela.fill((0, 0, 0))  # Preenchendo a tela com preto
    # Desenhar a imagem de fundo
    tela.blit(fundo, (0, 0))

    for estrela, posicao in marcacoes.items():
        if estrela != "linha":
            pygame.draw.circle(tela, (255, 255, 255), posicao, 5)  # Desenhar círculo branco
            texto = estrela
            fonte = pygame.font.Font(None, 20)
            texto_renderizado = fonte.render(texto, True, (255, 255, 255))
            tela.blit(texto_renderizado, (posicao[0] + 10, posicao[1] - 10))

    # Desenhar a linha entre as marcações
    if "linha" in marcacoes:
        coordenadas = marcacoes["linha"]["coordenadas"]
        distancia = marcacoes["linha"]["distancia"]
        pygame.draw.line(tela, (255, 255, 255), coordenadas[0], coordenadas[1])
        texto = "Distância: {:.2f}".format(distancia)
        fonte = pygame.font.Font(None, 20)
        texto_renderizado = fonte.render(texto, True, (255, 255, 255))
        tela.blit(texto_renderizado, (10, 10))

    pygame.display.update()

# Encerrando o Pygame
pygame.quit()