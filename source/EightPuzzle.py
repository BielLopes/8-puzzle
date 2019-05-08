class EightPuzzle(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, parent, cost):
		self.state = state
		self.switch = state.index(0)
		self.parent = parent
		self.cost = cost

	def childs(self):
		childs = []
		movs = self.moviments()
		new_state_1 = self.state.copy()
		new_state_2 = self.state.copy()
		new_state_3 = self.state.copy()
		new_state_4 = self.state.copy()
		for mov in  movs:
			if mov == 0:
				new_state_1[self.switch], new_state_1[self.switch-3] = new_state_1[self.switch-3], new_state_1[self.switch]
				childs.append(EightPuzzle(new_state_1, self, self.cost+1))
			elif mov == 1:
				new_state_2[self.switch], new_state_2[self.switch+1] = new_state_2[self.switch+1], new_state_2[self.switch]
				childs.append(EightPuzzle(new_state_2, self, self.cost+1))
			elif mov == 2:
				new_state_3[self.switch], new_state_3[self.switch+3] = new_state_3[self.switch+3], new_state_3[self.switch]
				childs.append(EightPuzzle(new_state_3, self, self.cost+1))
			elif mov == 3:
				new_state_4[self.switch], new_state_4[self.switch-1] = new_state_4[self.switch-1], new_state_4[self.switch]
				childs.append(EightPuzzle(new_state_4, self, self.cost+1))
		return childs


	def moviments(self):
		moves = []
		# move 0 -> cima
		# move 1 -> direita
		# move 2 -> baixo
		# move 3 -> esquerda
		if self.switch == 4:
			moves = [0, 1, 2, 3]
		elif self.switch == 0:
			moves = [1, 2]
		elif self.switch == 1:
			moves = [1, 2, 3]
		elif self.switch == 2:
			moves = [2, 3]
		elif self.switch == 3:
			moves = [0, 1, 2]
		elif self.switch == 5:
			moves = [0, 2, 3]
		elif self.switch == 6:
			moves = [0, 1]
		elif self.switch == 7:
			moves = [0, 1, 3]
		elif self.switch == 8:
			moves = [0, 3] 
		return moves