print('JOGO DA VELHA')
print('Para jogar o Jogo da velha, escolha X ou O ')
jogador1 = input('Digite sua escolha: ')
if jogador1 not in ['X', 'O']:
    print('Escolha inválida! Por favor, escolha X ou O.')
    exit()

jogador2 = 'O' if jogador1 == 'X' else 'X'
print(f'Jogador1 escolheu {jogador1}, então jogador2 é {jogador2}')

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

def checar_vencedor():
    linhas = [a, b, c]
    colunas = [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [a[2], b[2], c[2]]]
    diagonais = [[a[0], b[1], c[2]], [a[2], b[1], c[0]]]

    for linha in linhas:
        if linha[0] == linha[1] == linha[2]:
            return linha[0]
    for coluna in colunas:
        if coluna[0] == coluna[1] == coluna[2]:
            return coluna[0]
    for diagonal in diagonais:
        if diagonal[0] == diagonal[1] == diagonal[2]:
            return diagonal[0]
    return None

def atualizar_tabuleiro(posicao, jogador):
    if 1 <= posicao <= 3:
        if a[posicao - 1] not in ['X', 'O']:
            a[posicao - 1] = jogador
        else:
            print("Esta posição está ocupada, escolha outra posição.")
            return False
    elif 4 <= posicao <= 6:
        if b[posicao - 4] not in ['X', 'O']:
            b[posicao - 4] = jogador
        else:
            print("Esta posição está ocupada, escolha outra posição.")
            return False
    elif 7 <= posicao <= 9:
        if c[posicao - 7] not in ['X', 'O']:
            c[posicao - 7] = jogador
        else:
            print("Esta posição está ocupada, escolha outra posição.")
            return False
    else:
        print("Posição inválida, escolha uma posição de 1 a 9.")
        return False
    return True

for jogadas in range(9):
    if jogadas % 2 == 0:
        jogador_atual = jogador1
    else:
        jogador_atual = jogador2
    escolhaposicao = int(input(f'{jogador_atual}, escolha uma posição de 1 a 9: '))

    if atualizar_tabuleiro(escolhaposicao, jogador_atual):
        print(f"{a}\n{b}\n{c}")
        vencedor = checar_vencedor()
        if vencedor:
            print(f'{vencedor} venceu!')
            break
else:
    print('O jogo terminou em empate!')
