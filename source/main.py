from A_estrela import gera_caminho as caminho_A_star, EightPuzzle_A_star, A_star
from Breadth_first_search import gera_caminho as caminho_Breadth_firt_search, EightPuzzleBFS, BFS, test_goal
from Greedy import gera_caminho as caminho_Greedy, EightPuzzleGREEDY, Greedy
from Hill_Climbing import gera_caminho as caminho_Hill_Climbing, EightPuzzleHILL, heuristica, heuristica_2, Hill_Climbing
from Iterative_deepening_search import gera_caminho as caminho_Interative_deep_search, EightPuzzleIDS, IDS, resetar_lista
from Uniform_coust_search import gera_caminho as caminho_Uniform_coust_search, EightPuzzleUCS, UCS
from grafos import EightPuzzle, cria_grafo, ler_arquivo, compare, busca_binaria
import time
import json

def main():

	print("##########################################################")
	print("@ TP de Inteligência Artificial de Gabriel Lopes Machado @")
	print("##########################################################")

	print("Primeiramente entre com o grau do puzzle a ser resolvido:")
	print("Ex: ")
	print("8 -> eigth puzzle")
	print("15 -> fifteen puzzle (Garanta que o seu computador vai suportar a mamória necessária)")

	print("Obs: não trato exeção de input incorretos!")

	n = 9
	estados = None
	choice = 1
	while n > 0:

		del estados
		print("(-1 -> sair)")
		n = int(input('Entre com n: '))
		n = n + 1

		print("\n\n\n\n\n\n\n\n\n Gerando o grafo de pesquisa (isso pode demorar alguns segundos)")
		estados = cria_grafo(n)

#		for no in estados:
#			print("Nó em:" + str(no) + " com index de tamanho: " + str(len(no["index"])))
		while True:

			intput = []

			print("(-1 -> sair)")
			for i in range(n):
				intput.append(int(input('Entre com a posição '+str(i)+': ')))
				
				if (intput[i] <= -1):
					break
			if -1 in intput:
				break

			intput = tuple(intput)
			print(intput)

			while  choice > 0:

				print("(-1 -> sair)")
				print("(1 -> BFS)")
				print("(2 -> IDS)")
				print("(3 -> UCS)")
				print("(4 -> A*)")
				print("(5 -> Greedy)")
				print("(6 -> Hill Climbing)")

				choice = int(input('Escolha o algorítimo: '))
				if choice <= -1:
					choice = 1
					break
				
				if choice == 1:
					caminho_Breadth_firt_search(intput, estados)
				elif choice == 2:
					caminho_Interative_deep_search(intput, estados)
				elif choice == 3:
					caminho_Uniform_coust_search(intput, estados)
				elif choice >= 4:
					print("(1 -> Heuristica 1: nº quadrados fora de lugar)")
					print("(2 -> Heuristica 2: Distância de Manhatan)")
					h = int(input('Entre com a heuristica: '))
					if h == 1:
						heurist = heuristica
					elif h == 2:
						heurist = heuristica_2

					if choice == 4:
						caminho_A_star(intput, estados, heurist)
					if choice == 5:
						caminho_Greedy(intput, estados, heurist)
					if choice == 6:
						caminho_Hill_Climbing(intput, estados, heurist)
			

main()