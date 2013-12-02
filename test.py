import networkx as nx

class a:
	value=5

g=nx.Graph()
g.add_node(1)
g.add_node(2)
att=a()
att2=a()
att2.value=6
g.add_edge(1,2,attr=att)
#g.add_edge(1,2,attr=att2)
g.edges()