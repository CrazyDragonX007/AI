from queue import Queue

# This is an adjacency list representation of our graph
graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Bucharest': [('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211), ('Urziceni', 85)],
    'Craiova': [('Pitesti', 138), ('Dobreta', 120), ('Rimnicu Vilcea', 146)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Urziceni': [('Hirsova', 98), ('Bucharest', 85), ('Vaslui', 142)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Zerind': [('Oradea', 71), ('Arad', 75)]
}


def h(n):
    H = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Dobreta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Fagaras': 176,
        'Pitesti': 100,
        'Bucharest': 0,
        'Giurgiu': 77,
        'Urziceni': 80,
        'Hirsova': 151,
        'Eforie': 161,
        'Vaslui': 199,
        'Iasi': 226,
        'Neamt': 234
    }

    return H[n]

def a_star(graph, start, end):

        open_list = set([start])
        closed_list = set([])
        g = {}
        g[start] = 0
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + h(v) < g[n] + h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in graph[n]:
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

def dfs(graph, start, end, path=[], visited=[]):
    # print(path)
    # print(visited)
    path.append(start)
    visited.append(start)
    if start==end:
        # print('here')
        return path
    for (neighbour, weight) in graph[start]:
        if neighbour not in visited:
            result = dfs(graph,neighbour,end,path,visited)
            # print(result)
            if result is not None:
                return result
    path.pop()
    return None


def bfs(graph, start, end):
    visited = []
    queue = Queue()

    queue.put(start)
    visited.append(start)

    parent = dict()
    parent[start] = None

    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == end:
            path_found = True
            break

        for (next_node, weight) in graph[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.append(next_node)

    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return path

print('BFS Path:',bfs(graph,'Arad','Bucharest'))
print('DFS Path:',dfs(graph,'Arad','Bucharest'))
print('Output of A*:')
a_star(graph,'Arad','Bucharest')
