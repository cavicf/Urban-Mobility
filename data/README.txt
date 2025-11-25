Data-Set: Urban Street Networks
Description: This data set contains urban street networks, corresponding to 1 square mile maps of the city.
Reference: P. Crucitti, V. Latora, and S. Porta. "Centrality measures in spatial networks of urban streets". Phys. Rev. E 73 (2006), 036125.
Additional-Info: This data set is part of the accompanying material of the book "Complex Networks: Principles, Methods and Applications", 
                 V. Latora, V. Nicosia, G. Russo, Cambridge University Press (2017) ISBN: 9781107103184

Filename: brasilia.net
Type: edge_list
Nodes: 179
Edges: 230 
Directed: no
Weighted: no
File-Format: "node_1 node2"
Comments: Brasilis network

Filename: brasilia_edge_info.txt
Type: end-points of road segments
File-Format: "edge_num node_1 X_1 Y_1 node_2 X_2 Y_2 length"
             where 'edge_num' is the number of the edge,
             'node_1' (resp. 'node_2') is the label of the first
             (reps. second) end-point, (X_1,Y_1) (resp.,
             (X_2,Y_2)) are the coordinates of the first
             (resp. second) endpoint, and 'length' is the length of
             the road segment connecting the two endpoints, in meters.