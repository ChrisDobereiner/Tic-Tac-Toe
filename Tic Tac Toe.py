#Jogo da Velha

tabuleiro = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ',' ']

tabuleiroAI = [4,4,4,
               4,4,4,
               4,4,4]


def imprimir():
    print (tabuleiro[0], '|',tabuleiro[1],'|',tabuleiro[2])
    print ('___________')
    print (tabuleiro[3], '|',tabuleiro[4],'|',tabuleiro[5])
    print ('___________')
    print (tabuleiro[6], '|',tabuleiro[7],'|',tabuleiro[8])
    print ('___________')

def turn():
    jogador = input('Selecione um lugar para jogar! ')
    jogador = int(jogador)
    if tabuleiro[jogador] != 'X' and tabuleiro[jogador] != 'O':
        tabuleiro[jogador] = 'X'
        tabuleiroAI[jogador] = 5
    else:
        print ('Ops! Este lugar ja foi selecionado!')

def AIturn():
    for i in range (0,9):
        somaTotal = [0,0,0,0,0,0,0,0,0]
        if (tabuleiroAI[i] == 4):
            tabuleiroAI[i] = 3
            tabuleiro[i] = 'O'
            somaTotal[i] = ((tabuleiroAI[0]*tabuleiroAI[1]*tabuleiroAI[2]) + (tabuleiroAI[3]*tabuleiroAI[4]*tabuleiroAI[5]) + (tabuleiroAI[6]*tabuleiroAI[7]*tabuleiroAI[8]) + (tabuleiroAI[0]*tabuleiroAI[3]*tabuleiroAI[6]) + (tabuleiroAI[1]*tabuleiroAI[4]*tabuleiroAI[7]) + (tabuleiroAI[2]*tabuleiroAI[5]*tabuleiroAI[8]) + (tabuleiroAI[0]*tabuleiroAI[4]*tabuleiroAI[8]) + (tabuleiroAI[2]*tabuleiroAI[4]*tabuleiroAI[6]))
            int(somaTotal[i])
            print (somaTotal[i])
            if (somaTotal[i]<somaTotal[i-1]):
                return True
            else:
                tabuleiroAI[i] = 4
                tabuleiro[i] = ' '    
    
        
def play_again():
    novamente = input('Quer jogar novamente? ')
    if (novamente.upper() == 'SIM' or novamente.upper() =='S'):
        tabuleiro = [' ',' ',' ',
                 ' ',' ',' ',
                 ' ',' ',' ']
        check_winner() == False #Play again not working
        tie() == False

def tie():
    for i in range (0,9):
        if tabuleiro[i] == ' ':
            return False
        else:
            return True

def check_winner():
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'X': # X ganhou?
        print ('X Venceu!')
        return True
    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'X':
        print ('X Venceu!')
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'X':
        print ('X Venceu!')
        return True

    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'O': # O ganhou?
        print ('O Venceu!')
        return True
    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'O':
        print ('O Venceu!')
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'O':
        print ('O Venceu!')
        return True
    else:
        return False
    
    
print ('Voce sera "X" e o computador sera "O"!')

while (check_winner() == False and tie() == False):  #Jogo
    imprimir()
    turn()
    AIturn()
    check_winner()

imprimir()
print('O jogo acabou!')
play_again()


    
    

    
