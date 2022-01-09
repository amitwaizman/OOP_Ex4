import json
import sys

import random
from typing import List
from  queue import PriorityQueue
from client_python.DiGraph import DiGraph
from client_python.GraphInterface import GraphInterface
from client_python.Node import Node
import  matplotlib.pyplot as plt
import math



class GraphAlgo:

        def __init__(self, Graph=None):
            if Graph == None:
                self.Graph = DiGraph()
            else:
                    self.Graph = Graph

        """
        :return: the directed graph on which the algorithm works on.
        """
        def get_graph(self) -> GraphInterface:
            return self.Graph

        def __repr__(self) -> str:
            return f"Graph: |V|={self.get_graph().v_size()} |E|={self.get_graph().e_size()}"

        """
        Loads a graph from a json file.
        """
        def load_from_json(self, file_name) -> bool:
                graph = DiGraph()
                dict = json.loads(file_name)
                nodes = dict['Nodes']
                edges = dict['Edges']
                for n in nodes:
                    id = n['id']
                    if n.keys().__contains__("pos"):
                        pos = eval(n["pos"])
                        graph.add_node(id, pos)
                    else:
                        graph.add_node(id, None)
                for e in edges:
                    id1 = e["src"]
                    weight = e["w"]
                    id2 = e["dest"]
                    graph.add_edge(id1, id2, weight)
                self.Graph = graph
                return True

        """
        Saves the graph in JSON format to a file  
        """
        def save_to_json(self, file_name: str) -> bool:
            try:
                with open(file_name, "w") as file:
                    dict = {}
                    nodes = []
                    edges = []
                    for i in self.Graph.listNode.values():
                        if i.pos==None:
                            nodes.append({"id": i.id})
                        else:
                            nodes.append({"id": i.id, "pos": str(
                                str(i.pos[0]) + "," + str(i.pos[1]) + "," + str(
                                    i.pos[2]))})
                        for j in self.Graph.listEdge.values():
                            edges.append({"src": j.id1, "w": j.weight ,"dest": j.id2})
                    dict["Nodes"] = nodes
                    dict["Edges"] = edges

                    json.dump(dict, indent=4, fp=file)
                    return True
            except IOError as e:
                    print(e)
                    return False

        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        """
        def shortest_path(self, id1: int, id2: int) -> (float, list):
            if id1 == id2:
              return 0,[id1]
            if self.Graph.listNode.get(id1)!=None:
             a=self.Graph.listNode.get(id1)
             dijk= self.Dijkstra(a)
             s = []
             n=dijk.get(id2)
             if n==None:
                return math.inf,[]
             if dijk.get(id2)==math.inf:
                return [],math.inf
             s.insert(0,id2)
             while n != id1:
                s.insert(0, n)
                n=dijk.get(n)
             s.insert(0,id1)
             sum=0
             if len(s)==0:
                return math.inf,[]
             return self.Graph.listNode.get(id2).weight, s

        """
         Finds the shortest path that visits all the nodes in the list
        """
        def TSP(self, node_lst: List[int]) -> (List[int], float):
            min = sys.maxsize
            mind = sys.maxsize
            distm = 0
            ans = []
            ans2 = []
            for i in node_lst:
                for j in node_lst:
                    if i != j:
                        dis, ans = self.shortest_path(i, j)
                        a = self.isFound(node_lst, ans)
                        if a == True:
                            if min >= len(ans):
                                if mind > dis:
                                    min = len(ans)
                                    ans2 = ans
                                    distm = dis
                                    mind = dis
            i = len(node_lst) - 1
            j = len(node_lst) - 1
            while i > 0:
                while j > 0:
                    if i != j:
                        dis, ans = self.shortest_path(node_lst[i], node_lst[j])
                        a = self.isFound(node_lst, ans)
                        if a == True:
                            if min > len(ans):
                                if mind >= dis:
                                    min = len(ans)
                                    ans2 = ans
                                    distm = dis
                                    mind = dis
                    j = j - 1
                j = len(node_lst) - 1
                i = i - 1
            if len(ans2) == 0:
                i = 0
                distm = 0
                while (i < len(node_lst) - 1):
                    dis, ans = self.shortest_path(node_lst[i], node_lst[i + 1])
                    j = 0
                    while j < len(ans):
                        if len(ans2) == 0:
                            ans2.append(ans[j])
                        if len(ans2) != 0:
                            if ans[j] != ans2[(len(ans2) - 1)]:
                                ans2.append(ans[j])
                        j = j + 1
                    distm = distm + dis
                    i = i + 1
            return ans2, distm

        """
         Finds the node that has the shortest distance to it's farthest node.
        """
        def centerPoint(self) -> (int, float):
            sumMin = math.inf
            min_noseIs = Node
            for i in self.Graph.listNode.values():
                wMax = []
                dijk: dict = self.Dijkstra(i)
                if len(dijk) != 0:
                    for j in self.Graph.listNode:
                        w = 0
                        if i != j:
                            w = self.Graph.listNode[j].weight
                            if w != math.inf:
                                wMax.append(w)


                    max = sys.float_info.min
                    for k in range(len(wMax)):
                        if wMax[k] > max:
                            max = wMax[k]
                    if sumMin > max:
                        sumMin = max
                        min_noseIs = i
                else:
                    ans=(-1, math.inf)
                    return ans
                ans=(min_noseIs.id,sumMin)
            return ans

        """
                Plots the graph.
                If the nodes have a position, the nodes will be placed there.
        """
        def plot_graph(self) -> None:
                for i in self.Graph.listNode.values():
                    if i.pos is None:
                        xpos = random.uniform(0.0, 100)
                        ypos = random.uniform(0.0, 100)
                        pos = (xpos, ypos, 0)
                        i.pos = pos

                    xpos, ypos, zpos = i.pos
                    plt.plot(xpos, ypos, markersize=10, marker='.', color='red')
                    plt.text(xpos, ypos, str(i.id), color="green", fontsize=12)
                    for edge, weight in self.Graph.all_out_edges_of_node(i.id).items():
                        n = self.Graph.listNode[edge]
                        if n.pos is None:
                            v = random.uniform(0.0, 100)
                            w = random.uniform(0.0, 100)
                            pos = (v, w, 0)
                            n.pos = pos
                        v, w, zpos = n.pos
                        plt.annotate("", (xpos, ypos), (v, w), arrowprops=dict(arrowstyle="<-"))

                plt.show()

         #change Max Value in weight
        def changeMaxVal(self):
            for i in self.Graph.listNode:
                self.Graph.listNode[i].weight=sys.maxsize*2+1


        # Turns the entire tag of the node to 0
        def changeZero(self):
            for i in self.Graph.listNode:
                self.Graph.listNode[i].tag = 0

        #Returns if what is in the list  A is in the list B
        def isFound(self, a: List[int], b: List[int]) -> bool:
            if len(a) == 0 or len(b) == 0:
                return False
            if len(a) > len(b):
                return False
            i=0
            while i < len(a):
                find = False
                j = 0
                while j < len(b) and not find:
                    if a[i] == b[j]:
                        find = True
                    j = j + 1
                if not find:
                    return False
                i=i+1
            return True


        #Calculates the shortest path between the src and all the other vertices in the graph
        def Dijkstra(self,src:Node)->dict:
          self.changeMaxVal()
          self.changeZero()
          parents={}
          QueueP=PriorityQueue()
          QueueP.put(src)
          src.weight=0
          while (not QueueP.empty()):
              n =QueueP.get()
              if not QueueP.empty():
               temp=QueueP.get()
               QueueP.put(temp)
               if (temp!=None) and (temp.weight<n.weight):
                  QueueP.put(n)
                  n=QueueP.get()
               n.tag=1
              if self.Graph.listNode[n.id].edgeout==None:
                # self.changeMaxVal()
                break
              else:
                for i in self.Graph.listNode[n.id].edgeout:
                    nodeD= i
                    W=self.Graph.listNode[n.id].edgeout[i] +n.weight
                    if nodeD!=None:
                       if W< self.Graph.listNode[i].weight:
                           self.Graph.listNode[i].weight=W
                           if parents.get(nodeD)!=None:
                                parents[nodeD]=n.id
                           else:
                               parents[nodeD]=n.id
                               QueueP.put(self.Graph.listNode[i])
          return parents

