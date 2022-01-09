import unittest

from client_python.Node import Node
from client_python.Agents import Agents
from client_python.AlgoPokemon import AlgoPokemon
from client_python.pokemons import pokemons
from client_python.GraphAlgo import GraphAlgo
class testAlgoP(unittest.TestCase):

    def test_line(self):
      algo = AlgoPokemon()
      n1 =  Node(0,(4,8,0))
      n2 =  Node(0,(2,4,0))
      pos = (1,2,0)
      poc = pokemons(1,1,pos)
      self.assertEqual(algo.line(n1,n2,poc), True)

    def test_timeall(self):
        algo = AlgoPokemon()
        g = GraphAlgo()
        for n in range(5):
            g.Graph.add_node(n)
        g.Graph.add_edge(0, 1, 1)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        list = [0,1,2]
        algo.g=g
        self.assertEqual(algo.timeall(list), 0)
    def test_timetoMove(self):

        algo = AlgoPokemon()
        g = GraphAlgo()
        j = 0
        for n in range(5):
            g.Graph.add_node(n)
            g.Graph.listNode[n].pos = (j, 3, 0)
            j = j + 1
        g.Graph.add_edge(0, 1, 2.5)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        pok = pokemons(5, 1,(2,3,0))
        algo.g=g
        algo.listp=[pok]
        ag = Agents(0,0,0,1,1,(1,2,0))
        self.assertEqual(algo.timetoMove(pok,ag),  1.5)

    def test_distance(self):
        algo = AlgoPokemon()
        g = GraphAlgo()
        for n in range(5):
            g.Graph.add_node(n)
        g.Graph.add_edge(0, 1, 1)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        pok = pokemons(5, 1,(2,3,0))
        algo.g=g
        ag = Agents(0,0,0,1,1,(1,2,0))
        self.assertEqual(algo.distance(pok,ag),  1.4142135623730951)

    def test_findEdge(self):
        algo = AlgoPokemon()
        g = GraphAlgo()
        j=0
        for n in range(5):
            g.Graph.add_node(n)
            g.Graph.listNode[n].pos=(j,3,0)
            j=j+1
        g.Graph.add_edge(0, 1, 1)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        pok = pokemons(5, 1,(2,3,0))
        algo.g=g
        self.assertEqual(algo.findEdge(pok).id1,0 )
        self.assertEqual(algo.findEdge(pok).id2,1 )


    def test_theRout(self):
        algo = AlgoPokemon()
        g = GraphAlgo()
        j=0
        for n in range(5):
            g.Graph.add_node(n)
            g.Graph.listNode[n].pos=(j,3,0)
            j=j+1
        g.Graph.add_edge(0, 1, 1)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        pok = pokemons(5, 1,(2,3,0))
        algo.g=g
        ag = Agents(0,0,0,1,1,(1,2,0))
        algo.theRout(pok,ag)
        self.assertEqual(pok.routp,{1: [0, 1]} )

    def test_algoP(self):
        algo = AlgoPokemon()
        g = GraphAlgo()
        j = 0
        for n in range(5):
            g.Graph.add_node(n)
            g.Graph.listNode[n].pos = (j, 3, 0)
            j = j + 1
        g.Graph.add_edge(0, 1, 1)
        g.Graph.add_edge(1, 0, 1.1)
        g.Graph.add_edge(1, 2, 1.3)
        g.Graph.add_edge(2, 3, 1.1)
        g.Graph.add_edge(1, 3, 1.9)
        g.Graph.add_edge(1, 4, 0.9)
        g.Graph.add_edge(3, 4, 10)
        pok = pokemons(5, 1, (2, 3, 0))
        algo.g = g
        algo.listp=[pok]
        ag = Agents(0, 0, 0, 1, 1, (1, 2, 0))
        x,y=algo.algoP(ag)
        self.assertEqual(x.value,5 )
        self.assertEqual(y,[0,1])



    def test_json_pokemons(self):
        algo = AlgoPokemon()
        st = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"}}]}'
        list = algo.json_pokemons(st)
        self.assertEqual(list[0].value,5 )
    def test_json_Agents(self):
        algo = AlgoPokemon()
        st = '{"Agents":[{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"35.18753053591606,32.10378225882353,0.0"}}]}'
        list = algo.json_Agents(st)
        self.assertEqual(list[0].id, 0)

    def test_jsoninfo(self):
        algo = AlgoPokemon()
        st = '{"GameServer":{"pokemons":2,"is_logged_in":false,"moves":0,"grade":0,"game_level":1,"max_user_level":-1,"id":0,"graph":"data/A0","agents":1}}'
        list = algo.jsoninfo(st)
        self.assertEqual(list.get("pokemons"), 2)



