# oop_Ex4#
WELCOM TO THE POKEMON GAME
--------------------------
The aim of the game is to collect as many Pokemon as possible in less move (maximum 10 moves per second) <br />
![image](https://user-images.githubusercontent.com/93676748/148678172-701e4099-6560-4f17-944e-ab5f318d4664.png) <br />
class:
---------
**Agents:**<br />
A class that represents agents data, object: id, value, src, dest,speed and pos.<br />
**pokemons:** <br />
A class that represents pokemons data, object: value, type, pos and tag.<br />
**AlgoPoknem:**<br />
A class for the implementation of Pokemon placement to the agent, object: listp- list of pokemons, listA- list of agents, info, g-GraphAlgo and client. <br />
-function: <br />
*linel: The function gets 2 nodes and pos calculates the straight equation of the 2 nodes and returns true if the pos is on this equation and false otherwise. <br />
*timeall:Returns the time it takes for the agent to reach Pokemon when it's in edge's src. <br />
*timetoMove: Returns the time it takes for the agent to reach Pokemon <br />
*distance: Calculates the distance from the agent to the Pokemon <br />
*findEdge: Finds the side that the Pokemon is on <br />
*theRout: Calculates the distance of an agent to each Pokemon <br />
*routrSrc: Calculates the route to the src of the edge the Pokemon is on <br />
*firstLOC:Returns the position of the src of the edge the Pokemon is on <br />
*algoP: Places to the agent the Pokemon closest to him <br />
*json_pokemons: Loading Pokemon from the server <br />
*json_Agents: Loading agent from the server <br />
*jsoninfo: Loading info from the server <br />

**client:** <br />
communicating with the "server" <br />
***MyGui***  <br />
Displays the game, object: algo=AlgoPokempn, client.. <br />
Picatsu represents a Pokemon with type-1 meaning src> dest. <br />
Chermander represents a Pokemon with type 1 i.e. src> dest. <br />
-function: <br />
* scale:Arranges the coordinates of the screen <br />
* min_max: Adjusts the resolution of the screen <br />
* torun: Loads the information and calls to AlgoPokemon. <br />
* draw:Draws the graph <br />
* drawAgent:Draws the agent. <br />
* drawpokemons:Draws the pokemons. <br />
* end: Prints game over at the end of the game. <br />
* onClicked:Ends the game when the stop button is pressed. <br />
* runAlgo:Running process of the Pokemon inlay algorithm. <br />
* display:Introducing the game. <br />
* Class Button: A button that displays the stop button on the graph

**main:**<br />
Run the game <br />
**Node:**<br />
A class that represents node data, object: id, pos, weight, tag and dict to edge in and dict to edge out. <br />
**Edge:** <br />
A class that represents edges data object: weight id1=src, id2=dest. <br />
**DiGraph:** <br />
A class that implements the interface GraphInterface, object: sizeNode, sizeEdge, listNode, listEdge, mc. <br />
-function: <br />
* v_size:returns the number of nodes in this graph <br />
* e_size:returns the number of edges in this graph <br />
* get_all_v:return a dictionary of all the nodes in the Graph. <br />
* all_in_edges_of_node: return a dictionary of all the nodes connected to (into) node_id. <br />
* all_out_edges_of_node:return a dictionary of all the nodes connected from node_id. <br />
* get_mc:returns the current version of this graph. <br />
* add_edge:adds an edge to the graph. <br />
* add_node:adds a node to the graph. <br />
* remove_node:removes a node from the graph. <br />
* remove_edge:removes an edge from the graph. <br />

**GraphAlgo:** <br />
A class that implements the interface GraphAlgoInterface, object: DiGraph Graph. <br />
-function: <br />
* get_graph:return the graph that the algorithm works on. <br />
* load_from_json: loads a graph from a json file. <br />
* save_to_json: saves the graph in JSON format to a file <br />
* shortest_path:returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm <br />
   We used this function in Dijkstra We sent the src node to Dijkstra and according to the parents dict we received we went <br />
   from the destination node to reach the source and returned the weight of the node and the and list of the route. <br />
   If there is no route, we returned an empty list and infinite. <br />
* centerPoint:finds the node that has the shortest distance to it's farthest node. <br />
   This function we used a Dijkstra We sent each a node to Dijkstra and checked what the maximum distance is for each nodes and we checked if this distance is the    <br />        minimum and we returned from all the maximum distances the minimum distance and the nodes that holds it. <br />
   If there is a node from which the Dijkstra returned an empty dict, that is, there is no way to reach it from other nodes, that is, the graph is not linked. We       <br />      returned -1 and infinity 
-We also implemented auxiliary functions: <br />
*changeMaxVal:Updates to all weight of nodes to infinite <br />
*isFound: checks if the nodes in list a are in list b. <br />
*Dijkstra: <br />
We implemented the Dijkstra algorithm the algorithm gets a nodes src and updates ??ccording to the algorithm the weight of each nodes the minimum distance from src to the node,the algorithm returns a dictionary representing for each nodes the node that preceding in the path from the src to the node.<br />
***Test:***  <br />
A class to check the AlgoPokmen by unittest <br />
**TestDiGraph:** <br />
A class that test DiGraph function. <br />
**TestGraphAlgo:** <br />
A class that test GraphAlgo function. <br />

In addition, on the wiki page you can see a full explanation of how to run and a video of the game <br />
--------------------------------------------------------------------------------------------------
UML 
-----
![image](https://user-images.githubusercontent.com/93676748/148682245-038dac57-5301-4551-8e54-20a20776753c.png) <br />

Results
-------
| level | grade | moves |
| ----- | ----- | ----- |
| 0     | 147   | 199   |
| 1     | 423   | 461   |
| 2     | 158   | 224   |
| 3     | 606   | 463   |
| 4     | 175   | 225   |
| 5     | 541   | 441   |
| 6     | 79    | 244   |
| 7     | 315   | 483   |
| 8     | 85    | 235   |
| 9     | 497   | 557   |
| 10    | 105   | 224   |
| 11    | 998   | 516   |
| 12    | 40    | 244   |
| 13    | 300   | 516   |
| 14    | 226   | 264   |
| 15    | 349   | 457   |



