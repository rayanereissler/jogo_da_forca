import random

palavra =['ensolarado', 'computador', 'sol']
letras_jogador=[]
chances=6
ganhou=False
palavra_escolhida = random.choice(palavra)

while True:

    for letras in palavra_escolhida:
        if letras in letras_jogador:
            print(letras, end=" ")
        else:
            print("-", end=" ")
    print()
    print(f"você ainda tem {chances} chances.")
    tentativa_usuario=input("Digite uma letra minúscula:")
    letras_jogador.append(tentativa_usuario)
    if tentativa_usuario not in palavra_escolhida:
        chances = chances-1

    ganhou=True
    for letras in palavra_escolhida:
        if letras not in letras_jogador:
            ganhou=False

    if chances==0 or ganhou:
        break
if ganhou:
    print(f"Parabéns, você ganhou! A palavra era {palavra_escolhida}")
else:
    print(f"Infelizmente você perdeu! A palavra era {palavra_escolhida}")

