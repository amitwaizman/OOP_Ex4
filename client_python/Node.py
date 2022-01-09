
class Node:

    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        self.weight = 0
        self.tag = 0
        self.edgein = {}
        self.edgeout = {}


    def __str__(self) -> str:
       return f"{self.id}:|edges out| {len(self.edgeout)} |edges in| {len(self.edgein)}"


    def __repr__(self) -> str:
      return f"{self.id}:|edges out| {len(self.edgeout)} |edges in| {len(self.edgein)}"


    def __lt__(self, other):
     return self.weight < other.weight