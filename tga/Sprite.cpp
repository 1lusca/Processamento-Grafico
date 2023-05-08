#include "Sprite.h"

void Sprite::initialize(int texID, int imgWidth, int imgHeight, int nAnimations, int nFrames) {
	this->texID = texID;
	this->imgWidth = imgWidth;
	this->imgHeight = imgHeight;
	this->nAnimations = nAnimations;
	this->nFrames = nFrames;

	speed.x = 8.0;
	speed.y = 8.0;

	dx = 1.0 / float(nFrames);
	dy = 1.0 / float(nAnimations);

	time = 0.0f;
	frameTime = 8;

	GLfloat vertices[] = {
		//x		y     	z    	r    	g    	b     	s     	t
		//T1
		-0.5,	0.5,	0.0,	1.0,	0.0,	0.0,	0.0,	dy,
		-0.5,	-0.5,	0.0,	0.0,	1.0,	0.0,	0.0,	0.0,
		 0.5,	0.5,	0.0,	0.0,	0.0,	1.0,	dx,		dy,
		 //T2
		-0.5,	-0.5,	0.0,	0.0,	1.0,	0.0,	0.0,	0.0, 
		 0.5,	0.5,	0.0,	0.0,	0.0,	1.0,	dx,		dy,
		 0.5,	-0.5,	0.0,	0.0,	1.0,	0.0,	dx,		0.0 
	};

	GLuint VBO;

	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

	glGenVertexArrays(1, &VAO);
	glBindVertexArray(VAO);

	// posicao
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	// cor
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(1);

	// posicao texture
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), (GLvoid*)(6 * sizeof(GLfloat)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);

	glBindVertexArray(0);
}

void Sprite::setShader(Shader* shader) {
	this->shader = shader; 
	shader->use();
}

void Sprite::draw() {
	glBindVertexArray(VAO);
	glBindTexture(GL_TEXTURE_2D, texID);
	glDrawArrays(GL_TRIANGLES, 0, 6);
}

void Sprite::update() {
	glm::mat4 model = glm::mat4(1);
	model = glm::translate(model, position);
	model = glm::scale(model, dimensions);
	int modelLoc = glGetUniformLocation(shader->ID, "model");
	glUniformMatrix4fv(modelLoc, 1, false, glm::value_ptr(model));

	time += 1.0f;
	iFrame = int(time / frameTime) % nFrames;

	float offsetx = iFrame * dx;
	float offsety = iAnimation * dy;
	shader->setVec2("offsets", offsetx, offsety);
}

void Sprite::getAABB(glm::vec2& min, glm::vec2& max) {
	min.x = position.x - dimensions.x / 2.0;
	max.x = position.x + dimensions.x / 2.0;

	min.y = position.y - dimensions.y / 2.0;
	max.y = position.y + dimensions.y / 2.0;
}
