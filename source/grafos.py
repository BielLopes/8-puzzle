from itertools import permutations
import time
import json
import math

def compare(objetivo, teste, n):
	for i in range(n):
		if objetivo[i] < teste[i]:
			return -1
		if objetivo[i] > teste[i]:
			return 1

	return 0


def busca_binaria(lista, objetivo, n):
	i , j, m, comp = 0, 0, 0, 0
	j = len(lista)
	while True:
		
		m = int((i+j)/2)
		comp = compare(objetivo, lista[m], n)

		if (comp == 0):
			return m
		elif (comp < 0):
			j = m
		else:
			i = m

		if (i == j):
			break

	return -1

class EightPuzzle(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], cor=0):
		self.state = state
		self.switch = state.index(0)
		self.index = index
		self.cor = cor
		"""
			0-> branco
			1-> cinza
			2-> preto
		"""

	def indexes(self, lista, parent, n):
		movs = self.moviments()
		#print(len(movs))
		self.index = []
		for mov in  movs:
			#new = deepcopy(self.state) 
			new = list(self.state) 
			if mov == 0:
				new[self.switch], new[self.switch-int(math.sqrt(n))] = new[self.switch-int(math.sqrt(n))], new[self.switch]
				self.index.append([mov, parent, busca_binaria(lista, tuple(new), n)])
			elif mov == 1:
				new[self.switch], new[self.switch+1] = new[self.switch+1], new[self.switch]
				self.index.append([mov, parent, busca_binaria(lista, tuple(new), n)])
			elif mov == 2:
				new[self.switch], new[self.switch+int(math.sqrt(n))] = new[self.switch+int(math.sqrt(n))], new[self.switch]
				self.index.append([mov, parent, busca_binaria(lista, tuple(new), n)])
			elif mov == 3:
				new[self.switch], new[self.switch-1] = new[self.switch-1], new[self.switch]
				self.index.append([mov, parent, busca_binaria(lista, tuple(new), n)])

		#print(len(self.index))


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

def cria_grafo(n):

	permutacoes = list(permutations(range(n)))
	
	states = []
	no = None

	for node in permutacoes:
		no = EightPuzzle(node)
		states.append(no)

	inicio = time.time()
	dicionarios = []
	i = 0

	for estado in  states:

		estado.indexes(permutacoes, i, n) 
		dicionarios.append(estado.__dict__)

		i = i +1
	
	fim = time.time()
	print(dicionarios[0]["index"])
	print("Tempo gasto para gerar a lista: " + str(fim-inicio))

	return dicionarios


def ler_arquivo(grafo, Obj=EightPuzzle,  heristi=None):
	permutacoes = list(permutations(range(9)))
	lista = []
	if not heristi:
		for node in grafo:
			lista.append(Obj(node["state"], node["index"], node["cor"]))
	else:
		for node in grafo:
			lista.append(Obj(node["state"], node["index"], node["cor"], heuristic=heristi))

	print("Tamanho de permutações: "+str(len(permutacoes)))

	return lista, permutacoes

if __name__ == "__main__":
	cria_grafo(9)
