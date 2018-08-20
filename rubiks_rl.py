from keras.models import Sequential
import copy

class cube:
	def __init__(self, state):
		self.state = state

	# face: F = 0, R = 1, B = 2, L = 3, U = 4, D = 5; prime: True, False
	def move(self, face, prime):
		rep = copy.deepcopy(self.state)

		# convoluted methodology by which we rotate a face of the cube
		if face == 0:
			if prime == True:
				# rotated face
				self.state[0][0] = rep[0][1]
				self.state[0][1] = rep[0][2]
				self.state[0][2] = rep[0][3]
				self.state[0][3] = rep[0][0]
				# right face (rel rot)
				self.state[1][0] = rep[5][3]
				self.state[1][3] = rep[5][2]
				# bottom face (rel rot)
				self.state[5][3] = rep[3][2]
				self.state[5][2] = rep[3][1]
				# left face (rel rot)
				self.state[3][2] = rep[4][3]
				self.state[3][1] = rep[4][2]
				# upper face (rel rot)
				self.state[4][3] = rep[1][0]
				self.state[4][2] = rep[1][3]
			else:
				# rotated face
				self.state[0][0] = rep[0][3]
				self.state[0][1] = rep[0][0]
				self.state[0][2] = rep[0][1]
				self.state[0][3] = rep[0][2]
				# right face (rel rot)
				self.state[1][0] = rep[4][3]
				self.state[1][3] = rep[4][2]
				# upper face (rel rot)
				self.state[4][3] = rep[3][2]
				self.state[4][2] = rep[3][1]
				# left face (rel rot)
				self.state[3][2] = rep[5][3]
				self.state[3][1] = rep[5][2]
				# bottom face (rel rot)
				self.state[5][3] = rep[1][0]
				self.state[5][2] = rep[1][3]
		elif face == 1:
			if prime == True:
				# rotated face
				self.state[1][0] = rep[1][1]
				self.state[1][1] = rep[1][2]
				self.state[1][2] = rep[1][3]
				self.state[1][3] = rep[1][0]
				# right face (rel rot)
				self.state[2][0] = rep[5][0]
				self.state[2][3] = rep[5][3]
				# bottom face (rel rot)
				self.state[5][0] = rep[0][2]
				self.state[5][3] = rep[0][1]
				# left face (rel rot)
				self.state[0][2] = rep[4][2]
				self.state[0][1] = rep[4][1]
				# upper face (rel rot)
				self.state[4][2] = rep[2][0]
				self.state[4][1] = rep[2][3]
			else:
				# rotated face
				self.state[1][0] = rep[1][3]
				self.state[1][1] = rep[1][0]
				self.state[1][2] = rep[1][1]
				self.state[1][3] = rep[1][2]
				# right face (rel rot)
				self.state[2][0] = rep[4][2]
				self.state[2][3] = rep[4][1]
				# upper face (rel rot)
				self.state[4][2] = rep[0][2]
				self.state[4][1] = rep[0][1]
				# left face (rel rot)
				self.state[0][2] = rep[5][0]
				self.state[0][1] = rep[5][3]
				# bottom face (rel rot)
				self.state[5][0] = rep[2][0]
				self.state[5][3] = rep[2][3]

	# for 'num' times, make random moves in order to scramble the cube
	def scramble(self, num):
		pass

class nn:
	def __init__(self):
		pass

	def get_model():
		pass

	__call__ = get_model()

if __name__ == '__main__':
	c = cube([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19],[20,21,22,23]]) # default arrangement, with each sub-list (face) being in the same order as is used for cube.move
