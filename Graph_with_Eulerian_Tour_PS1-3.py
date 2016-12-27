# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that have an Eulerian tour.
#

from random import randint

def tuple(a, b):
    return (a, b)

def try_this_tour(nodes, degree, tour, node_dico):
    while degree < 2:
        for node in nodes:
            while True:
                # find a random node to connect
                random_node = randint(0, len(nodes)-1) + nodes[0]
                # node cannot be connected to itself nor connected twice
                if (node != random_node):
                    t = tuple(node, random_node)
                    # tuples should not have duplicates
                    if t not in tour:
                        tour.append(t)
                        node_dico[node][0].append(random_node)
                        # add 1 to connection ctr for each node
                        node_dico[node][1] = node_dico[node][1] + 1
                        node_dico[random_node][1] = node_dico[random_node][1] + 1
                        break
        degree = degree + 1
    return tour, node_dico

def create_tour(nodes):
# node_dico = {node1: node2, node3, node4: node5, node6...node6: node1, noden}
# tour = [(node1, node2), (more tuples) ...]
# degree is always even

# get random node
# pair with each node in nodes
# get tuples
# update tour, node dico
# check if all nodes have even degrees
    all_even = False
    while all_even == False:
        tour = []
        node_dico = {}
        # initialize node_dico
        for node in nodes:
            node_dico[node] = []
            node_dico[node].append([])
            node_dico[node].append(0)
        degree = 0
        # min degree = 2
        tour, node_dico = try_this_tour(nodes, degree, tour, node_dico)
        # check if every node has even edges
        all_even = True
        for node in nodes:
            if node_dico[node][1] % 2 != 0:
                all_even = False
                #print node, node_dico[node][1]

    print tour
    print node_dico
    return tour

#########

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False

def test():
    nodes = [20, 21, 22, 23, 24, 25]
#    nodes = [1, 2, 3, 4, 5]
    tour = create_tour(nodes)
    return is_eulerian_tour(nodes, tour)


test()
