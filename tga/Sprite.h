#pragma once

//GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "Shader.h"

class Sprite
{
public:
	Sprite() {}
	~Sprite() {}

	void initialize(int texID, int imgWidth, int imgHeight, int nAnimations = 1, int nFrames = 1);
	inline void setPosition(glm::vec3 pos) { this->position = pos; }
	inline void moveRight() { this->position.x += speed.x; }
	inline void moveLeft() { this->position.x -= speed.x; }
	inline void moveUp() { this->position.y += speed.y; }
	inline void moveDown() { this->position.y -= speed.y; }
	
	inline void setScale(glm::vec3 dimensions) { this->dimensions = glm::vec3(dimensions.x/nFrames, dimensions.y/nAnimations, dimensions.z); }
	inline void setIAnimation(int iAnimation) { this->iAnimation = iAnimation; }
	void setShader(Shader* shader);
	void draw();
	void update();

	void getAABB(glm::vec2& min, glm::vec2& max);


protected:
	GLuint VAO; //identificador do Vertex Array Object - Geometria
	glm::vec3 position;
	glm::vec3 dimensions;
	GLuint texID;
	int imgWidth, imgHeight;
	int nAnimations, nFrames;
	int iFrame, iAnimation;
	float dx, dy;
	glm::vec2 speed;


	Shader* shader;
};

