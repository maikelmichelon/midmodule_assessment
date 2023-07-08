#imperativeversion_floydsalgorithn

import sys
import itertools

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same, then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        
        # Check if the intermediate vertex provides a shorter path between start_node and end_node
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )
        



        
    # Print the resulting distance matrix
    for row in distance:
        print(row)






# Call the function with the graph
floyd(graph)
