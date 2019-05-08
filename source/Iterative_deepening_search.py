import sys
import bisect
from grafos import ler_arquivo
import time
import json

class EightPuzzleIDS(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], move=None, cor=0, deep=0):
		self.state = state
		self.index = index
		self.cor = cor
		self.move = move
		self.deep = deep

	def __lt__(self, other):
		return self.deep > other.deep

def test_goal(node):
	goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
	if node.state == goal:
		return True
	else:
		return False

def resetar_lista(lista):
	for node in lista:
		node.cor = 0
		node.deep = 0
		#node.move = []

def IDS(inicial, lista):
	
	frontier = []
	goal_state = None

	if test_goal(inicial):
		return 0, inicial, frontier

	deep = 1
	i = 0
	while True:
		inicial.cor = 1
		frontier.append(inicial)

		while frontier != []:

			node = frontier[0]			
			childs = node.index
			for child in childs:

				if (lista[child[2]].cor == 0) and ((node.deep < deep) or test_goal(lista[child[2]])) and (deep <= 31):
					lista[child[2]].deep = node.deep + 1
					lista[child[2]].move = child
					if not test_goal(lista[child[2]]):
						i = i + 1
						lista[child[2]].cor = 1
						bisect.insort(frontier, lista[child[2]])
					else:
						print("Nós expandidos: " + str(i+1))
						goal_state = lista[child[2]]
						print("To aqui!")
						return goal_state, frontier

			#print(node.state)
			node.cor = 2
			frontier.remove(node)

		frontier = []
		resetar_lista(lista)
		deep = deep + 1

def gera_caminho(inicial_state, grafo):

	lista, permutaciones = ler_arquivo(Obj=EightPuzzleIDS, grafo=grafo)
	#print("To aqui!")
	goal_state = None
	indice = permutaciones.index(inicial_state)
	inicial = lista[indice]

	#inicio = time.time()
	inicio = time.time()
	goal_state, frontier = IDS(inicial, lista)
	#fim = time.time()

	#print("Tempo de execuçaõ: "+str(fim-inicio))
	print("Alocação de memória do IDS da Fronteira: "+str(sys.getsizeof(frontier)))

	node = goal_state
	caminho = []
	#print(node.state)
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

	print("Profundidade: "+str(deep))
	print(caminho)
	final = time.time()
	print("Tempo gasto: "+str(final-inicio))

if __name__ == "__main__":
	#grafo = cria_grafo(9)
	arquivo = open('lista.json', 'r')
	grafo = json.load(arquivo)
	gera_caminho((8, 6, 7, 2, 5, 4, 3, 0, 1), grafo)