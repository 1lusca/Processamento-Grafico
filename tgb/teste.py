# import tkinter as tk
# import cv2
# import numpy as np

# # Carrega a imagem
# image = cv2.imread("baboon.png")

# def blueFilter():
#     cv2.destroyAllWindows()
#     blue_filter_table = np.zeros((256, 1, 3), dtype=np.uint8)
#     for i in range(256):
#         blue_filter_table[i] = [np.clip(2 * i, 0, 255), 0, 0]
#         filtered_image = cv2.LUT(image, blue_filter_table)
#         cv2.imshow("Imagem azul", filtered_image)

# def greenFilter():
#     cv2.destroyAllWindows()
#     green_filter_table = np.zeros((256, 1, 3), dtype=np.uint8)
#     for i in range(256):
#         green_filter_table[i] = [0, np.clip(2 * i, 0, 255), 0]
#         filtered_image = cv2.LUT(image, green_filter_table)
#         cv2.imshow("Imagem verde", filtered_image)

# # Cria uma janela
# window = tk.Tk()

# # Lista de nomes dos botões
# button_names = ["Blue", "Green"]
# button_callBack = [blueFilter(), greenFilter()]


# def filters(i):
#     if i == 0:
#         blueFilter()
#     elif i == 1:
#         greenFilter()
#     else:
#         print("a é igual a b")



# # Criação dinâmica dos botões
# buttons = []
# for name in button_names:
#     button = tk.Button(window, text=name, command=lambda n=name: filters(n))
#     button.pack()
#     buttons.append(button)




# # Inicia o loop de eventos da janela
# window.mainloop()




# import numpy as np
# import cv2 as cv

# img = cv.imread('baboon.png') #original
# img2 = cv.imread('baboon.png') #copia para img modificada
# print(img.shape) #exibe informações de dimensões e nro de canais

# for i in range(img.shape[0]): #percorre linhas
# 	for j in range(img.shape[1]): #percorre colunas
# 		media = img.item(i,j,0) * 0.333 + img.item(i,j,1) * 0.333 + img.item(i,j,2) * 0.3333
# 		img2.itemset((i,j,0),media) # canal B
# 		img2.itemset((i,j,1),media) # canal G
# 		img2.itemset((i,j,2),media) # canal R
	
# cv.imshow("Original",img)
# cv.imshow("Grayscale",img2)

# cv.waitKey(0)





# import numpy as np
# import cv2 as cv2

# cap = cv2.VideoCapture(1)

# cv2.namedWindow('Instagram') 


# while True: # loop para captura e tratamento dos frames/imagems do video
#   # captura o frame/imagem do video
#     ret, img = cap.read()


#     ret = cv2.GaussianBlur(img, (13, 13), 5, 0)
#     cv2.imshow('lala', ret)
  


#     cv2.imshow('Instagram', img) # exibe o frame/imagem

#     k = cv2.waitKey(20) & 0xFF # armazena o que foi digitado no teclado

#     if k == 27: # sai se pressionado 'esc'
#         break

# cap.release() # desliga o video
# cv2.destroyAllWindows() 

import numpy as np
import cv2 as cv

img = cv.imread('baboon.png') #original
img2 = img.copy() #copia para img modificada
img3 = img.copy()

img4 = img.copy()
corModificadora = [255, 0, 0]

# img5 = cv.imread('bolinhas.png') #original
# img6 = img5.copy()

img7 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img8 = img7.copy()
k = 200

img9 = img.copy()


print(img.shape) #exibe informações de dimensões e nro de canais

print(img7.shape)

for i in range(img.shape[0]): #percorre linhas
	for j in range(img.shape[1]): #percorre colunas
		media = img.item(i,j,0) * 0.333 + img.item(i,j,1) * 0.333 + img.item(i,j,2) * 0.3333
		img2.itemset((i,j,0),media) # canal B
		img2.itemset((i,j,1),media) # canal G
		img2.itemset((i,j,2),media) # canal R

		mediaPond = img.item(i,j,0) * 0.07 + img.item(i,j,1) * 0.71 + img.item(i,j,2) * 0.21
		img3.itemset((i,j,0),mediaPond) # canal B
		img3.itemset((i,j,1),mediaPond) # canal G
		img3.itemset((i,j,2),mediaPond) # canal R

		B = img.item(i,j,0) | corModificadora[0]
		G = img.item(i,j,1) | corModificadora[1]
		R = img.item(i,j,2) | corModificadora[2]
		img4.itemset((i,j,0),B) # canal B
		img4.itemset((i,j,1),G) # canal G
		img4.itemset((i,j,2),R) # canal R

		# img6.itemset((i,j,0),img5.item(i,j,0)^255) # canal B
		# img6.itemset((i,j,1),img5.item(i,j,1)^255) # canal G
		# img6.itemset((i,j,2),img5.item(i,j,2)^255) # canal R

		if img7.item(i,j) < k:
			img8.itemset((i,j),0)
		else:
			img8.itemset((i,j),255)
		
		#"color ramp"
		if img7.item(i,j) < 100:
			img9.itemset((i,j,0),255)
			img9.itemset((i,j,1),255)
			img9.itemset((i,j,2),0)
		elif img7.item(i,j) < 150:
			img9.itemset((i,j,0),255)
			img9.itemset((i,j,1),0)
			img9.itemset((i,j,2),255)
		else:
			img9.itemset((i,j,0),0)
			img9.itemset((i,j,1),255)
			img9.itemset((i,j,2),255)





cv.imshow("Original",img)
#cv.imshow("Grayscale - Média Aritmética",img2)
#cv.imshow("Grayscale - Média Ponderada",img3)
cv.imshow("Imagem colorizada",img4)
# cv.imshow("Imagem invertida",img6)
# cv.imshow("Imagem Grayscale - OpenCV",img7)
#cv.imshow("Imagem Binarizada",img8)
# cv.imshow("Imagem Color Ramp",img9)

cv.waitKey(0)
cv.destroyAllWindows()