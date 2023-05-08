
#include <iostream>
#include <string>
#include <assert.h>
#include <cmath>

using namespace std;

// GLAD
#include <glad/glad.h>

// GLFW
#include <GLFW/glfw3.h>

// GLM  
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

//Classe shader
#include "Shader.h"

// ProtÛtipo da funÁ„o de callback de teclado
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode);

// ProtÛtipos das funÁıes
int setupGeometry();

// Dimensões da janela (pode ser alterado em tempo de execução)
const GLuint WIDTH = 800, HEIGHT = 600;

int main()
{
	// Inicialização da GLFW
	glfwInit();

	//Muita atenção aqui: alguns ambientes não aceitam essas configurações
	//Você deve adaptar para a versão do OpenGL suportada por sua placa
	//Sugestão: comente essas linhas de código para desobrir a versão e
	//depois atualize (por exemplo: 4.5 com 4 e 5)
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	//Essencial para computadores da Apple
	#ifdef __APPLE__
		glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
	#endif

	// CriaÁ„o da janela GLFW
	GLFWwindow* window = glfwCreateWindow(WIDTH, HEIGHT, "Lucas Schneider - Lista 3 - Exercicio 1", nullptr, nullptr);
	glfwMakeContextCurrent(window);

	// Fazendo o registro da funÁ„o de callback para a janela GLFW
	glfwSetKeyCallback(window, key_callback);

	// GLAD: carrega todos os ponteiros d funÁıes da OpenGL
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
	{
		std::cout << "Failed to initialize GLAD" << std::endl;

	}

	// Obtendo as informaÁıes de vers„o
	const GLubyte* renderer = glGetString(GL_RENDERER); /* get renderer string */
	const GLubyte* version = glGetString(GL_VERSION); /* version as a string */
	cout << "Renderer: " << renderer << endl;
	cout << "OpenGL version supported " << version << endl;

	// Compilando e buildando o programa de shader
	Shader shader("vert.vs", "frag.fs");

	// Gerando um buffer simples, com a geometria de um tri‚ngulo
	GLuint VAO = setupGeometry();
	
	glUseProgram(shader.ID);

	//Matriz de projeÁ„o paralela ortogr·fica
	//glm::mat4 projection = glm::ortho(0.0, 800.0, 600.0, 0.0, -1.0, 1.0);

	glm::mat4 projection = glm::ortho(0.0, 800.0, 0.0, 600.0, -1.0, 1.0);
	GLint projLoc = glGetUniformLocation(shader.ID, "projection");
	glUniformMatrix4fv(projLoc, 1, false, glm::value_ptr(projection));

	// Loop da aplicaÁ„o - "game loop"
	while (!glfwWindowShouldClose(window))
	{
		// Checa se houveram eventos de input (key pressed, mouse moved etc.) e chama as fun��es de callback correspondentes
		glfwPollEvents();
		
		int width, height;
		glfwGetFramebufferSize(window, &width, &height);
		//glViewport(0, 0, width, height);

		// Limpa o buffer de cor
		glClearColor(0.8f, 0.8f, 0.8f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);

		glLineWidth(1);
		glPointSize(5);

		glBindVertexArray(VAO); //Conectando ao buffer de geometria

		// Definindo as dimensıes da viewport com as mesmas dimensıes da janela da aplicaÁ„o
		
		

		glm::mat4 model_1 = glm::mat4(1); //matriz identidade
		model_1 = glm::translate(model_1, glm::vec3(400.0, 300.0, 0.0));
		float angle_1 = glfwGetTime();
		model_1 = glm::rotate(model_1, -angle_1, glm::vec3(0.0, 0.0, 1.0));
		model_1 = glm::scale(model_1, glm::vec3(300.0, 300.0, 1.0));
		GLint modelLoc_1 = glGetUniformLocation(shader.ID, "model");
		glUniformMatrix4fv(modelLoc_1, 1, false, glm::value_ptr(model_1));

		glViewport(400, -300, width, height);
		glDrawArrays(GL_TRIANGLES, 0, 3);




		glm::mat4 model_2 = glm::mat4(1); //matriz identidade
		model_2 = glm::translate(model_2, glm::vec3(400.0, 300.0, 0.0));
		float angle_2 = glfwGetTime();
		model_2 = glm::rotate(model_2, /*glm::radians(90.0f)*/angle_2, glm::vec3(0.0, 0.0, 1.0));
		model_2 = glm::scale(model_2, glm::vec3(300.0, 300.0, 1.0));
		GLint modelLoc_2 = glGetUniformLocation(shader.ID, "model");
		glUniformMatrix4fv(modelLoc_2, 1, false, glm::value_ptr(model_2));

		glViewport(-400, 300, width, height);
		glDrawArrays(GL_TRIANGLES, 0, 3);




		

		glm::mat4 model_3 = glm::mat4(1); //matriz identidade
		model_3 = glm::translate(model_3, glm::vec3(400.0, 300.0, 0.0));
		float angle_3 = glfwGetTime();
		model_3 = glm::rotate(model_3, /*glm::radians(90.0f)*/angle_3, glm::vec3(0.0, 0.0, 1.0));
		model_3 = glm::scale(model_3, glm::vec3(200.0, 200.0, 1.0));
		GLint modelLoc_3 = glGetUniformLocation(shader.ID, "model");
		glUniformMatrix4fv(modelLoc_3, 1, false, glm::value_ptr(model_3));

		glViewport(-400, -300, width, height);
		glDrawArrays(GL_TRIANGLES, 0, 3);

		

		

		glBindVertexArray(0); //Desconectando o buffer de geometria

		// Troca os buffers da tela
		glfwSwapBuffers(window);
	}
	// Pede pra OpenGL desalocar os buffers
	glDeleteVertexArrays(1, &VAO);
	// Finaliza a execuÁ„o da GLFW, limpando os recursos alocados por ela
	glfwTerminate();
	return 0;
}

// FunÁ„o de callback de teclado - sÛ pode ter uma inst‚ncia (deve ser est·tica se
// estiver dentro de uma classe) - … chamada sempre que uma tecla for pressionada
// ou solta via GLFW
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode)
{
	if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
		glfwSetWindowShouldClose(window, GL_TRUE);
}

// Esta funÁ„o est· bastante harcoded - objetivo È criar os buffers que armazenam a 
// geometria de um tri‚ngulo
// Apenas atributo coordenada nos vÈrtices
// 1 VBO com as coordenadas, VAO com apenas 1 ponteiro para atributo
// A funÁ„o retorna o identificador do VAO
int setupGeometry()
{

// 								y
	// 						|
	// 						|
	// 						|
	// 						|
	// ---------------------------------------------- x
	// 						|
	// 						|
	// 						|
	// 						|


	GLfloat vertices[] = {
		//x   	y     	z    	r    	g    	b
		0.0, 	0.25,	0.0, 	0.451, 	0.769, 	0.949, //v0
		-0.25, 	-0.25, 	0.0, 	0.451, 	0.769, 	0.949, //v1
		0.25, 	-0.25,  	0.0, 	0.451, 	0.769, 	0.949,  //v2
	};

	GLuint VBO, VAO;

	//GeraÁ„o do identificador do VBO
	glGenBuffers(1, &VBO);
	//Faz a conex„o (vincula) do buffer como um buffer de array
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	//Envia os dados do array de floats para o buffer da OpenGl
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

	//GeraÁ„o do identificador do VAO (Vertex Array Object)
	glGenVertexArrays(1, &VAO);
	// Vincula (bind) o VAO primeiro, e em seguida  conecta e seta o(s) buffer(s) de vÈrtices
	// e os ponteiros para os atributos 
	glBindVertexArray(VAO);
	//Para cada atributo do vertice, criamos um "AttribPointer" (ponteiro para o atributo), indicando: 
	// LocalizaÁ„o no shader * (a localizaÁ„o dos atributos devem ser correspondentes no layout especificado no vertex shader)
	// Numero de valores que o atributo tem (por ex, 3 coordenadas xyz) 
	// Tipo do dado
	// Se est· normalizado (entre zero e um)
	// Tamanho em bytes 
	// Deslocamento a partir do byte zero 

	//Atributo posiÁ„o
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	//Atributo cor
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(1);

	// Observe que isso È permitido, a chamada para glVertexAttribPointer registrou o VBO como o objeto de buffer de vÈrtice 
	// atualmente vinculado - para que depois possamos desvincular com seguranÁa
	glBindBuffer(GL_ARRAY_BUFFER, 0); 

	// Desvincula o VAO (È uma boa pr·tica desvincular qualquer buffer ou array para evitar bugs medonhos)
	glBindVertexArray(0); 

	return VAO;
}

