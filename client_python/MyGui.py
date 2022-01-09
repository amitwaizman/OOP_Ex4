
from client_python.AlgoPokemon import AlgoPokemon
from client_python.GraphAlgo import GraphAlgo
from client import Client
from pygame import gfxdraw
import pygame
from pygame import *
from pygame.constants import RESIZABLE
"""
Displays the game, object: algo=AlgoPokempn, client..
Picatsu represents a Pokemon with type-1 meaning src> dest.
Chermander represents a Pokemon with type 1 i.e. src> dest.
-function:

scale:Arranges the coordinates of the screen
min_max: Adjusts the resolution of the screen
torun: Loads the information and calls to AlgoPokemon.
draw:Draws the graph
drawAgent:Draws the agent.
drawpokemons:Draws the pokemons.
end: Prints game over at the end of the game.
onClicked:Ends the game when the stop button is pressed.
runAlgo:Running process of the Pokemon inlay algorithm.
display:Introducing the game.
Class Button: A button that displays the stop button on the graph

"""

radius = 15
WIDTH, HEIGHT = 926, 529
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.font.init()
FONT0= pygame.font.SysFont('MV Boli', 25, bold=True)
FONT = pygame.font.SysFont('MV Boli', 17, bold=True)
FONT1 = pygame.font.SysFont('MV Boli', 11, bold=True)
FONT2 = pygame.font.SysFont('MV Boli', 15, bold=True)
FONT3 = pygame.font.SysFont('MV Boli', 50, bold=True)




PORT = 6666
HOST = '127.0.0.1'
clock = pygame.time.Clock()


class gui:

    def __init__(self):
     self.algo=AlgoPokemon()
     self.client = Client()

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    min_x = min_y = max_x = max_y = 0

    def min_max(self, g: GraphAlgo):
        global min_x, min_y, max_x, max_y
        min_x = min(list(g.Graph.listNode.values()), key=lambda n: n.pos[0]).pos[0]
        min_y = min(list(g.Graph.listNode.values()), key=lambda n: n.pos[1]).pos[1]
        max_x = max(list(g.Graph.listNode.values()), key=lambda n: n.pos[0]).pos[0]
        max_y = max(list(g.Graph.listNode.values()), key=lambda n: n.pos[1]).pos[1]

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return self.scale(data, 50, screen.get_height() - 50, min_y, max_y)



    def torun(self):
        self.client.start_connection(HOST, PORT)
        graph_json = self.client.get_graph()
        self.algo.g.load_from_json(graph_json)
        pokemons = self.client.get_pokemons()
        self.algo.json_pokemons(pokemons)
        info = self.algo.jsoninfo(self.client.get_info())
        sorted(self.algo.listp, key=lambda x: sorted(x.routp.items()))
        age=info.get("agents")
        if (age>=1) and (len(self.algo.listp)>=1) :
            li=self.algo.listp
            j=0
            for i in range(age):
                  if j<len(li):
                   a = self.algo.firstLOC(li[j])
                   j=j+1
                   self.client.add_agent("{\"id\":" + str(a) + "}")
                  else:
                       center,y=self.algo.g.centerPoint()
                       self.client.add_agent("{\"id\":" + str(center) + "}")
        self.client.start()
        self.display(self.algo.g )




    def draw(self,g):
    # draw bu
     pygame.draw.rect(screen, button.color, button.rect)
     button_txt = FONT.render(button.txt, True, (0, 0, 0))
     screen.blit(button_txt, (button.rect.x, button.rect.y))

     txtt = FONT.render("TIME:"+self.client.time_to_end()+"", True, (0, 0, 0))
     screen.blit(txtt, (70, 0))

     info = self.algo.jsoninfo(self.client.get_info())

     txtt1 = FONT.render("MOVE:" + str(info.get("moves")) + "", True, (0, 0, 0))
     screen.blit(txtt1, (200, 0))

     txtt3= FONT0.render("LEVEL:" + str(info.get("game_level")) + "", True, (0, 0, 0))
     screen.blit(txtt3, (450, 10))


     txtt2 = FONT.render("GRADE:" + str(info.get("grade"))+ "", True, (0, 0, 0))
     screen.blit(txtt2, (310, 0))

     for n in g.Graph.listNode.values():
          x = self.my_scale(n.pos[0], x=True)
          y = self.my_scale(n.pos[1], y=True)

          # its just to get a nice antialiased circle
          gfxdraw.filled_circle(screen, int(x), int(y),
                                radius, Color(64, 80, 174))
          gfxdraw.aacircle(screen, int(x), int(y),
                           radius, Color(255, 255, 255))

          # draw the node id
          id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
          rect = id_srf.get_rect(center=(x, y))
          screen.blit(id_srf, rect)

      # draw edges
     for e in g.Graph.listEdge.values():
          # find the edge nodes
          src = next(n for n in g.Graph.listNode.values() if n.id == e.id1)
          dest = next(n for n in g.Graph.listNode.values() if n.id == e.id2)


          # scaled positions
          src_x = self.my_scale(src.pos[0], x=True)
          src_y = self.my_scale(src.pos[1], y=True)
          dest_x = self.my_scale(dest.pos[0], x=True)
          dest_y = self.my_scale(dest.pos[1], y=True)

          # draw the line
          pygame.draw.line(screen, Color(61, 72, 126),(src_x, src_y), (dest_x, dest_y))



    def DrawAgent(self, ag):
     for agent in ag:
        x = self.my_scale(agent.pos[0], x=True)
        y = self.my_scale(agent.pos[1], y=True)
        img = pygame.image.load("agent.jpg").convert()
        new1 = pygame.transform.scale(img, (50, 50))
        new1.set_colorkey(Color(255, 255, 255))
        screen.blit(new1, (int(x) - 5, int(y) - 5))
        id_srf = FONT2.render("id:"+str(agent.id), True, Color(0, 0, 0))
        rect = id_srf.get_rect(center=(x, y-20))
        screen.blit(id_srf, rect)

    def DrawPokemons(self, p):
     for pp in p:
       x = self.my_scale(pp.pos[0], x=True)
       y = self.my_scale(pp.pos[1], y=True)
       if pp.type>0:
        id_srf = FONT2.render("value:"+str(pp.value)+"", True, Color(48, 48, 0))
        rect = id_srf.get_rect(center=(x, y-15))
        screen.blit(id_srf, rect)
        img= pygame.image.load("pokemon1.jpg").convert()
        new=pygame.transform.scale(img,(50,50))
        new.set_colorkey(Color(255,255,255))
        screen.blit(new,(int(x), int(y)))
       else:
        id_srf = FONT2.render("value:"+str(pp.value), True, Color(48, 48, 0))
        rect = id_srf.get_rect(center=(x, y-15))
        screen.blit(id_srf, rect)
        img = pygame.image.load("pokemon2.png").convert()
        new1=pygame.transform.scale(img,(50,50))
        new1.set_colorkey(Color(255,255,255))
        screen.blit(new1,(int(x), int(y)))


    def end(self):
        run=True
        while run:
            imgg = pygame.image.load("screen.jpeg")
            imgg = pygame.transform.scale(imgg, ((screen.get_width(), screen.get_height())))
            screen.blit(imgg, ((0, 0)))
            txtt = FONT3.render("GAME OVER", True, (0, 0, 0))
            screen.blit(txtt, (450, 250))
            pygame.display.update()
            pygame.time.wait(5000)
            run=False
            exit(0)

    def onClicked(self,b):
        b.fun()


    def RunAlgo(self, agent):
        for a in agent:
            p, l = self.algo.algoP(a)
            d = self.algo.RouteSrc(p, a)
            for i in l:
                aa = int(a.dest)
                if aa == -1:
                    next_node = (i)
                    self.client.choose_next_edge(
                        '{"agent_id":' + str(a.id) + ', "next_node_id":' + str(next_node) + '}')
                    ttl = self.client.time_to_end()
                    print(ttl, self.client.get_info())
                    if (a.src == l[len(l) - 2]):
                        dis = self.algo.timetoMove(p, a)
                        d2 = dis + d - 0.0000000000000255
                        d1 = dis + d + 0.0000000000000255
                        while ((float(self.client.time_to_end())) >= d2 and (float(self.client.time_to_end())) <= d1):
                            clock.tick(10)
            info = self.algo.jsoninfo(self.client.get_info())
            if info.get("game_level") == 0:
                clock.tick(7.5)
                self.client.move()
            if info.get("game_level") == 9:
                clock.tick(12)
                self.client.move()
            else:
                clock.tick(9.5)
                self.client.move()

    def display(self,g:GraphAlgo=None):
        button.fun = self.client.stop_connection
        self.min_max(g)
        try:
         while self.client.is_running() == 'true':
            pokemons = self.client.get_pokemons()
            pokemons_obj = self.algo.json_pokemons(pokemons)
            agent = self.algo.json_Agents(self.client.get_agents())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(event.pos):
                      button.press()
                      if button.isClicked:
                       self.onClicked(button)
            imgg = pygame.image.load("screen.jpeg")
            imgg=pygame.transform.scale(imgg,((screen.get_width(), screen.get_height())))
            screen.blit(imgg,((0, 0)))
            self.draw(g)
            self.DrawAgent(agent)
            self.DrawPokemons(pokemons_obj)
            pygame.display.update()
            clock.tick(60)
            self.RunAlgo(agent)
        except Exception:
            self.end()




class Button:
    def __init__(self, rect: pygame.Rect, color,txt,fun=None):
        self.color = color
        self.txt = txt
        self.fun = fun
        self.rect = rect
        self.isClicked = False
    def press(self):
        self.isClicked = not self.isClicked


button = Button(pygame.Rect((0,0),(60,22)),(255,0,0),"STOP")

