import json
import math
from client import  Client
from client_python.Agents import Agents
from client_python.Node import Node
from client_python.pokemons import pokemons
from client_python.GraphAlgo import GraphAlgo
"""
A class for the implementation of Pokemon placement to the agent, object: listp- list of pokemons, listA- list of agents, info, g-GraphAlgo and client.
-function:
*linel: The function gets 2 nodes and pos calculates the straight equation of the 2 nodes and returns true if the pos is on this equation and false otherwise.
*timeall:Returns the time it takes for the agent to reach Pokemon when it's in edge's src.
*timetoMove: Returns the time it takes for the agent to reach Pokemon
*distance: Calculates the distance from the agent to the Pokemon
*findEdge: Finds the side that the Pokemon is on
*theRout: Calculates the distance of an agent to each Pokemon
*routrSrc: Calculates the route to the src of the edge the Pokemon is on
*firstLOC:Returns the position of the src of the edge the Pokemon is on
*algoP: Places to the agent the Pokemon closest to him
*json_pokemons: Loading Pokemon from the server
*json_Agents: Loading agent from the server
*jsoninfo: Loading info from the server
"""

class AlgoPokemon:

     def __init__(self):
       self.listp=[]
       self.listA=[]
       self.info={}
       self.g=GraphAlgo()
       self.client = Client()
#y=mx+n
     def line(self,a:Node,b:Node,c)->bool:

         eps=0.00000015450
         m=(a.pos[1]-b.pos[1])/(a.pos[0]-b.pos[0])
         n=a.pos[1]-m*a.pos[0]
         d=m*c.pos[0]+n
         if abs(c.pos[1]-d)<=eps:
            return True
         return False
#d/s=t
     def timeall(self,l:list):
         return  self.g.Graph.listNode.get(l[len(l)-1]).weight

     def timetoMove(self,p:pokemons,a:Agents):
        ee=self.findEdge(p)
        e1=self.g.Graph.listNode.get(ee.id2)
        w= ee.weight
        d=self.distance(p,e1)
        sum=abs(w-d)
        t=sum/a.speed
        return  t

     def distance(self, p:pokemons, a:Agents):
         a=math.pow(p.pos[0]-a.pos[0],2)+math.pow(p.pos[1]-a.pos[1],2)
         d=math.sqrt(a)
         return d

     def findEdge(self, p):
         type = p.type
         for i in self.g.Graph.listEdge.values():
             src = self.g.Graph.listNode.get(i.id1)
             dest = self.g.Graph.listNode.get(i.id2)
             a = self.line(src, dest, p)
             if (a == True):
                 if src.id > dest.id:
                     t1 = -1
                     if type == t1:
                         return i
                     else:
                         k = str(dest.id) + "," + str(src.id)
                         return self.g.Graph.listEdge.get(k)

                 else:
                     t1 = 1
                     if type == t1:
                         return i
                     else:
                         k = str(dest.id) + "," + str(src.id)
                         return self.g.Graph.listEdge.get(k)


     def theRout(self, p:pokemons,a:Agents):
         edgeP = self.findEdge(p)
         f, l = self.g.shortest_path(a.src, edgeP.id2)
         size= len(l)-1
         if l[size-1]!=edgeP.id1:
             l.append(edgeP.id1)
             l.append(edgeP.id2)
         dic={}
         p.routp=dic
         p.routp[f]=l



     def RouteSrc(self, p: pokemons, a: Agents):
             edgeP = self.findEdge(p)
             f, l = self.g.shortest_path(a.src, edgeP.id1)
             t=self.timeall(l)
             return t
     def firstLOC(self,p):
         a=self.findEdge(p)
         return a.id1

     def algoP(self,a:Agents):
       for i in self.listp:
             self.theRout(i, a)
       self.listp= sorted(self.listp,key=lambda x:sorted(x.routp.items()))
       for j in self.listp:
           for k in j.routp.values():
             if(j.tag==0):
                j.tag=1
                return j,k







     def json_pokemons(self, file_name: str):
            self.listp=[]
            dict = json.loads(file_name)
            pock = dict['Pokemons']
            for n in pock:
                value = n["Pokemon"]["value"]
                type = n["Pokemon"]["type"]
                pos = eval(n["Pokemon"]["pos"])
                p = pokemons(value, type, pos)
                self.listp.append(p)
            return self.listp


     def json_Agents(self, file_name: str):
                 self.listA=[]
                 dict = json.loads(file_name)
                 pock = dict['Agents']
                 for n in pock:
                     value = n["Agent"]["value"]
                     id = n["Agent"]["id"]
                     src = n["Agent"]["src"]
                     dest = n["Agent"]["dest"]
                     speed = n["Agent"]["speed"]
                     pos = eval(n["Agent"]["pos"])
                     A = Agents(id,value,src,dest,speed,pos)
                     self.listA.append(A)
                 return self.listA

     def jsoninfo(self, file_name: str):
                     self.info={}
                     dict = json.loads(file_name)
                     pock = dict['GameServer']
                     self.info["pokemons"] = pock["pokemons"]
                     self.info["is_logged_in"] = pock["is_logged_in"]
                     self.info["moves"] = pock["moves"]
                     self.info["grade"] = pock["grade"]
                     self.info["game_level"] = pock["game_level"]
                     self.info["max_user_level"] = pock["max_user_level"]
                     self.info["id"] = pock["id"]
                     self.info["graph"] = pock["graph"]
                     self.info["agents"] = pock["agents"]
                     return self.info

