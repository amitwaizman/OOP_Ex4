from client_python.Edge import Edge
from client_python.Node import Node


class DiGraph:
    def __init__(self):
        self.sizeNode = 0
        self.sizeEdge = 0
        self.listNode = {}
        self.listEdge = {}
        self.mc = 0

    def __repr__(self) -> str:
        return f"Graph: |V|={self.sizeNode} |E|={self.sizeEdge}"

    """
     Returns the number of vertices in this graph
    """
    def v_size(self) -> int:
        return self.sizeNode

    """
    Returns the number of edges in this graph
    """
    def e_size(self) -> int:
        return self.sizeEdge

    """
     return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    """
    def get_all_v(self) -> dict:
        return self.listNode

    """
    return a dictionary of all the nodes connected to (into) node_id ,
     each node is represented using a pair (other_node_id, weight)
    """
    def all_in_edges_of_node(self, id1: int) -> dict:
            return self.listNode[id1].edgein


    """
    return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """
    def all_out_edges_of_node(self, id1: int) -> dict:
            return self.listNode[id1].edgeout

    """
     Returns the current version of this graph,
     on every change in the graph state - the MC should be increased
    """
    def get_mc(self) -> int:
        return self.mc


    """
    Adds an edge to  the graph.
    """
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if ( self.listNode.get(id1)==None or self.listNode.get(id2)==None):
             return False
        a = Edge(id1, id2, weight)
        n1 = self.listNode.get(id1)
        n2 = self.listNode.get(id2)
        key = str(id1) + "," + str(id2)

        if key in self.listEdge:
            return False
        else:
            self.listEdge[key]=a
            n1.edgeout[id2]=weight
            n2.edgein[id1]=weight
        self.sizeEdge = self.sizeEdge + 1
        return True

    """
        Adds an node to  the graph.
    """
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.listNode.keys():
            return False
        self.listNode[node_id] = Node(node_id, pos)
        self.sizeNode = self.sizeNode + 1
        self.mc = self.mc + 1
        return True

    """
        Remove  node in  the graph.
    """
    def remove_node(self, node_id: int) -> bool:
        if  self.listNode.get(node_id)==None:
            return False
        for i in self.listNode.items():
            n= i[1]
            if n.edgein.get(node_id) != None:
             key = str(n.id) +","+ str(node_id)
             self.listEdge.pop(key)
             n.edgein.pop(node_id)
            if n.edgeout.get(node_id) != None:
               key = str(node_id) + "," + str(n.id)
               n.edgeout.pop(node_id)
               self.listEdge.pop(key)
        self.listNode.pop(node_id)
        self.mc = self.mc + 1
        self.sizeNode = self.sizeNode - 1
        return True
    """
        Remove  edge in  the graph.
    """
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        key = str(node_id1) + "," + str(node_id2)
        if key in self.listEdge:
            e = self.listEdge.pop(key)
            self.listNode[node_id2].edgein.pop(node_id1)
            self.listNode[node_id1].edgeout.pop(node_id2)
            self.mc = self.mc + 1
            self.sizeEdge = self.sizeEdge - 1
            return True
        return False
