class Edge:
  def __init__(self, id1, id2, weight):
        self.weight = weight
        self.id1 = id1
        self.id2 = id2

  def __repr__(self) -> str:
    return f"id1={self.id1} id2={self.id2} weight={self.weight}"