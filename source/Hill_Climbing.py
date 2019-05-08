import sys
import random
from grafos import ler_arquivo
import json
import time
import math


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


class EightPuzzleHILL(object):
	"""docstring for EightPuzzle"""
	def __init__(self, state, index=[], mov=None, cor=0, heuristic=heuristica):
		self.state = state
		self.index = index
		self.cor = cor
		self.mov = mov
		self.valor = heuristic(self.state)

	def __lt__(self, other):
		return self.valor < other.valor

def test_goal(node):
	goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
	if node.state == goal:
		return True
	else:
		return False

def igual(vetor):

	for valor in vetor:
		for val in vetor:
			if val != valor:
				return False

	return True

def Hill_Climbing(inicial, lista):
	
	goal_state = None

	if test_goal(inicial):
		return 0, inicial

	node = inicial
	i = 0

	while True:
		
		childs = node.index
		proximo = []
		for child in childs:
			print(child)
			lista[child[2]].mov = child
			if not test_goal(lista[child[2]]):
				
				proximo.append(lista[child[2]].valor)
			else:
				goal_state = lista[child[2]]
				return goal_state

		#print(len(proximo))
			
		if igual(proximo):
			place = random.randint(0, len(proximo)-1)
		else:	
			place = proximo.index(min(proximo))

		#print(proximo)

		node = lista[childs[place][2]]
		#print(childs[place][2])

		i = i + 1
		if i > 300000:
			print("Deu ruin")
			return None


def gera_caminho(inicial_state, grafo, heurist):

	lista, permutaciones = ler_arquivo(Obj=EightPuzzleHILL, grafo=grafo, heristi=heurist)
	goal_state = None
	indice = permutaciones.index(inicial_state)
	inicial = lista[indice]

	inicio = time.time()
	while goal_state == None:
		goal_state = Hill_Climbing(inicial, lista)

	#print("Alocação de memória do Hill-Climbing da Fronteira: "+str(sys.getsizeof(frontier)))

	node = goal_state
	caminho = []
	deep = 1

	while node.state != list(inicial_state):
		print(node.mov)
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

		if (node.state != list(inicial_state)):
			deep = deep + 1

	final = time.time()
	print("Tempo gasto: "+str(final-inicio))
	print("Profundidade: "+str(deep))
	print(caminho)


if __name__ == "__main__":
	#grafo = cria_grafo(9)
	arquivo = open('lista.json', 'r')
	grafo = json.load(arquivo)
	gera_caminho((1, 2, 3, 4, 0, 5, 7, 8, 6), grafo, heurist=heuristica_2)