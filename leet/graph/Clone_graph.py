# Definition for a undirected graph node
class Node:
    '''
    Define a node class for our undirected graph
    '''
    def __init__(self, node_label, node_neighbors=[]):
        self.label = node_label
        self.neighbors = node_neighbors

class Solution(object):
    def cloneGraph(self, node):
        nodeMap = {}
        return self.cloneNode(node, nodeMap)

    def cloneNode(self, node, nodeMap):
        if node == None:
            return None
        if node.label in nodeMap:
            return nodeMap[node.label]
        newNode = Node(node.label)
        nodeMap[node.label] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneNode(neighbor, nodeMap))
        return newNode

if  __name__ == "__main__":
    test = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    check = test.cloneGraph(node1)