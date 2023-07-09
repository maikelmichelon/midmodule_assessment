# Floyd's Algorithm Implementation

This repository contains an implementation of Floyd's algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. It includes both a recursive and an imperative version of the algorithm, along with corresponding unittest and performance tests.

## Algorithm Overview

Floyd's algorithm, also known as the Floyd-Warshall algorithm, is a graph algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. It works by iteratively updating a distance matrix to find the shortest path between any two vertices. The algorithm has applications in various domains, such as network routing and traffic optimization.

## Files

- `Floyd’s algorithm_programforrecursive.py`: Contains the recursive implementation of Floyd's algorithm.
- `Floyd’s algorithm_programforimperative.py`: Contains the imperative implementation of Floyd's algorithm.
- `performancetest_programforrecursive.py`: Performance test for the recursive version.
- `performancetest_programforimperative.py`: Performance test for the imperative version.
- `unitest_programforimperative.py`: unit test for the imperative version.
- `unittest_programforrecursive.py`: unit test for the recursive version.


## Usage

To use the implementation and run the algorithms and tests, follow these steps:

1. Clone the repository or download the necessary files.

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt and navigate to the directory containing the files.

4. Feel free to modify the file to test the algorithms with different graphs. Adjust the weights and connectivity of the vertices as needed.

## Performance Considerations

Both implementations include performance tests to measure the execution time of the algorithm for a given graph. The performancetest_programforrecursive.py and performancetest_programforimperative.py files contain the necessary code to run these tests.

## Testing

The implementations also include unit tests to verify the correctness of the algorithm. The unittest_programforrecursive.py and unitest_programforimperative.py files contain the test cases.

## Contributions

Contributions to this repository are welcome. If you find any issues, have suggestions for improvements, or would like to add new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


