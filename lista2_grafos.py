# Nome: Renan Cristyan Araujo Pinheiro
# Matrícula: 17/0044386

from copy import deepcopy
from random import *

# Cada nó do grafo é um objeto do tipo Node
class Node(object):
  def __init__(self, value, name = None, adj = None, visited = False):
    self.value = value       # Valor do nó
    self.name = name         # Nome do nó (para facilitar a visualização)
    self.adj = adj           # Lusta de nós adjacentes
    self.visited = visited   # Diz se o nó já foi visitado ou não
    
  # Método para adcionar as conexões de um nó
  def setConnex(self, connex = None):
    self.adj = connex

  # Método auxiliar para adicionar uma conexão numa lista de conexões
  def addConnex(self, connex):
    self.adj.append(connex)
  
  # Imprime as conexões do nó. Por padrão imprime os nomes. Para
  # imprimir os valores dos nós adjacentes, usar o parâmetro "value"
  def showConnex(self, mode = None):
    i = 0
    aux = []
    if self.adj == None:
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
   
# Busca em profundidade começando em 'u'
# Até faz a busca (não tenho certeza se de forma correta),
# mas buga quando todos os vizinhos de um nó já foram visitados...
def DFS(u):
  print("\nComeço da iteração:")
  print("Nó atual: ", u.name)
  print("u.visited = ", u.visited)
  u.visited = True
  print("Agora, ", u.name, " foi marcado como visitado")
  i = 0
  while i < len(u.adj):
    print("Vizinho: ", u.adj[i].name)
    print("u.adj[",i,"].visited = ", u.adj[i].visited)
    if u.adj[i].visited == False:
      print("Valor no momento = ", u.adj[i].value)
      DFS(u.adj[i])
    i += 1
  print("Fim da função:")

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
      # return ordenados
      break

    nao_apontados = saoApontados(g, False, False)
    n = sample(nao_apontados, 1)
    no_alvo = n[0]
    j = j + 1

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

def graphConnex(grafo):
  print(50 * '-')
  print("Todas as conexões do grafo: ")
  for no in grafo:
    no.showConnex()
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

# grafo_3 = generateRandomGraph(5, 5)

# Criando alguns nós...
v1 = Node(1, "v1")
v2 = Node(2, "v2")
v3 = Node(3, "v3")
v4 = Node(4, "v4")
v5 = Node(5, "v5")
v6 = Node(6, "v6")
v7 = Node(7, "v7")

v1.setConnex([v4, v5, v7])
v2.setConnex([v3, v5, v6])
v3.setConnex([v4, v5])
v4.setConnex([v5])
v5.setConnex([v6, v7])
v6.setConnex([v7])
v7.setConnex(None)

# Um grafo é simplesmente uma lista de nós
grafo = [v1, v2, v3, v4, v5, v6, v7]

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