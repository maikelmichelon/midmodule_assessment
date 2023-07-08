#unittest_forcodeusingimperative

import sys
import itertools
import unittest

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
    Implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same, then the distance is zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        
        # Check if the intermediate vertex provides a shorter path between start_node and end_node
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )
        

class FloydTestCase(unittest.TestCase):

    def test_floyd_algorithm(self):
        distance = [row[:] for row in graph]  # Create a copy of the original graph
        floyd(distance)
        expected_result = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        self.assertEqual(distance, expected_result)


if __name__ == '__main__':
    unittest.main()
