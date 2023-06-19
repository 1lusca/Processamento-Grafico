import cv2 as cv
import numpy as np

# renderiza um unico canal de cor
# renderizando o canal Blue
# 0 = blue, 1  = green, red = 2
def canalUnico(img):
  blue_channel = img[:, :, 0]
  return cv.cvtColor(blue_channel, cv.COLOR_GRAY2BGR)

# grayscale media aritmetica
# scale com valor maior = imagem com grayscale mais claro
# scale com valor menor = imagem com grayscale mais escuro
def greyScaleAritmetica(img):
  temp = img.copy()
  scale = 0.3
  for i in range(temp.shape[0]): #percorre linhas
    for j in range(temp.shape[1]): #percorre colunas
      media = temp.item(i,j,0) * scale + temp.item(i,j,1) * scale + temp.item(i,j,2) * scale
      temp.itemset((i,j,0),media) # canal B
      temp.itemset((i,j,1),media) # canal G
      temp.itemset((i,j,2),media) # canal R
  return temp
      
# grayscale media ponderada
# scale com valor maior = imagem com grayscale mais claro
# scale com valor menor = imagem com grayscale mais escuro
def greyScalePonderada(img):
  temp = img.copy()
  scale = 0.3
  for i in range(temp.shape[0]): #percorre linhas
    for j in range(temp.shape[1]): #percorre colunas
      media = temp.item(i,j,0) * scale + temp.item(i,j,1) * scale + temp.item(i,j,2) * scale
      temp.itemset((i,j,0),media) # canal B
      temp.itemset((i,j,1),media) # canal G
      temp.itemset((i,j,2),media) # canal R
  return temp

# colorizacao
# altera a cor da imagem no padrao rgb
def colorizacao(img):
  temp = img.copy()
  red = 162
  green = 0
  blue = 255
  for i in range(temp.shape[0]):
     for j in range(temp.shape[1]):
        B = temp.item(i,j,0) | blue
        G = temp.item(i,j,1) | green
        R = temp.item(i,j,2) | red
        temp.itemset((i,j,0),B) # canal B
        temp.itemset((i,j,1),G) # canal G
        temp.itemset((i,j,2),R) # canal R
  return temp

# inversao
# percorre pixel a pixel e inverte o valor
def inversao(img):
  return cv.bitwise_not(img)

# binarizacao
# os pixels com valores menores ou igual que o limite serao pretos
# os pixels com valores maiores que o limite serao brancos
def binarizacao(img):
  limite = 127
  limitePixelsBrancos = 255
  retval, img = cv.threshold(img, limite, limitePixelsBrancos, cv.THRESH_BINARY)
  return img

# recortar
# 640 × 424 imagem original
def recortar(img):
  x1, y1 = 100, 100  # superior esquerdo
  x2, y2 = 500, 500  # inferior direito
  return img[y1:y2, x1:x2]

# redimensioar
# new_width = nova largura da imagem
# new_height = nova altura da imagem
def redimensionar(img):
  new_width = 300
  new_height = 300
  return cv.resize(img, (new_width, new_height))

# desfoque
# percorre pixel a pixel calculando a media dos pixel na area do kernel, e aplica no pixel atual
# quanto maior a matriz do kernel, maior o desfoque
def blur(img):
  kernel = (14, 14)
  return cv.blur(img, kernel)

# deteccao de borda canny
# deteccao de bordas na imagem
# limiar minimo: quanto menor o valor, detecta bordas mais fracas
# limiar maximo: quanto maior o valor, detecta bordas mais fortes
def canny(img):
  limiarMinimo = 80
  limiarMaximo = 200
  return cv.Canny(img, limiarMinimo, limiarMaximo)

# deteccao de borda sobel
# deteccao de bordas na imagem atraves do gradiente de sobel
# calcula as derivadas de primeira ordem
def sobel(img):
  sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
  sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
  temp = np.sqrt(sobelx**2 + sobely**2) #calcula magnitude das bordas
  temp = cv.normalize(temp, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U) #normaliza a magnitude 255
  return temp

# dilatacao
# dilata/aumenta o tamanho dos objetos na imagem
# percorre pixel a pixel a imagem
# quando maior a matriz do kernel, maior a dilatacao do pixel
def dilatacao(img):
  kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))
  return cv.dilate(img, kernel)

# erosao
# diminui o tamanho dos objetos na imagem
# percorre pixel a pixel a imagem
# quando maior a matriz do kernel, maior a diminuicao do pixel
def erosao(img):
  kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))
  return cv.erode(img, kernel)

# winter
# utiliza um preset de mapa de cores do opencv
def winter(img):
  img = cv.applyColorMap(img, cv.COLORMAP_WINTER)
  # ajusta o brilho
  alpha = 1.2  # fator de ajuste de brilho
  beta = -50  # valor de deslocamento de brilho
  return cv.convertScaleAbs(img, alpha=alpha, beta=beta)
