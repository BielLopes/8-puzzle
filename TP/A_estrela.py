import sys
import bisect
import math
from grafos import ler_arquivo
import json
import time

def heuristica(estado):

	value = 0

	for i in range(9):
		if i != estado[i]:
			value = value + 1

	return value


def heuristica_2(estado):
	value = 0
	i = 0
	for point in estado:
		if point != 0:
			value = value + math.floor(math.fabs((point-i)/3)) + int(math.fabs((point-i))%3)
		i = i + 1
	return value



class EightPuzzle_A_star(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], mov=None, cor=0, deep=0, heuristic=heuristica_2):
		self.state = state
		self.index = index
		self.cor = cor
		self.mov = mov
		self.deep = deep
		self.heuristic = heuristic(self.state)
		self.valor = deep + self.heuristic
		#print(self.valor)

	def atualiza_valor(self):	
		self.valor = self.deep + self.heuristic

	def __lt__(self, other):
		return self.valor < other.valor


def test_goal(node):
	goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
	if node.state == goal:
		return True
	else:
		return False

def sortCost(val):
	return val.valor

def A_star(inicial, lista):
	
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
			#if (lista[child[2]].cor == 0) or (lista[child[2]].cor == 1 and lista[child[2]].valor > (node.valor + 1)):
			if (lista[child[2]].cor == 0) :

				lista[child[2]].deep = node.deep + 1
				lista[child[2]].atualiza_valor()
				lista[child[2]].mov = child

				if not test_goal(lista[child[2]]):
					#if (lista[child[2]].cor == 0):
					#	lista[child[2]].cor = 1
					#	bisect.insort(frontier, lista[child[2]])
					i = i + 1
					lista[child[2]].cor = 1
					bisect.insort(frontier, lista[child[2]])
					#else:
						#frontier.sort(key=sortCost, reverse=False)
				else:
					print("Nós expandidos: " + str(i+1))
					goal_state = lista[child[2]]
					return goal_state, frontier

		node.cor = 2
		frontier.remove(node)
		#print(node.valor)
 
def gera_caminho(inicial_state, grafo, heurist):


	lista, permutaciones = ler_arquivo(Obj=EightPuzzle_A_star, grafo=grafo, heristi=heurist)
	goal_state = None
	indice = permutaciones.index(inicial_state)
	inicial = lista[indice]

	inicio = time.time()
	goal_state, frontier = A_star(inicial, lista)

	node = goal_state
	caminho = []
	deep = 1
	while node.state != inicial_state:
		if node.mov[0] == 3:
			move = "Esquerda"
		elif node.mov[0] == 2:
			move = "Baixo"
		if node.mov[0] == 1:
			move = "Direita"
		elif node.mov[0] == 0:
			move = "Cima"
		caminho.insert(0,move)
		node = lista[node.mov[1]]
		if (node.state != inicial_state):
			deep = deep + 1

	final = time.time()
	print("Tempo gasto: "+str(final-inicio))

	print("Profundidade: "+str(deep))
	print("Alocação de memória do A* da Fronteira: "+str(sys.getsizeof(frontier)))
	

	print(caminho)
