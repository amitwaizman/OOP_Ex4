import math
import unittest

from client_python.DiGraph import DiGraph
from client_python.GraphAlgo import GraphAlgo

class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        g=DiGraph()
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(1, 4, 0.9)
        g.add_edge(3, 4, 10)
        algo= GraphAlgo(g)
        self.assertEqual(algo.get_graph().e_size(),7)
        self.assertEqual(algo.get_graph().v_size(), 5)

    def test_load_from_json(self):
        pass

    def test_save_to_json(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(1, 4, 0.9)
        g.add_edge(3, 4, 10)
        algo = GraphAlgo(g)
        self.assertEqual(  algo.save_to_json("file.json"),True)
    def test_shortest_path(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(1, 4, 0.9)
        g.add_edge(3, 4, 10)
        algo = GraphAlgo(g)
        x,y=algo.shortest_path(0,2)
        j=[0,1,2]
        self.assertEqual(x,2.3)
        self.assertEqual(y,j)



    def test_TSP(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(1, 4, 0.9)
        g.add_edge(3, 4, 10)
        algo = GraphAlgo(g)
        x,y=algo.TSP([0,4])
        j=[0,1,4]
        self.assertEqual(x,j)
        self.assertEqual(y,1.9)



    def test_centerPoint(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(1, 4, 0.9)
        g.add_edge(3, 4, 10)
        algo = GraphAlgo(g)
        x,y=algo.centerPoint()
        j=-1
        self.assertEqual(x,j)
        self.assertEqual(y,math.inf)
        g.add_edge(4, 1, 10)
        x,y=algo.centerPoint()
        self.assertEqual(y,1.9)



