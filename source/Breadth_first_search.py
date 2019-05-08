import sys
from grafos import ler_arquivo, cria_grafo
import json
import time


class EightPuzzleBFS(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], move=None, cor=0):
		self.state = state
		self.index = index
		self.cor = cor
		self.move = move
		"""
			0-> branco
			1-> cinza
			2-> preto
		"""


def test_goal(node):
	goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
	if node.state == goal:
		return True
	else:
		return False


def BFS(inicial, lista):
	
	goal_state = None
	frontier = []

	if test_goal(inicial):
		return 0, lista, frontier

	frontier.append(inicial.index[0][1])
	new_frontier = []
	deep = 1

	i = 0
	while True:
		for node in frontier:
			#print(len(frontier))
			childs = lista[node].index
			for child in childs:
				#print("ponto: " + str(child[2]))
				if lista[child[2]].cor == 0:
					lista[child[2]].move = child
					#print(lista[child[2]])
					if not test_goal(lista[child[2]]):
						i = i + 1
						lista[child[2]].cor = 1
						new_frontier.append(child[2])
					else:
						print("Nós expandidos: " + str(i+1))
						
						goal_state = lista[child[2]]
						return deep, goal_state, frontier

			lista[node].cor = 2

		#print("Fronteira: "+str(len(frontier)))
		#print("Profundidade: "+str(deep))
		#print(frontier)
		#print(new_frontier)
		frontier = new_frontier.copy()
		new_frontier.clear()
		deep = deep + 1

		#print("Profundidade: "+str(deep))

def gera_caminho(inicial_state, grafo):

	lista, permutaciones = ler_arquivo(Obj=EightPuzzleBFS, grafo=grafo)
	goal_state = None
	indice = permutaciones.index(inicial_state)
	inicial = lista[indice]

	inicio = time.time()
	deep, goal_state, frontier = BFS(inicial, lista)
	fim = time.time()

	print("Tempo de execuçaõ: "+str(fim-inicio))
	print("Profundidade: "+str(deep))
	print("Alocação de memória do BFS da Fronteira: "+str(sys.getsizeof(frontier)))

	node = goal_state
	caminho = []
	while node.state != inicial_state:
		#print(node.move)
		if node.move[0] == 3:
			move = "Esquerda"
		elif node.move[0] == 2:
			move = "Baixo"
		if node.move[0] == 1:
			move = "Direita"
		elif node.move[0] == 0:
			move = "Cima"
		caminho.insert(0,move)
		node = lista[node.move[1]]

	print(caminho)

if __name__ == "__main__":
	#grafo = cria_grafo(9)
	arquivo = open('lista.json', 'r')
	grafo = json.load(arquivo)
	gera_caminho((8, 6, 7, 2, 5, 4, 3, 0, 1), grafo)
