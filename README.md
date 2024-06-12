# Heuristic-based Path Planning

Heuristic-based Path Planning is a project dedicated to finding optimal routes efficiently. Applicable across robotics, transportation, and gaming, it offers robust and timely path planning solutions.

## Table of Contents
- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Kernighan-Lin (KL)](#kernighan-lin-kl)
  - [Fiduccia-Mattheyses (FM)](#fiduccia-mattheyses-fm)
  - [Multi-Level Graph Partitioning (MLGP)](#multi-level-graph-partitioning-mlgp)
- [Complexity Comparison](#complexity-comparison)
- [Usage](#usage)
- [Resources & References](#resources--references)
- [GitHub Repository](#github-repository)

## Introduction
Heuristic-based Path Planning focuses on developing efficient algorithms for pathfinding tasks. These solutions are vital in various fields such as robotics, where they aid in navigation, transportation for route optimization, and gaming for character movement.

## Algorithms

### Kernighan-Lin (KL)
The Kernighan-Lin algorithm is an efficient heuristic for finding good partitions in a graph. It is often used as a refinement step in other algorithms.

**Steps:**
1. Assign vertices to initial partitions randomly.
2. Iteratively swap pairs of vertices between partitions to improve the cut size.
3. Accept a swap only if it decreases the cut size.
4. Terminate when no more beneficial swaps can be found.

**Complexity:** O(n^2 * log n)

**Key Points:**
- Efficient heuristic for finding good partitions.
- Often used as a refinement step in other algorithms.
- Doesn't guarantee finding the optimal solution.

### Fiduccia-Mattheyses (FM)
The Fiduccia-Mattheyses algorithm prioritizes moving vertices with high gain scores to improve partitions.

**Steps:**
1. Assign vertices to initial partitions randomly.
2. Move single vertices between partitions to improve the cut size.
3. Prioritize moving vertices with high gain scores.
4. Update gain scores after each move.
5. Terminate when no more beneficial moves can be found.

**Complexity:** O(n * m)

**Key Points:**
- Often faster than KL in practice.
- Can produce high-quality partitions in a reasonable amount of time.
- Also doesn't guarantee finding the optimal solution.

### Multi-Level Graph Partitioning (MLGP)
MLGP is effective for large graphs, producing high-quality partitions through a multi-level approach.

**Steps:**
1. Coarsen the graph repeatedly by merging vertices and edges.
2. Partition the coarsest graph (often using KL or FM).
3. (Uncoarsen) Project the partition back to the original graph refining it at each level.

**Complexity:** O(n log n) (typically)

**Key Points:**
- Effective for large graphs.
- Can produce high-quality partitions for complex graph structures.
- Commonly used in practice for large-scale partitioning tasks.

## Complexity Comparison
| Algorithm                  | Complexity         | Strengths                     |
|----------------------------|--------------------|-------------------------------|
| Kernighan-Lin (KL)         | O(n^2 * log n)     | Efficient, good refinement tool |
| Fiduccia-Mattheyses (FM)   | O(n * m)           | Fast, high-quality partitions |
| Multi-Level Graph Partitioning (MLGP) | O(n log n) (typically) | Effective for large graphs, good quality |

## Usage
To use this project, you can find the source code in the GitHub repository provided below. The code includes implementations of the KL, FM, and MLGP algorithms, along with example usage for various applications in path planning.

## GitHub Repository
Find the source code and more details in our [GitHub Repository](https://github.com/erogluegemen/Heuristic-Path-Planning).
