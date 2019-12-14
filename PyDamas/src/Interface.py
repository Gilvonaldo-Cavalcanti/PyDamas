#coding: latin1
from Logica import imprime_tabuleiro, organiza_tabuleiro, cadastra_jogador, manipula_tabuleiro, iniciar_jogo, terminou_jogo
from Logica import jogada_valida, testa_turno, TURNO, get_vez, captura_pecas_pretas, Dama, verifica_situacao
import time, os 

print "\n"
print "  #############################################################################"
time.sleep(0.2)
print "  # ||||||\\  \ \    / / ||||||\\    / ____  \ |  \    /  |  / ____  \  /  ___| #"
time.sleep(0.2)
print "  # |||   \\\\\ \ \  / /  |||   \\\\\ | |    | | |   \  /   | | |    | | | /      #"
time.sleep(0.2)
print "  # |||__ ///  \ \/ /   |||   ||| | |____| | | |\ \/ /| | | |____| | \ \____  #"
time.sleep(0.2)
print "  # |||||///    |  |    |||   ||| |  ____  | | | \__/ | | |  ____  |  \___  \ #"
time.sleep(0.2)
print "  # |||         |  |    |||__///  | |    | | | |      | | | |    | |  ____| | #"
time.sleep(0.2)
print "  # |||         |  |    |||||//   | |    | | | |      | | | |    | | |_____/  #"
time.sleep(0.2)
print "  #############################################################################"

time.sleep(1)
M = "\n                           |-------- Menu ---------| \n"
M+= "                           |      Novo Jogo => 1   |\n"
M+= "                           |        Sobre   => 2   |\n"
M+= "                           |         Sair   => 3   |\n"
M+= "                           |-----------------------|\n"
print M

#Variaveis 
p = 0
b = 0
nome = ""
nome1 = ""

while True:
#testa se a op��o escolhida pelo usu�rio � valida
    try:
        try:
            op = input()
            break
        except SyntaxError:
            print "entrada invalida, digite 1, 2 ou 3."
    except NameError:
        print "entrada invalida, voc� digitou uma letra em vez de um numero"

while op != 1 and op != 2 and op != 3:
    print "Valor invalido !!! digite 1, 2 ou 3"
    op = input()

if op == 1:

    print "\n             -----------Bem vindo ao PyDamas !!!----------- \n \n "

    jogadorA = raw_input("Digite o nome do jogador 1:")
    jogadorB = raw_input("Digite o nome do jogador 2:")
    print '\n'
    
    iniciar_jogo()
    organiza_tabuleiro()
    print cadastra_jogador(nome, nome1, jogadorA, jogadorB)
    time.sleep(3)
    terminou_jogo(p, b)
    terminou = False

    while not(terminou):
    #Enquanto n�o terminar o jogo, o While permanesse rodando.            
        print get_vez()
        os.system('cls')
        print '\n'
        print imprime_tabuleiro()+'\n'
        
        verifica_situacao(p, b)
        
        if terminou:
            iniciar_jogo()
        
        print get_vez()
        while True:
        #recebe as codernadas do usu�rio
            try:
                try:
                    try: 
                        linhaOrigem = input("Linha de origem da pe�a:")
                        colunaOrigem = input("Coluna de origem da pe�a:")
                        linhaDestino = input("Linha de destino da pe�a:")
                        colunaDestino = input("Coluna de destino da pe�a:")
                        print '\n'
                        break
                    except SyntaxError:
                        print "jogada invalida, digite as coredenadas corretamente."
                except NameError:
                    print "Jogada invalida, voc� digitou uma letra em vez de um n�mero"
            except IndexError:
                print "Jogada invalida, n�o existe essa posi��o dentro so tabuleiro"
            try:
                testa_turno(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem, TURNO)
            except IndexError:
                print "Jogada invalida, n�o existe essa posi��o dentro do tabuleiro"
        
        jogada_valida(linhaDestino, colunaDestino, linhaOrigem, colunaOrigem)
         
        try:    
            try:
                try:
                    try:
                        manipula_tabuleiro(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino, jogada_valida, testa_turno, captura_pecas_pretas)
                                 
                        Dama(linhaDestino, colunaDestino)
                        
                    except IndexError:
                        print "Jogada invalida, n�o existe essa posi��o dentro do tabuleiro"
                
                except SyntaxError:
                    print "Jogada invalida, digite as cordenardas corretamente"
                    time.sleep(2)
            except NameError:
                print "Jogada invalida"
                time.sleep(2) 
        except TypeError:
            print "Jogada invalida, N�o � sua vez"
            time.sleep(2)
        terminou = terminou_jogo(p, b) 

# Caso o usuario escolha a op��o 2(Sobre), ser� imprimido na tela informa��es sobre o jogo. 
if op == 2:
    print "=================================# PyDamas #========================================\n"

    print "                           Projeto de Programa��o 1"
    print "               Sob Orienta��o: Prof. Henrique do Nascimento Cunha"
    print "             Desenvolvido por: Gilvonaldo Alves da Silva Cavalcanti"

# Caso escolha a op��o 3(Sair), limparar a tela e sairar so jogo.   
if op == 3:
    os.system('cls')
    SystemExit
    print '\n'
    print '\n'
    print "                           THE END"
     
