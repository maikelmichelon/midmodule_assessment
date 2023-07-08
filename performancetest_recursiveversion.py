import sys
import itertools
import timeit

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])


def floyd_recursive(distance, intermediate, start_node, end_node):
    """
    Recursive implementation of Floyd's algorithm
    """
    if start_node == end_node:
        distance[start_node][end_node] = 0
        return

    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )

    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node)


def floyd(distance):
    """
    Implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        floyd_recursive(distance, intermediate, start_node, end_node)


# Performance test
def test_performance():
    distance = [row[:] for row in graph]  # Create a copy of the original graph

    # Measure the execution time of the floyd function - (function is executed 10000 times)
    execution_time = timeit.timeit(lambda: floyd(distance), number=10000)
    print(f"Execution time: {execution_time} seconds")


if __name__ == '__main__':
    test_performance()
