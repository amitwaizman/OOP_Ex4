
class Agents:

 def __init__(self, id, value,src,dest,speed,pos):
    self.id=id
    self.value=value
    self.src=src
    self.d={}
    self.dest = dest
    self.speed = speed
    self.pos = pos
    self.rout=[]
    self.sumrout=0