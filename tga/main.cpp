#include <iostream>
#include <string>
#include <assert.h>
#include <thread>
#include <unistd.h>

using namespace std;

// GLAD
#include <glad/glad.h>

// GLFW
#include <GLFW/glfw3.h>

// GLM  
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

// STB IMAGE
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

// Classe shader
#include "Shader.h"

// Classe sprite
#include "Sprite.h"

// Callback teclado
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode);

// Funcoes
int setupGeometry();
int setupSprite();

GLuint generateTexture(string filePath, int &width, int &height);
bool testCollision(Sprite spr1, Sprite spr2);

// Tamanho da janela 800x600
const GLuint WIDTH = 800, HEIGHT = 600;

// Personagem
Sprite character;

// Obstaculo
Sprite obstaculo;

int main()
{	

	// Initialize GLFW
	glfwInit();

	// Versao OpenGL
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// MacOS
	#ifdef __APPLE__
		glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
	#endif

	// Cria a janela
	GLFWwindow* window = glfwCreateWindow(WIDTH, HEIGHT, "TGA - Lucas Schneider", nullptr, nullptr);
	glfwMakeContextCurrent(window);

	// Callback da janela
	glfwSetKeyCallback(window, key_callback);

	// GLAD: carrega todos os ponteiros e funcoes do OpenGL
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
	{
		std::cout << "Failed to initialize GLAD" << std::endl;
	}

	// Shaders
	Shader shader("vert.vs", "frag.fs");

	int bgwidth, bgheight;
	int charwidth, charheight;

	// Carrega as texturas
	GLuint texID = generateTexture("textures/bg/bg-ocean.png", bgwidth, bgheight);
	GLuint texID2 = generateTexture("textures/sprite-sheets/octopus-walk.png", charwidth, charheight);
	GLuint texID3 = generateTexture("textures/sprite-sheets/shark-walk.png", charwidth, charheight);

	// Initialize sprite do personagem 
	character.initialize(texID2, charwidth, charheight, 1, 6);
	character.setShader(&shader);
	character.setPosition(glm::vec3(200, 210, 0));
	character.setScale(glm::vec3(charwidth*2, charheight*2, 1));

	// Initialize sprite do obstaculo
	obstaculo.initialize(texID3, charwidth, charheight, 1, 4);
	obstaculo.setShader(&shader);
	obstaculo.setPosition(glm::vec3(400, 410, 0));
	obstaculo.setScale(glm::vec3(charwidth*2, charheight*2, 1));

	// Initialize sprite do background
	Sprite background;
	background.initialize(texID, bgwidth, bgheight);
	background.setShader(&shader);
	background.setPosition(glm::vec3(400, 300, 0));
	background.setScale(glm::vec3(bgwidth*0.56, bgheight*0.56, 1));
	
	glUseProgram(shader.ID);

	// Correcao ortho
	glm::mat4 projection = glm::ortho(0.0, 800.0, 0.0, 600.0, -1.0, 1.0);
	GLint projLoc = glGetUniformLocation(shader.ID, "projection");
	glUniformMatrix4fv(projLoc, 1, false, glm::value_ptr(projection));

	// Buffer de textura
	glActiveTexture(GL_TEXTURE0);

	// Profundidade
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_ALWAYS);

	// Transparencia na texture do personagem
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

	// Game
	while (!glfwWindowShouldClose(window))
	{

		// Checa input
		glfwPollEvents();

		// Dimencoes janela
		int width, height;
		glfwGetFramebufferSize(window, &width, &height);
		glViewport(0, 0, width, height);

		// Buffer de cor
		glClearColor(0.8f, 0.8f, 0.8f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glLineWidth(1);
		glPointSize(5);

		background.update();
		background.draw();

		character.update();
		character.draw();

		obstaculo.update();
		obstaculo.draw();

		glBindVertexArray(0);

		// Troca os buffers da tela
		glfwSwapBuffers(window);
	}

	// Finaliza GLFW
	glfwTerminate();
	return 0;

}

// Callback teclado
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode) {
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GL_TRUE);

    // Verifica se há colisão entre o personagem e o obstáculo
    if (testCollision(character, obstaculo)) {
        // Se houver colisão, não permite que o personagem se mova naquela direção
        if (key == GLFW_KEY_D || key == GLFW_KEY_RIGHT)
            character.moveLeft();
			character.moveDown();
        if (key == GLFW_KEY_A || key == GLFW_KEY_LEFT)
            character.moveRight();
			character.moveDown();
        if (key == GLFW_KEY_W || key == GLFW_KEY_UP)
            character.moveDown();
			 character.moveLeft();
        if (key == GLFW_KEY_S || key == GLFW_KEY_DOWN)
            character.moveUp();
			 character.moveLeft();
    } else {
        // Se não houver colisão, permite que o personagem se mova normalmente
        if (key == GLFW_KEY_D || key == GLFW_KEY_RIGHT)
            character.moveRight();
        if (key == GLFW_KEY_A || key == GLFW_KEY_LEFT)
            character.moveLeft();
        if (key == GLFW_KEY_W || key == GLFW_KEY_UP)
            character.moveUp();
        if (key == GLFW_KEY_S || key == GLFW_KEY_DOWN)
            character.moveDown();
    }
}


// Config geometry
int setupGeometry() {

	GLfloat vertices[] = {
		//x   	y     	z   	r    	g    	b     	s     	t
		-0.5,	-0.5,	0.0,	1.0,	0.0,	0.0,	0.0,	0.0,
		 0.5,	-0.5,	0.0,	0.0,	1.0,	0.0,	1.0,	0.0,
		 0.0,	0.5,	0.0,	0.0,	0.0,	1.0,	0.5,	1.0 
	};

	GLuint VBO, VAO;

	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

	glGenVertexArrays(1, &VAO);
	glBindVertexArray(VAO);

	// Posicao
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	// Cor
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(1);

	// Posicao texture
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(6 * sizeof(GLfloat)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0); 

	glBindVertexArray(0); 

	return VAO;
}

// Config sprite
int setupSprite() {

	GLfloat vertices[] = {
		//x		y     	z    	r    	g    	b     	s     	t
		//T1
		-0.5,	0.5,	0.0,	1.0,	0.0,	0.0,	0.0,	1.0,
		-0.5, 	-0.5, 	0.0, 	0.0, 	1.0, 	0.0, 	0.0, 	0.0, 
		 0.5,  	0.5, 	0.0, 	0.0, 	0.0, 	1.0, 	1.0, 	1.0,
		 //T2
		-0.5, 	-0.5, 	0.0, 	0.0, 	1.0,	0.0, 	0.0, 	0.0,
		 0.5,  	0.5, 	0.0, 	0.0, 	0.0, 	1.0, 	1.0, 	1.0,
		 0.5, 	-0.5, 	0.0, 	0.0, 	1.0, 	0.0, 	1.0, 	0.0 
	};

	GLuint VBO, VAO;

	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

	glGenVertexArrays(1, &VAO);
	glBindVertexArray(VAO);

	// Posicao
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	// Cor
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(1);

	// Posicao texture
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(6 * sizeof(GLfloat)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);

	glBindVertexArray(0);

	return VAO;
}

// Cria as texturas
GLuint generateTexture(string filePath, int &width, int &height) {
	GLuint texID;

	// Gera o identificador da textura me memoria 
	glGenTextures(1, &texID);
	glBindTexture(GL_TEXTURE_2D, texID);

	// Definindo o metodo de wrapping e de filtering
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

	// Carregando a imagen da textura
	int nrChannels;
	unsigned char* data = stbi_load(filePath.c_str(), &width, &height, &nrChannels, 0);

	// Manda para OpenGL armazenar a textura e gerar o mipmap
	if (data) {	
		if (nrChannels == 3) {
			// jpg, bmp
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
		} else {
			// png
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
		}
		glGenerateMipmap(GL_TEXTURE_2D);
	} else {
		std::cout << "Failed to load texture" << std::endl;
	}

	stbi_image_free(data);
	glBindTexture(GL_TEXTURE_2D, 0);

	return texID;
}

// Colisao (NOT USED)
bool testCollision(Sprite spr1, Sprite spr2) {
	glm::vec2 min1, min2, max1, max2;
	spr1.getAABB(min1, max1);
	spr2.getAABB(min2, max2);

	// Verifica se há interseção nas coordenadas X
    bool overlapX = max1.x >= min2.x && max2.x >= min1.x;
    // Verifica se há interseção nas coordenadas Y
    bool overlapY = max1.y >= min2.y && max2.y >= min1.y;

    // Se houver interseção nas coordenadas X e Y, os sprites colidiram
    return overlapX && overlapY;
}
