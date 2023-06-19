import cv2 as cv
import overlay
import filtros

def selecionaFiltro(indexFiltro, img, imgOriginal):

    if indexFiltro == '1':
        imgFiltered = filtros.canalUnico(img)
        cv.imshow('Filtro - um canal de cor', imgFiltered)

    elif indexFiltro == '2':
        imgFiltered = filtros.greyScaleAritmetica(img)
        cv.imshow('Filtro - greyScale aritmetica', imgFiltered)

    elif indexFiltro == '3':
        imgFiltered = filtros.greyScalePonderada(img)
        cv.imshow('Filtro - greyScale ponderada', imgFiltered)

    elif indexFiltro == '4':
        imgFiltered = filtros.colorizacao(img)
        cv.imshow('Filtro - colorizacao', imgFiltered)

    elif indexFiltro == '5':
        imgFiltered = filtros.inversao(img)
        cv.imshow('Filtro - inversao', imgFiltered)

    elif indexFiltro == '6':
        imgFiltered = filtros.binarizacao(img)
        cv.imshow('Filtro - binarizacao', imgFiltered)

    elif indexFiltro == '7':
        imgFiltered = filtros.recortar(img)
        cv.imshow('Filtro - recortar', imgFiltered)

    elif indexFiltro == '8':
        imgFiltered = filtros.redimensionar(img)
        cv.imshow('Filtro - redimensionar', imgFiltered)

    elif indexFiltro == '9':
        imgFiltered = filtros.blur(img)
        cv.imshow('Filtro - blur', imgFiltered)

    elif indexFiltro == '10':
        imgFiltered = filtros.canny(img)
        cv.imshow('Filtro - bordas canny', imgFiltered)

    elif indexFiltro == '11':
        imgFiltered = filtros.sobel(img)
        cv.imshow('Filtro - bordas sobel', imgFiltered)

    elif indexFiltro == '12':
        imgFiltered = filtros.dilatacao(img)
        cv.imshow('Filtro - dilatacao', imgFiltered)

    elif indexFiltro == '13':
        imgFiltered = filtros.erosao(img)
        cv.imshow('Filtro - erosao', imgFiltered)

    elif indexFiltro == '14':
        imgFiltered = filtros.winter(img)
        cv.imshow('Filtro - winter', imgFiltered)
        

    cv.imshow('Imagem original', imgOriginal)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return imgFiltered

def mouse_click(event, x, y, 
                flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        out = overlay.overlay(img, sticker, x, y) 
        cv.imshow('Stickers', out)

# loop para selecionar a imagem
while 1:
    print('\n')
    print('--------------------------')
    print('---- Lista de imagens -----')
    print('--------------------------')
    print('\n')
    print('1 - Corgi')
    print('2 - Maltes')
    print('3 - Carregar imagem')
    print('0 - Sair')
    print('\n')

    imagem = input('Escolha uma imagem: ')

    if imagem == '1': 
        img = cv.imread('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/assets/images/corgi.jpg')
    elif imagem == '2':
        img = cv.imread('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/assets/images/maltes.jpg')
    elif imagem == '3':
        caminho_imagem = input('Digite o caminho da imagem: ')
        img = cv.imread(caminho_imagem)
    else:
        break

    imgOriginal = img.copy()

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
        print('4 - Reset imagem')
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
                    sticker = cv.imread('assets/stickers/dino-abduzido.png', cv.IMREAD_UNCHANGED)
                elif sticker_selecionado == '2':
                    sticker = cv.imread('assets/stickers/dino-astronauta.png', cv.IMREAD_UNCHANGED)
                elif sticker_selecionado == '3':
                    sticker = cv.imread('assets/stickers/dino-censurado.png', cv.IMREAD_UNCHANGED)
                elif sticker_selecionado == '4':
                    sticker = cv.imread('assets/stickers/dino-godzilla.png', cv.IMREAD_UNCHANGED)
                elif sticker_selecionado == '5':
                    sticker = cv.imread('assets/stickers/dino-noel.png', cv.IMREAD_UNCHANGED)
                elif sticker_selecionado == '6':
                    sticker = cv.imread('assets/stickers/dino-rockeiro.png', cv.IMREAD_UNCHANGED)
                else:
                    cv.destroyAllWindows()
                    break

                cv.imshow('Stickers', img)
                cv.setMouseCallback('Stickers', mouse_click)

                cv.waitKey(0)
                cv.destroyAllWindows()
            

        elif tipo_input == '2': 
            
            # loop para selecionar o filtro
            while 1:
                print('\n')
                print('-------------------------------')
                print('------ Lista de filtros -------')
                print('-------------------------------')
                print('\n')

                print('1 - Um canal de cor')
                print('2 - Greyscale aritmetica')
                print('3 - Greyscale ponderada')
                print('4 - Colorizacao')
                print('5 - Inversao')
                print('6 - Binarizacao')
                print('7 - Recortar')
                print('8 - Redimensionar')
                print('9 - Blur')
                print('10 - Bordas canny')
                print('11 - Bordas sobel')
                print('12 - Dilatacao')
                print('13 - Erosao')
                print('14 - Winter (meus filtros)')
                print('0 - Voltar')

                filtro_selecionado = input('\nEscolha uma opção: ')

                if filtro_selecionado == '0':
                    break
                else:
                    img = selecionaFiltro(filtro_selecionado, img, imgOriginal)

        elif tipo_input == '3':
            cv.imwrite('/Users/1lusca/Documents/GitHub/Processamento-Grafico/tgb/out/imagem.png', img)
            print("Imagem salva com sucesso!")

        elif tipo_input == '4':
            img = imgOriginal
            print("Imagem resetada!")

        else:
            break







