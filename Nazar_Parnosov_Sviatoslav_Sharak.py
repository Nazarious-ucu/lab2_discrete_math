"""
member1: Nazar Parnosov
member2: Sviat Sharak
"""
from typing import List, Dict


def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    :rtype: dict(key=int, value=list(int))
    :param file_name: string
    :return: graph
    """
    dct_result = {}

    # read scv file and create a list of all list of list elements in lines
    with open(file_name, 'r', encoding='utf-8') as matrix:
        lst_lines = [line.strip().split(',') for line in matrix.readlines()]

    # create keys with value (= empty list) of graph vertex in result dict
    [dct_result.update({i: []}) for i in range(len(lst_lines))]

    # fill in dict
    for i, line in enumerate(lst_lines):
        for k, element in enumerate(line):
            if element == '1':
                dct_result[i].append(k)

    return dct_result


def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result
    """
    return help_bfs(graph, 0)

def help_bfs(graph, first_vertex):
    """
    help func to bfs
    """
    lst_result = [first_vertex]
    help_graph = {}

    #fill in help graph without empty vertex
    for key in graph:
        if not len(graph[key]) == 0:
            help_graph.update({key: graph[key]})

    #create stack of bfs of graph
    while len(lst_result) != len(help_graph):
        for k in lst_result:
            for i in help_graph[k]:
                if not i in lst_result:
                    lst_result.append(i)

    return lst_result

def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    """
    # Your code goes here(delete "pass" keyword)
    pass


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers
    """
    # Your code goes here(delete "pass" keyword)
    pass


def find_path(number: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    :rtype: bool
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :return:
    """
    graph = {}

    #if num of vertex is 0
    if number == 0:
        return False
    #transform graph from list of lists to dictionary
    for edge in edges:
        for i, elem in enumerate(edge):
            if elem in graph:
                graph[elem].append(edge[i - 1])
            else:
                graph[elem] = [edge[i - 1]]

    #call func help_bsv from vertex sourse
    lst_bfs = help_bfs(graph, source)

    #return values
    if destination in lst_bfs:
        return True
    return False
