# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def tuple(x, y):
    return x, y

def get_tuple_nodes(tuple):
    a, b = tuple
    return a, b

# compare to another tuple
def compare_nodes(used_nodes, tuples, graph, tpl ):
    # base case
    if len(tuples) == 0:
        final_a, final_b = get_tuple_nodes(used_nodes[-1])
        first_a, first_b = get_tuple_nodes(used_nodes[0])
        if first_a == final_b:
            return True
        else:
            return False

    # get next tuple from tuples
    for tup in tuples:
        #print "TUP" + str(tup)
        # check if node has not already been used
        if tup not in used_nodes:
            curr_a, curr_b = get_tuple_nodes(tup)
            prev_a, prev_b = get_tuple_nodes(tpl)
            # check if the b of previous tuple == the a of current tuple
            if prev_b == curr_a or prev_b == curr_b:
                if prev_b == curr_a:
                    #print tup
                    tuples.remove(tup)
                    used_nodes.append(tup)
                    if not compare_nodes(used_nodes, tuples, graph, tup):
                        tuples.add(tup)
                        used_nodes.remove(tup)
                        return False
                elif prev_b == curr_b:
                    opp_tup = tuple(curr_b, curr_a)
                    #print opp_tup
                    tuples.remove(tup)
                    used_nodes.append(opp_tup)
                    if not compare_nodes(used_nodes, tuples, graph, opp_tup):
                        tuples.add(tup)
                        used_nodes.remove(opp_tup)
                        return False
                return True
    return False

#THROW IT IN A SET
def find_eulerian_tour(graph):
    nodes = []
    tuples = set()
    used_nodes = []
    tupl = graph[0]

    # create a set of tuples
    for tpl in graph:
        # place elem in set
        tuples.add(tpl)
    compare_nodes(used_nodes, tuples, graph, tupl)

    # convert tuples list to nodes list
    for node in used_nodes:
        if node == used_nodes[0]:
            nodes.extend(node)
        else:
            a, b = get_tuple_nodes(node)
            nodes.append(b)
    return nodes


#graph = [(1, 2), (2, 3), (3, 1)]
#graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
#graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]
print find_eulerian_tour(graph)


