# oop_Ex4#
#WELCOM TO THE POKEMON GAMEֳֳ#
class:
---------
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
* TSP:finds the shortest path that visits all the nodes in the list <br />
   In this function we checked the short path between all 2 vertices if the short path contains all the vertices in the list and is the minimum we returned this path, <br />        and the minimum distance. If it did not exist, we checked for every 2 consecutive vertices in the list the short route between them and returned the short route and   <br />    the minimum distance<br />
* centerPoint:finds the node that has the shortest distance to it's farthest node. <br />
   This function we used a Dijkstra We sent each a node to Dijkstra and checked what the maximum distance is for each nodes and we checked if this distance is the    <br />        minimum and we returned from all the maximum distances the minimum distance and the nodes that holds it. <br />
   If there is a node from which the Dijkstra returned an empty dict, that is, there is no way to reach it from other nodes, that is, the graph is not linked. We       <br />      returned -1 and infinity 
* plot_graph:plots the graph. <br />
* <br />
-We also implemented auxiliary functions: <br />
*changeMaxVal:Updates to all weight of nodes to infinite <br />
*isFound: checks if the nodes in list a are in list b. <br />
*Dijkstra: <br />
We implemented the Dijkstra algorithm the algorithm gets a nodes src and updates שccording to the algorithm the weight of each nodes the minimum distance from src to the node,the algorithm returns a dictionary representing for each nodes the node that preceding in the path from the src to the node.<br />
***TestDiGraph:***  <br />
A class to check the DiGraph by unittest <br />
***TestGraphAlgo:*** <br />
A class to check the DiGraph by unittest  <br />
***TestComperison:*** <br />
A class that test the algorithms on A0-A5 file.  <br />
***TestBigNUM:*** <br />
A class that test the algorithms on 1000,10000,100000.  <br />
***MyGui***  <br />
This class displays the graph that is toned from the Jason file via the main in the class by the load function. <br />
When we run the main the directed graph will be displayed: <br />
![image](https://user-images.githubusercontent.com/93676748/147508005-a0aeb7aa-cac5-4959-8d24-5982e555f21e.png)
 <br />
By pressing the center button you can see the center of the graph (painted in purple). <br />

![image](https://user-images.githubusercontent.com/93676748/147507925-6269c39d-d0c5-41de-aca5-a8fe9d00ea9b.png)
 <br />
After we ran check1:
<br />
![image](https://user-images.githubusercontent.com/93676748/147505134-d0a5e029-1952-41ab-954e-b7c4af31dc3d.png)
<br />
After we ran check2:
<br />
![image](https://user-images.githubusercontent.com/93676748/147505237-e5ad860d-8ad4-43af-9ca1-eaebec42e473.png)

UML
-----
![image](https://user-images.githubusercontent.com/93676748/147506541-6f9021f8-b7f3-468f-9f04-23e6e2f2b98e.png)




