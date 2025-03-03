# O programa deve gerar um número aleatório entre 1 e 15
# e pedir para o usuário adivinhar o número gerado.

# Se a tentativa do usuário não for correta, o programa
# deve informar se ele tentou um valor baixo ou alto,
# comparando com o valor gerado.

# Se o usuário acertar, exibir a mensagem 'Parabéns! Você acertou.'.

# O programa deve permitir até três tentativas por jogo.

# Obs.: A tecla 's' permite iniciar um novo jogo.

import random
import os

novo_jogo = 's'

while novo_jogo == 's':
    print(f'Bem-vindo ao jogo de adivinhação!')
    print(f'Você terá três chances para adivinhar um número entre 1 e 15')
     
    # Gerar número aleatório secreto:
    num = random.randint(1,15)
   
    #Jogar:
    for i in range(3):
        print(f'\nQual o número escolhido:')
        chute = (int(input()))
        
        if chute == num:
            print(f'\nParabéns! Você acertou.')
            break
        elif chute > num:
            print(f'\nNúmero alto!')
        else:
            print(f'\nNúmero baixo!')

# Caso não tenha acertado revelar o número secreto

    if chute != num:
        print(f'O número secreto é {num}\n')
        print(f'Jogo finalizado\n')

    novo_jogo = input(f'Deseja jogar outra vez? "S" para "Sim", outra tecla qualquer para "Não": ')
    novo_jogo = novo_jogo.lower() # 'Lower' = Metodo especifico de Strings: Coloca todos os caracteres em Caixa Baixa.

# Limpar a tela (Windows):

    os.system('cls')

# # Limpar a tela (MAC OS ou Linux):

#     os.system('clear')
