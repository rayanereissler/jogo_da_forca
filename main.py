import pygame as pg
import random

import pygame.mouse

#cores do jogo
rosa = (216,191,216)
preto = (0,0,0)

#setup da tela do jogo
window=pg.display.set_mode((1000,600))

#iniciando fonte do jogo
pg.font.init()

#escolhendo uma fonte e tamanho
font=pg.font.SysFont('Courier New', 50) #fonte da palavra chave
font_rb=pg.font.SysFont('Courier New', 30) #fonte do botão 'restart'

palavras = ['GARRAFA', 'COMPUTADOR', 'BEIJA FLOR', 'XICARA']
tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance=0 #começo do jogo, sem o boneco desenhado
letra='' #letra que vamos pressionar no teclado
click_last_status=False  #variável para poder clicar no botão restart

#agora iniciando o looping do jogo:
#função para desenhar a forca:

def desenho_da_forca(window, chance):
    pg.draw.rect(window, rosa, (0,0,1000,600))
    #acima criamos a tela do jogo na cor rosa com largura 1000px e altura de 600px
    pg.draw.line(window, preto, (100,500), (100,100), 10)
    #acima desenhamos o poste da forca
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    #aqui acabamos de desenhar a forca e seguimos para o boneco
    #agora criamos uma estrutura de condição para que a cada erro seja desenhado uma parte do boneco

    if chance >=1:
        pg.draw.circle(window, preto, (300,200), 50,10) #desenho da cabeça
    if chance >= 2: #desenho do tronco
        pg.draw.line(window, preto,(300,250), (300,350), 10)
    if chance >=3: #desenho do braço direito
        pg.draw.line(window, preto, (300,260), (255,350), 10)
    if chance >=4:#desenho do braço esquerdo
        pg.draw.line(window, preto, (300,260), (375,350),10)
    if chance >=5: #desenho da perna direita
        pg.draw.line(window, preto, (300,350), (375,450),10)
    if chance >=6: #desenho da perna esquerda
        pg.draw.line(window,preto, (300,350), (225,450),10)

#criando uma função para desenhar o botão de restart:
def desenho_restart_button(window):
    pg.draw.rect(window, preto, (700,100,200,65))
    texto=font_rb.render('Reiniciar', True, rosa,) #criando o botão reiniciar
    window.blit(texto, (720,120)) #posicionamento do texto

#criando uma função para sortear a palavra:
def sorteando_palavra(palavras, palavra_escolhida, end_game):
    if end_game== True:
        palavra_n=random.randint(0, len(palavras) -1)
        palavra_escolhida=palavras[palavra_n]
        end_game=False
    return palavra_escolhida, end_game

#agora criamos uma função para camuflar a palavra escolhida e colocar ela dentro do jogo
def camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada=palavra_escolhida
    for n in range (len(palavra_camuflada)):
        if palavra_camuflada[n:n+1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n],'#')
    return palavra_camuflada

#criando uma função para as tentativas de letras:
def tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras: #se a letra não estiver dentro do array, entao ele vai colocar essa letra dentro da nossa array
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida: #se a letra não estiver na palavra escolhida, aumenta em 1 a chance de tentativas
            chance+=1
    elif letra in tentativas_de_letras: #se a letra estiver na palavra escolhida, ele da um passo sem fazer nada
        pass
    return tentativas_de_letras, chance

#criando uma função para mostrar a palavra do jogo:
def palavra_do_jogo(window, palavra_camuflada):
    palavra=font.render(palavra_camuflada, True, preto)
    window.blit(palavra, (200,500))

#criando uma função para ativar o restart do jogo:
def restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras,click_last_status,click, x, y):
    count=0
    limite=len(palavra_escolhida)

    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] !=  '#':
            count+=1
    if count == limite and click_last_status == False and click[0] == True:
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas_de_letras = ['', '-']
            end_game = True
            chance=0
            letra =' '
    return end_game, chance, tentativas_de_letras, letra


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type==pg.KEYDOWN: #para que todas as letras digitadas fiquem maiusculas
            letra=str(pg.key.name(event.key)).upper()
            print(letra)

    #declarando uma variavel para a posição do mouse dentro da nossa tela:
    mouse=pygame.mouse.get_pos()
    mouse_posicao_x=mouse[0]
    mouse_posicao_y=mouse[1]

    #declarando uma variavel para o click do mouse:
    click=pg.mouse.get_pressed()

    #chamando funções para iniciar o jogo:
    desenho_da_forca(window, chance)
    desenho_restart_button(window)
    palavra_escolhida, end_game=sorteando_palavra(palavras, palavra_escolhida, end_game)
    palavra_camuflada=camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance=tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    palavra_do_jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_posicao_x, mouse_posicao_y)


    #criando uma variavel para click_last_status:
    if click[0]==True:
        click_last_status=True
    else:
        click_last_status=False


    pg.display.update()






