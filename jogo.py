from random import choice

palavrasSorteadasParaOJogo = list()
numeroDeDerrotas = 0
numeroDeVitorias = 0
totalDeJogadas = 1

def telaDeInicio():
    menuInicial = '''
    -----------------------------------
    |||||||||GAME DAS PALAVRAS|||||||||
    |---------------------------------|
    |Niveis:                          |
    |1 >>>>>>>>>>>>>>>> Iniciante     |
    |2 >>>>>>>>>>>>>>>> Intermédio    |
    |3 >>>>>>>>>>>>>>>> Díficil       |
    |-1 >>>>>>>>>>>>>>> Terminar      |
    |---------------------------------|'''
    print(menuInicial)
    lerNivelDesejadoPeloUsuario()

    
def lerNivelDesejadoPeloUsuario():
    nivel = str(input('Qual nível pretende: ')).strip()
    validarONivelInseridoPeloUsuario(nivel)


def validarONivelInseridoPeloUsuario(nivel):
    if not nivel[0] in '123':
        if nivel[0] == '-':
            print('O usuário decidiu fechar a aplicação antes de jogar')
        else:
            print(f'Opção inserida invalida\nOpção digitada: {nivel}')
        exit()
    selecionarAsListasDePalavrasParaOJogo(nivel[0])


def selecionarAsListasDePalavrasParaOJogo(nivel):
    if(nivel == '1'):
        from ConjuntoDePalavrasParaOJogo import PalavrasCom4Letras, PalavrasCom5Letras
        
        sorteadorDePalavrasParaOJogo(PalavrasCom4Letras)
        sorteadorDePalavrasParaOJogo(PalavrasCom5Letras)
    elif(nivel == '2'):
        from ConjuntoDePalavrasParaOJogo import PalavrasCom5Letras, PalavrasCom6Letras
        
        sorteadorDePalavrasParaOJogo(PalavrasCom5Letras)
        sorteadorDePalavrasParaOJogo(PalavrasCom6Letras)
    else:
        from ConjuntoDePalavrasParaOJogo import PalavrasCom6Letras, PalavrasCom8Letras
        
        sorteadorDePalavrasParaOJogo(PalavrasCom6Letras)
        sorteadorDePalavrasParaOJogo(PalavrasCom8Letras)

        
def sorteadorDePalavrasParaOJogo(listaDePalavras):
    global palavrasSorteadasParaOJogo
    
    quantPalavrasSorteadas = 0
    
    while quantPalavrasSorteadas < 3:
            palavraSorteada = choice(listaDePalavras)
            if not palavraSorteada in palavrasSorteadasParaOJogo:
                palavrasSorteadasParaOJogo.append(palavraSorteada)
                quantPalavrasSorteadas += 1
                

if __name__ == '__main__':
    telaDeInicio()
    while True:
        palavraSorteada = choice(palavrasSorteadasParaOJogo)
        print(f'{totalDeJogadas}º Jogada')
        print(f'\033[40;35;1mACERTOS: {numeroDeVitorias}\033[m \n\033[31;40;1mFALHAS: {numeroDeDerrotas}\033[m')
        print(f'Palavras Sorteadas: {palavrasSorteadasParaOJogo}')
        print('-'*35)
        print(f'Dica: A palavra sorteado tem \033[31;40;1m{len(palavraSorteada)} letras\033[m')
        print('_'*50)
        palavraInseridaPeloUsuario = str(input('Palavra: ')).strip().lower()
        totalDeJogadas += 1
        if palavraInseridaPeloUsuario == palavraSorteada:
            print('\033[32;40;1mACERTOU')
            numeroDeVitorias += 1
            continue
        elif palavraInseridaPeloUsuario == '-1':
            break
        numeroDeDerrotas += 1
        print(f'\033[31;40;1mERRADO!!!!\nPalavra Sorteada: {palavraSorteada}')
