graph = {}

graph['you'] = ['alice', 'bob', 'clarie']

graph['bob'] = ['anuj', 'peggy']

graph['alice'] = ['peggy']

graph['clarie'] = ['thom', 'jonny']

graph['thom'] = []

graph['jonny'] = []

graph['anuj'] = []

graph['peggy'] = []

from collections import deque


def search():
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    
    return False


def person_is_seller(name):
    return name[-1] == 'm'

print(search())


"""
breadt first serach complexity is O(V <numbrt og vertices> + E <number of edges>)

If task A depends on
task B, task A shows up later in the list. his is called a topological sort,
and it’s a way to make an ordered list out of a graph. Suppose you’re
planning a wedding and have a large graph full of tasks to do—and
you’re not sure where to start. You could topologically sort the graph
and get a list of tasks to do, in order.

A tree is a special type of graph, where no edges
ever point back.

• Breadth-irst search tells you if there’s a path from A to B.
• If there’s a path, breadth-irst search will ind the shortest path.
• If you have a problem like “ind the shortest X,” try modeling your
problem as a graph, and use breadth-irst search to solve.
• A directed graph has arrows, and the relationship follows the
direction of the arrow (rama -> adit means “rama owes adit money”).
• Undirected graphs don’t have arrows, and the relationship goes both
ways (ross - rachel means “ross dated rachel and rachel dated ross”).
• Queues are FIFO (First In, First Out).
• Stacks are LIFO (Last In, First Out).
• You need to check people in the order they were added to the search
list, so the search list needs to be a queue. Otherwise, you won’t get
the shortest path.
• Once you check someone, make sure you don’t check them again.
Otherwise, you might end up in an infinite loop.
"""

"""
1. Check if there is a path from point A to point B
2. Find the shortest path from point A to point B - breadth-first search
3. Find the fastest path to get from point A to point B - Dijkstra's algorithm (weighted graph)

There is two types of graphs which is undirected graph and directed graph, Undirected means two edges
points to each other by default which is a cycle, directed graph is when edges can point only one to other.

breadth-first search works with undirected graphs, and Dijkstra's algorithm works with directed acyclic graphs (DAGs) 
"""

graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


def bfs(graph, node):
    # breadth first search implementation
    # this example is a copy of: https://youtu.be/HZ5YTanv5QE

    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited
