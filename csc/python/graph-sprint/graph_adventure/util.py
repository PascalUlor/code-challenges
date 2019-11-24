class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        Given that the vertex of each vertice is set
        so each vertex which is the node and key of the vertices is equated to a set
        """
        # pass  # TODO
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            print('No vertex at here')
            raise KeyError("That vertex does not exist")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print('visited node', v)
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print('visited node', v)
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)
    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # pass  # TODO

        visited.add(starting_vertex)
        print('recur visited node', starting_vertex)
        for v in self.vertices[starting_vertex]:
            if v not in visited:
                self.dft_recursive(v)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            vertex = q.dequeue()
            last_vertex = vertex[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return vertex
                visited.add(last_vertex)
                for next_vertex in self.vertices[last_vertex]:
                    path = list(vertex)
                    path.append(next_vertex)
                    q.enqueue(path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
         # create a stack
        s = Stack()
        # push a list holding the starting vertex id
        s.push([starting_vertex])
        # created an empty visited set
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop to the path
            vertex = s.pop()
            # set a vert to the last item in the path
            last_vertex = vertex[-1]
            # if vert is not in visited
            if last_vertex not in visited:
                # if vert is equal to target value
                if last_vertex == destination_vertex:
                    # return path
                    return vertex
                # add vert to visited set
                visited.add(last_vertex)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[last_vertex]:
                    # set a new path equal to a new list of the path (copy)
                    path = list(vertex)
                    # append next vert to new path
                    path.append(next_vert)
                    # push the new path
                    s.push(path)
        return None


