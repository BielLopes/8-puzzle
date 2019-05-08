import sys
import bisect
from grafos import ler_arquivo
import json
import time

class EightPuzzleUCS(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], move=None, cor=0, cost=0):
		self.state = state
		self.index = index
		self.cor = cor
		self.move = move
		self.cost = cost

	def __lt__(self, other):
		return self.cost < other.cost

def test_goal(node):
	goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
	if node.state == goal:
		return True
	else:
		return False


def sortCost(val):
	return val.cost

def UCS(inicial, lista):
	
	frontier = []
	goal_state = None

	if test_goal(inicial):
		return inicial, frontier

	frontier.append(inicial)

	i = 0
	while True:		
		node = frontier[0]	

		childs = node.index
		for child in childs:

			if (lista[child[2]].cor == 0):
				lista[child[2]].move = child
				lista[child[2]].cost = node.cost + 1
				if not test_goal(lista[child[2]]):
					i = i + 1
					lista[child[2]].cor = 1
					bisect.insort(frontier, lista[child[2]])
					
				else:
					print("Nós expandidos: " + str(i+1))
					goal_state = lista[child[2]]
					return goal_state, frontier

		node.cor = 2
		frontier.remove(node)			
		#print(node.cost)
 
def gera_caminho(inicial_state, grafo):


	lista, permutaciones = ler_arquivo(Obj=EightPuzzleUCS, grafo=grafo)
	goal_state = None
	indice = permutaciones.index(inicial_state)
	inicial = lista[indice]

	inicio = time.time()
	goal_state, frontier = UCS(inicial, lista)

	node = goal_state
	caminho = []
	deep = 1
	while node.state != inicial_state:
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
		if node.state != inicial_state:
			deep = deep + 1
	
	final = time.time()
	print("Profundidade: "+str(deep))
	print("Tempo gasto: "+str(final-inicio))
	print("Alocação de memória do UCS da Fronteira: "+str(sys.getsizeof(frontier)))
	

	print(caminho)


if __name__ == "__main__":
	#grafo = cria_grafo(9)
	arquivo = open('lista.json', 'r')
	grafo = json.load(arquivo)
	gera_caminho((8, 6, 7, 2, 5, 4, 3, 0, 1), grafo)