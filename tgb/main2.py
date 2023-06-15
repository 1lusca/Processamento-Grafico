import cv2
import Overlay

def selecionaFiltro(indexFiltro):
    if indexFiltro == '1':
        cv2.imshow('Filtro - blur', blurFunction())
    elif indexFiltro == '2':
        cv2.imshow('Filtro - brightness', brightnessFunction())

def blurFunction():
  img = cv2.GaussianBlur(img, (13, 13), 5, 0)
  return img

def brightnessFunction():
  return cv2.convertScaleAbs(img, beta=60)

def mouse_click(event, x, y, 
                flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        out = Overlay.overlay(img, sticker, x, y) 
        cv2.imshow('Stickers', out)

# loop para selecionar a imagem
while 1:
    print('\n')
    print('--------------------------')
    print('---- Lista de imagens -----')
    print('--------------------------')
    print('\n')
    print('1 - Corgi')
    print('2 - Maltes')
    print('0 - Sair')
    print('\n')

    imagem = input('Escolha uma imagem: ')

    if imagem == '1': 
        img = cv2.imread('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/assets/images/corgi.jpg')
    elif imagem == '2':
        img = cv2.imread('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/assets/images/maltes.jpg')
    else:
        break

    # loop para selecionar a opcao (sticker ou filtro)
    while 1:
        print('\n')
        print('--------------------------')
        print('------- Menu opcao -------')
        print('--------------------------')
        print('\n')
        print('1 - Stickers')
        print('2 - Filtros')
        print('3 - Salvar a imagem')
        print('0 - Voltar')
        print('\n')

        tipo_input = input('Escolha uma opcao: ')

        if tipo_input == '1': 

            # loop para selecionar o sticker
            while 1:

                print('\n')
                print('--------------------------')
                print('--- Lista de stickers ----')
                print('--------------------------')
                print('\n')
                print('1 - Dino abduzido')
                print('2 - Dino astronauta')
                print('3 - Dino cansurado')
                print('4 - Dino godzilla')
                print('5 - Dino noel')
                print('6 - Dino rockeiro')
                print('0 - Voltar')
                print('\n')

                sticker_selecionado = input('Qual sticker voce quer: ')

                if sticker_selecionado == '1':
                    sticker = cv2.imread('assets/stickers/dino-abduzido.png', cv2.IMREAD_UNCHANGED)
                elif sticker_selecionado == '2':
                    sticker = cv2.imread('assets/stickers/dino-astronauta.png', cv2.IMREAD_UNCHANGED)
                elif sticker_selecionado == '3':
                    sticker = cv2.imread('assets/stickers/dino-censurado.png', cv2.IMREAD_UNCHANGED)
                elif sticker_selecionado == '4':
                    sticker = cv2.imread('assets/stickers/dino-godzilla.png', cv2.IMREAD_UNCHANGED)
                elif sticker_selecionado == '5':
                    sticker = cv2.imread('assets/stickers/dino-noel.png', cv2.IMREAD_UNCHANGED)
                elif sticker_selecionado == '6':
                    sticker = cv2.imread('assets/stickers/dino-rockeiro.png', cv2.IMREAD_UNCHANGED)
                else:
                    cv2.destroyAllWindows()
                    break

                cv2.imshow('Stickers', img)
                cv2.setMouseCallback('Stickers', mouse_click)

                cv2.waitKey(0)
                cv2.destroyAllWindows()
            

        elif tipo_input == '2': 
            
            # loop para selecionar o filtro
            while 1:
                print('\n')
                print('-------------------------------')
                print('------ Lista de filtros -------')
                print('-------------------------------')
                print('\n')
                print('1 - Blur')
                print('2 - Brightness')
                print('0 - Voltar')

                filtro_selecionado = input('\nEscolha uma opção: ')

                if filtro_selecionado == '0':
                    break
                else:
                    # imgOriginal = img.copy()
                    selecionaFiltro(filtro_selecionado)
                    # cv2.imshow('Imagem original', imgOriginal)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

        elif tipo_input == '3':
            cv2.imwrite('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/out/imagem.png', img)
            print("Imagem salva com sucesso!")

        else:
            break







