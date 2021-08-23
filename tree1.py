file = '/Users/isajgordeev/Desktop/Python_Coding/just/data/rosalind_tree.txt'

nodes_text = open(file)

revealed_nodes = nodes_text.readlines()

number_of_all_nodes = int(revealed_nodes[0])
revealed_nodes.pop(0)
nodes = []
nodes_list_label = []

for line in revealed_nodes:
    nodes.append(tuple(line.replace('\n', '').split(' ')))

# print(nodes)

graph = []
index_of_set_bond = 0
number_of_nodes = 0


class Node():
    def __init__(self, bond=None, index_bond=None):
        self.index_bond = index_bond
        self.vertex = bond


for bond in nodes:
    nodes_list_label.append(bond[0])
    nodes_list_label.append(bond[1])
nodes_list_label = list(set(nodes_list_label))
print(nodes_list_label)

graph = {}


def create_graph(graph, nodes):
    index = 0
    for bond in nodes:
        if bond[0] not in graph and bond[1] not in graph:
            graph[bond[0]] = index
            graph[bond[1]] = index
        if bond[0] not in graph and bond[1] in graph:
            temp_index = min(graph[bond[1]], index)
            graph[bond[0]] = temp_index
        if bond[0] in graph and bond[1] not in graph:
            temp_index = min(graph[bond[0]], index)
            graph[bond[1]] = temp_index
        if bond[0] in graph and bond[1] in graph:
            temp_index = min(graph[bond[1]], graph[bond[0]])
            graph[bond[0]] = temp_index
            graph[bond[1]] = temp_index

        index += 1


for bond in nodes:
    create_graph(graph,nodes)


print(len(set(graph.values()))-1+number_of_all_nodes-len(set(nodes_list_label)))