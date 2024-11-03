# Kruskal-Algorithm
The Software Requirements Specification (SRS) document for the implementation of Kruskal’s Algorithm defines the requirements and functional objectives of a program designed to compute the Minimum Spanning Tree (MST) of a graph. This document provides a structured overview of the problem, the proposed solution, and the expected functionality, covering both functional and non-functional requirements.

### Overview
The Kruskal’s Algorithm implementation aims to identify the minimum spanning tree within a given weighted, undirected graph. The graph is represented by vertices and edges, each edge having an associated weight. Kruskal’s algorithm is particularly useful in applications where minimizing connection costs is essential, such as in network design and circuit routing.

### Functional Requirements
The program shall allow the user to initialize a graph by defining the number of vertices and adding edges, with each edge specifying its two endpoints and the associated weight. The program will sort edges in ascending order of weight, ensuring that lower-weight edges are prioritized in the MST selection process. Additionally, the algorithm will utilize an optimized Union-Find data structure with path compression and union by rank to manage and merge sets efficiently, preventing cycles within the MST and thus enhancing performance. Upon successful computation, the MST is printed, displaying each edge along with its weight, following the format “u -- v == weight,” where “u” and “v” are the vertices connected by each edge.

### Non-Functional Requirements
The algorithm is designed to perform efficiently with a time complexity of \(O(E \log E + E \log V)\), where \(E\) represents the number of edges and \(V\) the number of vertices. The use of path compression and union by rank optimizations in the Union-Find operations ensures that the program can handle relatively large graphs with improved performance. 

### Constraints and Assumptions
The implementation assumes that the input graph is undirected and connected. It is further assumed that all edge weights are non-negative. The program will terminate once the MST contains exactly \(V-1\) edges, a requirement for the MST of a connected graph with \(V\) vertices.

### Conclusion
The Kruskal’s Algorithm program provides a reliable and efficient solution for computing the MST of a graph, fulfilling both functional and non-functional requirements. The implementation is intended for use cases that require minimal connection paths, optimized for scenarios such as networking and infrastructure planning. The output MST is expected to represent the least-cost connections, aiding users in decision-making and cost management.
