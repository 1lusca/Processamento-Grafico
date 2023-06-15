import cv2 as cv
import filtros as filtros
import Overlay as overlay

def selecionaFiltro(indexFiltro, img):
    if indexFiltro == '11':
        cv.imshow('Filtro - Blur', filtros.blurFunction(img))
    elif indexFiltro == '12':
        cv.imshow('Filtro - Brightness', filtros.brightnessFunction(img))




 
    



def selecionaInput(img, is_camera):
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
        stickers(img, is_camera)
    elif tipo_input == '2': 
        filtros(img, is_camera)
    else:
        main()
    


    
    



def filtros(img, is_camera):
    print('lala')



def stickers(img, is_camera):

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
        sticker = cv.imread('assets/stickers/dino-stronauta.png', cv.IMREAD_UNCHANGED)
    elif sticker_selecionado == '3':
        sticker = cv.imread('assets/stickers/dino-censurado.png', cv.IMREAD_UNCHANGED)
    elif sticker_selecionado == '4':
        sticker = cv.imread('assets/stickers/dino-godzilla.png', cv.IMREAD_UNCHANGED)
    elif sticker_selecionado == '5':
        sticker = cv.imread('assets/stickers/dino-noel.png', cv.IMREAD_UNCHANGED)
    elif sticker_selecionado == '6':
        sticker = cv.imread('assets/stickers/dino-rockeiiro.png', cv.IMREAD_UNCHANGED)
    else:
        selecionaInput(img, is_camera)

    cv.imshow('sticker', img)
    cv.setMouseCallback('sticker', mouse_click)

    cv.waitKey(0)
    cv.destroyAllWindows()



def uploadImagem():
    print('\n')
    caminho_imagem = input('Digite o caminho da imagem: ')
    img = cv.imread(caminho_imagem)
    return img






def mouse_click(event, x, y, 
                flags, param):
      
    if event == cv.EVENT_LBUTTONDOWN:
          
        #sticker = cv.imread('assets/stickers/dino-rockeiro.png', cv.IMREAD_UNCHANGED)

        out = overlay.overlay(img, sticker, x, y) 

        cv.imshow('sticker', out)





print('\n')
print('--------------------------')
print('------- Menu input -------')
print('--------------------------')
print('\n')
print('1 - Upload de imagem')
print('2 - Abrir a camera')
print('0 - Sair')
print('\n')

img = ''
is_camera = False
tipo_input = input('Escolha uma opcao: ')

if tipo_input == '1': 
    img = uploadImagem()
elif tipo_input == '2': 
    is_camera = True
else:
    exit

selecionaInput(img, is_camera)



def main():
    print('\n')
    print('--------------------------')
    print('------- Menu input -------')
    print('--------------------------')
    print('\n')
    print('1 - Upload de imagem')
    print('2 - Abrir a camera')
    print('0 - Sair')
    print('\n')

    sticker = ''
    img = ''
    is_camera = False
    tipo_input = input('Escolha uma opcao: ')

    if tipo_input == '1': 
        img = uploadImagem()
    elif tipo_input == '2': 
        is_camera = True
    else:
        exit

    selecionaInput(img, is_camera)


# while 1:

#     print('\n')
#     print('--------------------------')
#     print('----- MENU PRINCIPAL -----')
#     print('--------------------------')
#     print('\n')
#     print('1 - Upload de imagem')
#     print('2 - Abrir a câmera')
#     index = input('\nEscolha uma opção: ')

#     if index == '1':
#         caminho_imagem = input('Digite o caminho da imagem: ')
        
#         img = cv.imread(caminho_imagem)
#         imgFiltered = img.copy()

#         while 1:

#             print('\n')
#             print('-------------------------------')
#             print('----- Selecione um filtro -----')
#             print('-------------------------------')
#             print('\n')
#             print('11 - Blur')
#             print('12 - Brightness')
#             print('00 - Voltar')
#             indexFiltroUpload = input('\nEscolha uma opção: ')

#             if indexFiltroUpload == '00':
#                 break
#             else:
#                 selecionaFiltro(indexFiltroUpload, img)
            
#             cv.imshow('Imagem original', img)

#             tecla = cv.waitKey(0)
#             cv.destroyAllWindows()
#             if tecla & 0xFF == ord('q'): #seleciona input de imagem
#                 break
#             elif tecla & 0xFF == ord('c'): #seleciona outro filtro
#                 continue

#     elif index == '2':

#         while 1:

#             print('\n')
#             print('-------------------------------')
#             print('----- Selecione um filtro -----')
#             print('-------------------------------')
#             print('\n')
#             print('11 - Blur')
#             print('12 - Brightness')
#             print('00 - Voltar')
#             indexFiltroUpload = input('\nEscolha uma opção: ')
            
#             if indexFiltroUpload == '00':
#                 break
        
#             else:     
#                 capture = cv.VideoCapture(0)
#                 if not capture.isOpened():
#                     print('Erro')
#                     exit(0)
#                 while True:
#                     ret, frame = capture.read()
#                     if frame is None:
#                         break
#                     # Display the resulting frame
#                     selecionaFiltro(indexFiltroUpload, frame)
                    
#                     tecla = cv.waitKey(1)
#                     if tecla & 0xFF == ord('q'): #seleciona input de imagem
#                         break
#                     elif tecla & 0xFF == ord('c'): #seleciona outro filtro
#                         break

#                 capture.release()
#                 cv.destroyAllWindows()

#                 # if tecla & 0xFF == ord('q'): #seleciona input de imagem
#                 #     break
#                 # elif tecla & 0xFF == ord('c'): #seleciona outro filtro
#                 #     continue
                
                

        
        
        
        
#     else:
#         print('Opção inválida')
#         break

    


