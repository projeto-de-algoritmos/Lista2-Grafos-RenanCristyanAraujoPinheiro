# Nome: Renan Cristyan Araujo Pinheiro
# Matrícula: 17/0044386

from copy import deepcopy
from random import *

# Cada nó do grafo é um objeto do tipo Node
class Node(object):
  def __init__(self, value, name = None, adj = None, wgt = None, visited = False):
    self.value = value       # Valor do nó
    self.name = name         # Nome do nó (para facilitar a visualização)
    self.adj = adj           # Lista de nós adjacentes
    self.wgt = wgt           # Lista de pesos das arestas
    self.visited = visited   # Diz se o nó já foi visitado ou não
    
  # Método para adcionar as conexões de um nó
  def setConnex(self, connex):
    self.adj = connex

  # Método para adicionar os pesos das arestas de um nó
  def setWeights(self, weights):
    self.wgt = weights
  
  # Imprime os pesos das arestas de um nó, na ordem em que as arestas
  # foram adicionadas
  def showWeights(self):
    i = 0
    aux = []

    if self.wgt is None:
      print("Pesos das arestas de " + self.name + " : ", None)

    else:
      print("Pesos das arestas de ", self.name, " : ", self.wgt)

  # Imprime as conexões do nó. Por padrão imprime os nomes. Para
  # imprimir os valores dos nós adjacentes, usar o parâmetro "value"
  def showConnex(self, mode = None):
    i = 0
    aux = []
   
    if self.adj is None:
      print("Conexões de " + self.name + " : ", None)
    
    else:
      while i < len(self.adj):
        if mode == "value":
          aux.append(self.adj[i].value)
        else:
          aux.append(self.adj[i].name)
        i += 1
   
      if mode == "value":
          print("Conexões de " + str(self.value) + " : ", aux)
      else:
          print("Conexões de " + self.name + " : ", aux)

# Função auxiliar para resetar todos os valores de no.visited de um grafo,
# ou seja, todos os nós voltam a estar não-explorados
def resetVisited(grafo):
  for no in grafo:
    no.visited = False

# Função que retorna True se os nós u e v forem adjacentes, 
# ou False caso contrário 
def isAdjacent(u, v):
  i = 0
  while i < len(u.adj):
    if u.adj[i].value == v.value:
      return True
    i += 1
  return False

# Busca em largura começando em 'u'
# Ainda não funcional
def BFS(grafo, u):
  g = deepcopy(grafo)

  fila = []

  for no in g:
    fila.append(no)
    no.visited = True
    while len(fila):
      x = fila.pop(0)
      for y in x.adj:
        if y.visited is False:
          y.visited = True
          fila.append(y)
   
# Busca em profundidade em um grafo que pode ter mais de 1 componente,
# mas sempre começa a busca do primeiro nó
def DFS(grafo):
  for no in grafo:
    if no.visited is False:
      DFS_v(grafo, no)

# Busca em profundidade em apenas 1 componente de grafo,
# começando de qualquer nó 'u'
def DFS_v(grafo, u):
  if u not in grafo:
    print("O nó não está no grafo")
    return None

  index = 0
  for i, no in enumerate(grafo):
    if no == u:
      no.visited = True
      index = i

  print(grafo[index].name)

  # Agora, u é visto como grafo[index]
  
  for w in grafo[index].adj:
    if w.visited is False:
      DFS_v(grafo, w)

# Topological Ordering Algorithm
# Retorna valores diferentes a cada chamada de função
def TOA(grafo):
  g = deepcopy(grafo)

  nao_apontados = saoApontados(g, False, False)
  n = sample(nao_apontados, 1)
  no_alvo = n[0]

  oredenados = []
  nos = []
  # Encontrar esse nó no grafo, remover do grafo
  # e adicionar em uma lista
  j = 0
  tam = len(g)

  while j < tam:
    for i, no in enumerate(g):
      if no == no_alvo:
        no.adj = None
        oredenados.append(no)
        del(g[i])

    if len(g) < 1:
      for o in oredenados:
        nos.append(o.name)
      print("Ordenação Topológica: ", nos)
      break

    nao_apontados = saoApontados(g, False, False)
    n = sample(nao_apontados, 1)
    no_alvo = n[0]
    j = j + 1

# Função auxiliar que mostra quais nós são "apontados" (tem vizinhos), ou não
# Se apontados == True, mostra os nós apontados. Se false, mostra os não apontados (útil na função TOA)
# Se name == True, retorna uma lista com os nomes dos nós. Se false, retorna uma lista dos objetos do tipo Node
def saoApontados(grafo, apontados=True, name=True):
  nos_apontados = []
  
  for no in grafo:
    if no.adj is None:
      # Não tem vizinhos
      continue
    for vizinho in no.adj:
      if vizinho not in nos_apontados:
        nos_apontados.append(vizinho)

  nomes_dos_nos = []

  if apontados is True:
    for no in nos_apontados:
      if name is True:
        nomes_dos_nos.append(no.name)
      elif name is False:
        nomes_dos_nos.append(no)
    return nomes_dos_nos
  
  elif apontados is False:
    for no in grafo:
      if no not in nos_apontados:
        if name is True:
          nomes_dos_nos.append(no.name)
        elif name is False:
          nomes_dos_nos.append(no)
    return nomes_dos_nos

# Imprime todas as conexões do grafo
def graphConnex(grafo):
  print(50 * '-')
  print("Todas as conexões do grafo: ")
  for no in grafo:
    no.showConnex()
  print(50 * '-')

# Imprime os pesos de todas as arestas do grafo
def graphWeights(grafo):
  print(50 * '-')
  print("Todas os pesos do grafo: ")
  for no in grafo:
    no.showWeights()
  print(50 * '-')

# Ainda não funciona como esperado :(
def generateRandomGraph(n_vertices, n_arestas):
  v = [] # Lista de vertices
  gra = []

  for i in range(n_vertices):
    value = randint(1, 20)
    v.append(Node(value, "r"+str(value)))
    print(v[i].name, "\t", v[i].value)

  # Implementar aqui como conectar os nós criados
  count = 0
  while count < n_arestas:
    a = sample(v, 1)
    alvo = a[0]
    if alvo in gra:
      continue

    d = sample(v, 1)
    destino = d[0]

    if alvo.value == destino.value:
      continue

    if alvo.adj is None:
      alvo.setConnex([destino])
    else:
      if destino in alvo.adj:
        continue
      alvo.addConnex(destino)
    # alvo.showConnex()
    count = count + 1
    gra.append(alvo)
  
  for a in gra:
    a.showConnex()
  return gra

# Criando alguns nós...
v1 = Node(1, "v1")
v2 = Node(2, "v2")
v3 = Node(3, "v3")
v4 = Node(4, "v4")
v5 = Node(5, "v5")
v6 = Node(6, "v6")
v7 = Node(7, "v7")

# Criando as conexões (arestas)
v1.setConnex([v4, v5, v7])
v2.setConnex([v3, v5, v6])
v3.setConnex([v4, v5])
v4.setConnex([v5])
v5.setConnex([v6, v7])
v6.setConnex([v7])
v7.setConnex(None)

# Um grafo é simplesmente uma lista de nós
grafo = [v1, v2, v3, v4, v5, v6, v7]

# Outro grafo
x0 = Node(0, "x0")
x1 = Node(1, "x1")
x2 = Node(2, "x2")
x3 = Node(3, "x3")
x4 = Node(4, "x4")
x5 = Node(5, "x5")

x0.setConnex(None)
x1.setConnex(None)
x2.setConnex([x3])
x3.setConnex([x1])
x4.setConnex([x0, x1])
x5.setConnex([x0, x2])

grafo_2 = [x0, x1, x2, x3, x4, x5]

# Novo grafo
n1 = Node(1, "n1")
n2 = Node(2, "n2")
n3 = Node(3, "n3")
n4 = Node(4, "n4")
n5 = Node(5, "n5")
n6 = Node(6, "n6")
n7 = Node(7, "n7")

n1.setConnex([n2, n4, n5])
n2.setConnex([n1, n4, n6])
n3.setConnex([n7])
n4.setConnex([n1, n2, n5])
n5.setConnex([n1, n4])
n6.setConnex([n2])
n7.setConnex([n3])

grafo_3 = [n1, n2, n3, n4, n5, n6, n7]

o2 = Node(2, "o2")
o3 = Node(3, "o3")
o5 = Node(5, "o5")
o7 = Node(7, "o7")
o8 = Node(8, "o8")
o9 = Node(9, "o9")
o10 = Node(10, "o10")
o11 = Node(11, "o11")

o2.setConnex(None)
o3.setConnex([o8, o10])
o5.setConnex([o11])
o7.setConnex([o8, o11])
o8.setConnex([o9])
o9.setConnex(None)
o10.setConnex(None)
o11.setConnex([o2, o9])

grafo_4 = [o2, o3, o5, o7, o8, o9, o10, o11]

a1 = Node(1, "a1")
a2 = Node(2, "a2")
a3 = Node(3, "a3")
a4 = Node(4, "a4")
a5 = Node(5, "a5")
a6 = Node(6, "a6")
a7 = Node(7, "a7")
a8 = Node(8, "a8")

a1.setConnex([a2, a6, a7])
a2.setConnex([a3])
a3.setConnex([a5, a8])
a4.setConnex([a3, a8])
a5.setConnex([a4, a8])
a6.setConnex([a3, a5, a7])
a7.setConnex([a5, a8])
a8.setConnex(None)

a1.setWeights([9, 14, 15])
a2.setWeights([23])
a3.setWeights([2, 19])
a4.setWeights([6, 6])
a5.setWeights([11, 16])
a6.setWeights([18, 30, 5])
a7.setWeights([20, 44])
a8.setWeights(None)

grafo_5 = [a1, a2, a3, a4, a5, a6, a7, a8]
graphConnex(grafo_5)
graphWeights(grafo_5)

'''
print("Exemplo de ordenações aleatórias: ")
for i in range(5):
  TOA(grafo_4)
'''