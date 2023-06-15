import cv2 as cv

def inicio():
    print('\n')

inicio()

caminho_imagem = input('Digite o caminho da imagem: ')
img = cv.imread(caminho_imagem)

while 1:

    print('\n')
    print('--------------------------')
    print('------- Menu opcao -------')
    print('--------------------------')
    print('\n')
    print('1 - Stickers')
    print('2 - Filtros')
    print('0 - Voltar')
    print('\n')

    tipo_input = input('Escolha uma opcao: ')

    if tipo_input == '1': 
        print('lala')
    elif tipo_input == '2': 
        print('lala')
    else:
        break
 