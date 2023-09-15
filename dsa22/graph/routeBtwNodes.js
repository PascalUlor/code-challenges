class Graph {
    vertices;
    constructor(){
        this.vertices = {}
    };

    addVertex(vertexId) {
        this.vertices[vertexId] = new Set();
    }

    addEdge(v1, v2) {
        if(this.vertices[v1] && this.vertices[v2]) {
            this.vertices[v1].add(v2);
            this.vertices[v2].add(v1);
        }
    }

    bfs(startNode, endNode) {
        if(startNode === endNode) return true;

        const queue = [];

        queue.push(startNode);
        const visitedNodes = new Set();
        while(queue.length !== 0) {
            let node = queue.shift();
            if(node === endNode) return true;

            if (!visitedNodes.has(node) && this.vertices[node]) {
                visitedNodes.add(node);
                for (let nextNode of this.vertices[node]) {
                    queue.push(nextNode)
                }
            }
            
        }
        return false;
    }

    dfs(startNode, endNode) {
        if(startNode === endNode) return true;
        const stack = [];

        stack.push(startNode);
        const visitedNodes = new Set();
        while(stack.length !== 0) {
            let node = stack.pop();
            if(node === endNode) return true;

            if (!visitedNodes.has(node) && this.vertices[node]) {
                visitedNodes.add(node);
                for (let nextNode of this.vertices[node]) {
                    stack.push(nextNode)
                }
            }
            
        }
        return false;
    }
}

const graph = new Graph();
graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)



graph.addEdge(0, 2);
graph.addEdge(1, 2);
graph.addEdge(2, 0);
graph.addEdge(2, 3);
graph.addEdge(4, 3);

console.log(graph, '<<<<===graph');

console.log(graph.bfs(3, 4), '<<<<===BFS');

console.log(graph.dfs(3, 4), '<<<===DFS');