D = int(input('Qual a distância de robô até o começo da quadra? '))

if D <= 800:
    print('------------------------------------------')
    print('A pontuação do lançamento foi de 1 ponto!')
    print('------------------------------------------')

elif D <= 1400:
    print('------------------------------------------')
    print('A pontuação do lançamento foi de 2 pontos!')
    print('------------------------------------------')

else:
    print('------------------------------------------')
    print('A pontuação do lançamento foi de 3 pontos!')
    print('------------------------------------------')
