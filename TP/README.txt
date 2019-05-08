##########################################################
@ TP de Inteligência Artificial de Gabriel Lopes Machado @
##########################################################

Para utilizar o programa basta acessar o interfze de acesso aos diferentes métodos de busca definida em main.py (a versão do python foi a 3.6.x), lembrando que o quadrado vazio corresponde ao indice 0.


Modelagem:

Estado -> O estado de de referência foi uma classe classe python que possui a seguinte estrutura básica:

class EightPuzzle(object):

	def __init__(self, state, index=[], cor=0):

	def indexes(self, lista, parent, n):


	def moviments(self):

  Sendo que o método indexes é usado para criar as arestas da minha estrutura em GRAFO e o método movimento usado pelo métdo indexes para retornar quais os movimentos são válidos em um determinado estado.

Função Sucessora -> Diz respeito de como os estados serão enseridos na fila de expansão de nós
                

                  if (lista[child[2]].cor == 0) and (node.deep < deep):
					lista[child[2]].move = child
					lista[child[2]].deep = node.deep + 1
					if not test_goal(lista[child[2]]):
						
						lista[child[2]].cor = 1
						bisect.insort(frontier, lista[child[2]])
						
					else:
						goal_state = lista[child[2]]
						return goal_state, frontier


    Basicamente é feita uma simples validação se o nó expandido já está na fronteira conferindo sua cor, sendo que que todos os nós são testados no momento em que são expandidos e, obviamente, são tratados os casos de nós repetidos.

    Diferença entre os algorítimos -> De forma objetiva, o que diferencia os diferentes algorítimos é a forma com que ele organiza a ordem de expansão e visitação de cada nó, sendo uma breve descrição:
        1. BFS - Coloca a lista de expansão como sendo os nós pertencentes ao nó mais superficiais antes dos nós mais profundos.
        2. IDS - Coloca o nó mais profundidade primeiro na lista de expansão, além de dar um limite incremental na profundidade máxima
        3. UCS - Organiza a lista de forma que os nós de menores custo são visitados primeiro.
        4. A* - Idem ao UCS, só que o custo é medido como o custo real do nó mais uma heurtica que tenta mensurar a distância real até 