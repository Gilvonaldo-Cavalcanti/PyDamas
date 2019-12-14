#coding: latin1
from random import randint

tab = []
TURNO = 0

def cadastra_jogador(nome, nome1, jogadorA, jogadorB):
# Cadastra os jogadores e atribui uma peça para cada jogador
    esc = randint(0, 1)
    if esc == 0:
        nome = "p"
    else:
        nome = "b"
    if esc == 1:
        nome1 = "p"
    else:
        nome1 = "b"
    return str(jogadorA) + " sua peça é "+nome+'\n' + str(jogadorB) + " sua peça é "+nome1+'\n'

def iniciar_jogo():
# Lista de listas, tabuleiro do jogo, as posições são representadas
# por casas " " e casas "", as casas " " são as casas onde pode-se realizar jogadas, e
# as "" são as casas vazias, que não pode ser oculpadas por nenhuma peça. 
    global tab
    tab = [[" ", "", " ", "", " ", "", " ", ""],
           ["", " ", "", " ", "", " ", "", " "],
           [" ", "", " ", "", " ", "", " ", ""],
           ["", " ", "", " ", "", " ", "", " "],
           [" ", "", " ", "", " ", "", " ", ""],
           ["", " ", "", " ", "", " ", "", " "],
           [" ", "", " ", "", " ", "", " ", ""],
           ["", " ", "", " ", "", " ", "", " "]]

def muda_turno():
#Muda a vez, a cada vez que for realizada uma jogada 
    global TURNO
    if TURNO == 0:
        TURNO = 1
    else:
        TURNO = 0 
        
def get_vez():
# Indica de quem é a vez de jogar.    
    global TURNO
    if TURNO == 0:
        return "é a vez das peças Brancas !!!"
    if TURNO == 1:
        return "é a vez das peças Pretas !!!\n"

def imprime_tabuleiro():
# Imprime um tabuleiro na tela para visualização do usuario
    t = "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[0][0]+"  |   "+tab[0][1]+"  |  "+tab[0][2]+"  |   "+tab[0][3]+"  |  "+tab[0][4]+"  |   "+tab[0][5]+"  |  "+tab[0][6]+"  |   "+tab[0][7]+"  |"" 1\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |   "+tab[1][0]+"  |  "+tab[1][1]+"  |   "+tab[1][2]+"  |  "+tab[1][3]+"  |   "+tab[1][4]+"  |  "+tab[1][5]+"  |   "+tab[1][6]+"  |  "+tab[1][7]+"  |"" 2\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[2][0]+"  |   "+tab[2][1]+"  |  "+tab[2][2]+"  |   "+tab[2][3]+"  |  "+tab[2][4]+"  |  "+tab[2][5]+"   |  "+tab[2][6]+"  |  "+tab[2][7]+"   |"" 3\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |   "+tab[3][0]+"  |  "+tab[3][1]+"  |   "+tab[3][2]+"  |  "+tab[3][3]+"  |   "+tab[3][4]+"  |  "+tab[3][5]+"  |  "+tab[3][6]+"   |  "+tab[3][7]+"  |"" 4\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[4][0]+"  |  "+tab[4][1]+"   |  "+tab[4][2]+"  |  "+tab[4][3]+"   |  "+tab[4][4]+"  |  "+tab[4][5]+"   |  "+tab[4][6]+"  |  "+tab[4][7]+"   |"" 5\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[5][0]+"   |  "+tab[5][1]+"  |  "+tab[5][2]+"   |  "+tab[5][3]+"  |  "+tab[5][4]+"   |  "+tab[5][5]+"  |  "+tab[5][6]+"   |  "+tab[5][7]+"  |"" 6\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[6][0]+"  |  "+tab[6][1]+"   |  "+tab[6][2]+"  |  "+tab[6][3]+"   |  "+tab[6][4]+"  |  "+tab[6][5]+"   |  "+tab[6][6]+"  |  "+tab[6][7]+"   |"" 7\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "   |  "+tab[7][0]+"   |  "+tab[7][1]+"  |  "+tab[7][2]+"   |  "+tab[7][3]+"  |  "+tab[7][4]+"   |  "+tab[7][5]+"  |  "+tab[7][6]+"   |  "+tab[7][7]+"  |"" 8\n"
    t+= "    +-----+-----+-----+-----+-----+-----+-----+-----+\n'"
    t+= "      1     2     3     4     5     6     7     8"
    return t 

def organiza_tabuleiro():
# Organiza as peças nas posições iniciais de jogo.
    global tab
    for i in range(0,8,2):
            tab[0][i] = "p"
    for i in range(1,8,2):
            tab[1][i] = "p"
    for i in range(0,8,2):
            tab[2][i] = "p"
    for i in range(1,8,2):
            tab[5][i] = "b"
    for i in range(0,8,2):
            tab[6][i] = "b"
    for i in range(1,8,2):
            tab[7][i] = "b"                       
    return tab

def jogada_valida(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem):
#Testa se as jogadas realisadas pelo usuario são validas 
    
    if linhaDestino > 8 or linhaDestino < 1 or linhaOrigem > 8 or linhaOrigem < 1:
        return False 
    if (tab[linhaDestino - 1][colunaDestino - 1] != " " or tab[linhaOrigem - 1][colunaOrigem - 1] == " ") or tab[linhaOrigem - 1][colunaOrigem - 1] == "":
        return  False
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "p" and (linhaDestino < linhaOrigem):
        return False        
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "b" and (linhaDestino > linhaOrigem):
        return False
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "b" and ((linhaOrigem - 1) - (linhaDestino - 1)) > 2:
        return False
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "p" and ((linhaDestino - 1) - (linhaOrigem - 1)) > 2:
        return False
    return True

def testa_turno(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, TURNO):
#testa a vez da jogada, 0 quando é a vez das peças brancas e um quando é a vez das peças pretas.
    if TURNO == 0:
        if tab[linhaOrigem - 1][colunaOrigem - 1] == "p" or tab[linhaOrigem - 1][colunaOrigem - 1] == "D":
            return False
        else:
            return True
    if TURNO == 1:
        if tab[linhaOrigem - 1][colunaOrigem - 1] == "b" or tab[linhaOrigem - 1][colunaOrigem - 1] == "B":
            return False
        else:
            return True

def manipula_tabuleiro(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino, jogada_valida, testa_turno, captura_pecas_pretas):
#se a jogada for valida, Manipula as peças dentro do tabuleiro, de acordo com as cordenadas fornecidas pelo usuario na interface,
#atravez de (linhaOrigem, colunaOrigem, linhaDestino, colunaDestino).
    global tab
    
    if jogada_valida(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem):
        if captura_pecas_pretas(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas(colunaOrigem,colunaDestino)):
            if Captura_Pecas_Brancas(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas(colunaOrigem,colunaDestino)):
                if testa_turno(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, TURNO):
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    muda_turno()    
                    return tab
                else:
                    raise TypeError
            else:
                raise TypeError
        else:
            raise TypeError  
    else:
        raise NameError

def Dama(linhaDestino, colunaDestino):
#Quando uma peça b chega na linha 1 no tabuleiro ela é promovida a Dama, e quando uma peça p chega a linha 8 no tabuleiro,
#ela é promovida a Dama.
    global tab
    for i in range(8):    
        if tab[0][i] == "b":
            tab[linhaDestino - 1][colunaDestino - 1] = "B"
            return tab
    for i in range(8):
        if tab[7][i] == "p":
            tab[linhaDestino - 1][colunaDestino - 1] = "D" 
            return tab
        
def testa_direcao_colunas(colunaOrigem, colunaDestino):
#testa para que lado o usuario realizar a jogada usando como parâmetros as colunas
#dentro do tabuleiro, (para Direita = 1, para a esquerda = 0)
    if colunaOrigem < colunaDestino:
        return 1
    else:
        return 0 
    
def testa_direcao_linhas(linhaDestino, linhaOrigem):
#testa para que lado o usuario realizar a jogada usando como parâmetros as linhas
#dentro do tabuleiro, (para Cima = 1, para Baixo = 0)
    if linhaOrigem > linhaDestino:
        return 1
    else:
        return 0

def captura_pecas_pretas(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas):
    global tab
    if (tab[linhaOrigem - 1][colunaOrigem - 1] == "b" or tab[linhaOrigem - 1][colunaOrigem - 1] == "B") and ((linhaDestino - 1) - (linhaOrigem - 1)) == -2:    
        #captura as peças pretas, se a comida, dentro do tabuleiro, for para a direita
        if testa_direcao_colunas == 1:
            if tab[linhaDestino][colunaDestino - 2] == "p" or tab[linhaDestino][colunaDestino - 2] == "D":
                tab[linhaDestino - 1][colunaDestino -1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                tab[linhaDestino][colunaDestino - 2] = " "
                return tab
            else:
                raise NameError 
        #captura as peças pretas, se a comida, dentro do tabuleiro, for para a esquerda
        if testa_direcao_colunas == 0:    
            if tab[linhaDestino][colunaDestino] == "p" or tab[linhaDestino][colunaDestino] == "D":
                tab[linhaDestino - 1][colunaDestino -1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                tab[linhaDestino][colunaDestino] = " "
                return tab
            else:
                raise NameError      
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "B":
        captura_pecas_para_tras(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas, testa_direcao_linhas, jogada_valida) 
    else:
        return True
    
def Captura_Pecas_Brancas(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas):
    global tab
    if (tab[linhaOrigem - 1][colunaOrigem - 1] == "p" or tab[linhaOrigem - 1][colunaOrigem - 1] == "D") and ((linhaDestino - 1) - (linhaOrigem - 1)) == 2:    
        #captura as peças Brancas, se a comida, dentro do tabuleiro, for para a direita
        if testa_direcao_colunas == 1:            
            if tab[linhaDestino - 2][colunaDestino - 2] == "b" or tab[linhaDestino - 2][colunaDestino - 2] == "B":
                tab[linhaDestino - 1][colunaDestino -1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                tab[linhaDestino - 2][colunaDestino - 2] = " "
                return tab
            else:
                raise NameError 
        #captura as peças Brancas, se a comida, dentro do tabuleiro, for para a esquerda
        if testa_direcao_colunas == 0:
            if tab[linhaDestino - 2][colunaDestino] == "b" or tab[linhaDestino - 2][colunaDestino] == "B":
                tab[linhaDestino - 1][colunaDestino -1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                tab[linhaDestino - 2][colunaDestino] = " "
                return tab
            else:
                raise NameError
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "D":
        captura_pecas_para_tras(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas, testa_direcao_linhas, jogada_valida)
    else:
        return True
    
def captura_pecas_para_tras(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, testa_direcao_colunas, testa_direcao_linhas, jogada_valida):
#Realiza a captura de peças adversarias para traz pelas damas.
    global tab  
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "B": 
        if testa_direcao_linhas(linhaDestino, linhaOrigem) == 0:
            if testa_direcao_colunas == 0:
                if tab[linhaDestino - 2][colunaDestino] == "p" or tab[linhaOrigem][colunaOrigem] == "D":
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    tab[linhaDestino - 2][colunaDestino] = " "
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    muda_turno()
                    return tab
                else:
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    muda_turno()
            if testa_direcao_colunas == 1:
                if tab[linhaDestino - 2][colunaDestino - 2] == "p" or tab[linhaDestino - 2][colunaDestino - 2] == "D":
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaDestino - 2][colunaDestino - 2] = " "
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    muda_turno()
                    return tab
                else:
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " " 
                    muda_turno()
    if tab[linhaOrigem - 1][colunaOrigem - 1] == "D":
        if testa_direcao_linhas(linhaDestino, linhaOrigem) == 1:
            if testa_direcao_colunas == 1:
                if tab[linhaDestino][colunaDestino - 2] == "b" or tab[linhaDestino][colunaDestino - 2] == "B":
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaDestino][colunaDestino - 2] = " "
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    return tab
                else:
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " " 
                    muda_turno()
            if testa_direcao_colunas == 0:
                if tab[linhaDestino][colunaDestino] == "p" or tab[linhaDestino][colunaDestino] == "D":
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaDestino][colunaDestino] = " "
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " "
                    return tab
                else:
                    tab[linhaDestino - 1][colunaDestino - 1] = tab[linhaOrigem - 1][colunaOrigem - 1]
                    tab[linhaOrigem - 1][colunaOrigem - 1] = " " 
                    muda_turno()

def verifica_situacao(p, b):
#verifica a situação do tabuleiro, conta a quantidade de peças no tabuleiro 
#e retorna a quantidade de peças de cada jogador. 
    for i in tab[0][:]:
        b = i.count("b")
        p = i.count("p")
    for i in tab[1][:]:
        p = p + i.count("p")
        b = b + i.count("b")
    for i in tab[2][:]:
        b = b + i.count("b")
        p = p + i.count("p")
    for i in tab[3][:]:
        p = p + i.count("p")
        b = b + i.count("b")
    for i in tab[4][:]:
        b = b + i.count("b")
        p = p + i.count("p")
    for i in tab[5][:]:
        p = p + i.count("p")
        b = b + i.count("b")
    for i in tab[6][:]:
        b = b + i.count("b")
        p = p + i.count("p")
    for i in tab[7][:]:
        p = p + i.count("p")
        b = b + i.count("b")
    for i in tab[0][:]:
        p = p + i.count("p")
        b = b + i.count("b")
    return p, b
        
def terminou_jogo(p, b):
# Retorna, se terminou ou não o jogo tomando como 
#parametros a funão (verifica_situacao()).
    if verifica_situacao == 0:
        return True
    else:
        return False
    if verifica_situacao == 0:
        return True
    else:
        return False
