import unittest

from client_python.DiGraph import DiGraph
from client_python.Node import Node
from client_python.Edge import Edge


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        a = DiGraph()
        n1 = Node(1, (1, 2, 0))
        n2 = Node(0, (1, 1, 0))
        a.add_node(n1)
        a.add_node(n2)
        size = a.v_size()
        self.assertEqual(size, 2)

    def test_e_size(self):
        a = DiGraph()
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        e1 = Edge(1, 2, 0)
        e2 = Edge(2, 1, 0)
        a.add_edge(1, 2, 0)
        size = a.e_size()
        self.assertEqual(size, 1)

    def test_add_edge(self):
        a = DiGraph()
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        e1 = Edge(1, 2, 0)
        e2 = Edge(2, 1, 0)
        b = a.add_edge(e1.id1, e2.id2, 0)
        self.assertEqual(b, True)

    def test_add_node(self):
        a = DiGraph()
        n2 = Node(0, (1, 1, 0))
        b = a.add_node(n2)
        self.assertEqual(b, True)

    def test_get_mc(self):
        a = DiGraph()
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        e1 = Edge(1, 2, 0)
        e2 = Edge(2, 1, 0)
        a.add_edge(1, 2, 0)
        m = a.e_size()
        self.assertEqual(m, 1)

    def test_get_all_v(self):
        a = DiGraph()
        n1 = Node(1, (1, 2, 0))
        n2 = Node(2, (1, 1, 0))
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        a.add_edge(n1.id, n2.id, 0)
        dict1 = a.get_all_v()
        self.assertEqual(dict1.get(1).id, 1)
        self.assertEqual(dict1.get(2).id, 2)

    def test_all_out_edges_of_node(self):
        a = DiGraph()
        n1 = Node(1, (1, 2, 0))
        n2 = Node(2, (1, 1, 0))
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        a.add_edge(n1.id, n2.id, 0)
        ll = {2: 0}

        self.assertEqual(a.all_out_edges_of_node(n1.id), ll)

    def test_remove_node(self):
        a = DiGraph()
        n = Node(1, (1, 2, 0))
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        aa = a.v_size()
        size = a.remove_node(n.id)
        ab = a.v_size()
        self.assertEqual(size, True)

    def test_remove_edge(self):
        a = DiGraph()

        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        a.add_edge(1, 2, 0)
        a.remove_edge(1, 2)
        size = a.e_size()
        self.assertEqual(size, 0)

    def test_all_in_edges_of_node(self):
        a = DiGraph()
        n1 = Node(1, (1, 2, 0))
        n2 = Node(2, (1, 1, 0))
        a.add_node(1, (1, 2, 0))
        a.add_node(2, (1, 1, 0))
        a.add_edge(n1.id, n2.id, 0)
        ll = {1: 0}
        self.assertEqual(a.all_in_edges_of_node(n2.id), ll)

