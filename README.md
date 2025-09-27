11. Sparse Matrix
A sparse matrix is a matrix where most of the elements are zero. Storing it as a normal 2D array wastes memory because unnecessary zeros occupy space. For example, in a 100×100 matrix with only 10 non-zero values, most of the storage is wasted. To overcome this, sparse matrices are stored using efficient representations like triplet form (row, column, value of non-zero elements) or linked list representation. Sparse matrices are very useful in scientific computing, machine learning, and search engines, where data often has high dimensions but very few meaningful values. For example, in Natural Language Processing (NLP), word occurrence matrices are sparse because each document contains only a small subset of the total vocabulary. Using sparse representations saves both memory and computation time by avoiding unnecessary operations on zeros.
________________________________________
12. Class in C++
A class in C++ is a user-defined data type that combines variables (data members) and functions (methods) into a single unit. Unlike structures, classes support data hiding, encapsulation, inheritance, and polymorphism, making them the foundation of object-oriented programming (OOP). A class defines a blueprint, while objects are instances of a class. For example, a Car class may contain attributes like speed, color, and price, and methods like accelerate() or brake(). Access specifiers (public, private, protected) control data visibility. Constructors initialize objects, while destructors clean up memory. Classes enable modular, reusable, and secure code. In data structures, classes are used to implement stacks, queues, linked lists, and trees with better abstraction.
________________________________________
13. Searching (Linear and Binary Search)
Searching is the process of finding a specific element in a collection.
•	Linear Search: Sequentially checks each element until the target is found. Time complexity is O(n). It is simple but inefficient for large datasets.
•	Binary Search: Works on sorted arrays by repeatedly dividing the search range into halves. It compares the middle element with the target and discards half of the elements each step. Time complexity is O(log n). Binary search is much faster but requires sorted data.
Searching is fundamental in databases, file systems, and search engines. Optimizing search operations saves enormous time, especially with large data.
________________________________________
14. Sorting Algorithms
Sorting is arranging data in ascending or descending order. Common algorithms include:
•	Bubble Sort: Repeatedly swaps adjacent elements; O(n²).
•	Selection Sort: Selects the smallest/largest element each pass; O(n²).
•	Insertion Sort: Builds sorted list one element at a time; O(n²), efficient for small datasets.
•	Merge Sort: Divide-and-conquer method; O(n log n).
•	Quick Sort: Partition-based sorting; O(n log n) average, O(n²) worst case.
•	Heap Sort: Uses heap property; O(n log n).
Sorting is crucial in searching, optimization, and data organization. Efficient sorting algorithms improve performance in databases, libraries, and large-scale systems.
________________________________________
15. Hashing
Hashing is a technique that maps data to a fixed-size table (hash table) using a hash function. It provides O(1) average case time for searching, insertion, and deletion. However, collisions (two keys mapping to the same index) are common. Collision resolution strategies include chaining (linked lists at each index) and open addressing (probing for the next available slot). Hashing is widely used in dictionaries, password storage (with encryption), and caching systems. For example, search engines use hashing to store and retrieve webpages quickly. The efficiency of hashing depends on a good hash function that minimizes collisions and distributes data uniformly.
________________________________________
16. AVL Tree (Height Balanced Tree)
An AVL tree is a type of self-balancing Binary Search Tree (BST). For every node, the difference in heights of its left and right subtrees (balance factor) is at most 1. If the tree becomes unbalanced after insertion or deletion, it is restructured using rotations (LL, RR, LR, RL). This ensures the tree remains balanced, guaranteeing O(log n) time for searching, insertion, and deletion. AVL trees are crucial in databases and memory indexing, where balanced search is required. They provide faster lookups compared to unbalanced BSTs.
________________________________________
17. Heap Tree
A heap is a complete binary tree where each node satisfies the heap property:
•	Max Heap → Parent ≥ children.
•	Min Heap → Parent ≤ children.
Heaps are mainly used to implement priority queues where the highest (or lowest) priority element is always at the root. The most common application is Heap Sort, which sorts elements in O(n log n) time. Heaps are also used in graph algorithms like Dijkstra’s shortest path and Prim’s minimum spanning tree.
________________________________________
18. Huffman Tree
A Huffman tree is a special binary tree used for data compression. It assigns variable-length codes to input characters, with shorter codes for more frequent characters. For example, in text compression, common letters like ‘e’ or ‘a’ get shorter codes, while rare letters get longer codes. Huffman coding reduces file size without losing information, making it a lossless compression algorithm. It is widely used in ZIP files, JPEG images, and MP3 audio formats.
________________________________________
19. Graph Traversal (BFS and DFS)
Graph traversal means visiting all nodes of a graph systematically.
•	Breadth-First Search (BFS): Uses a queue to explore level by level. Useful in finding the shortest path in unweighted graphs.
•	Depth-First Search (DFS): Uses a stack (recursion) to explore as deep as possible before backtracking. Useful for cycle detection and topological sorting.
Both algorithms are widely applied in networking (routing), social networks (friend suggestions), and AI (pathfinding in games).
________________________________________
20. Topological Sorting
Topological sorting is used on Directed Acyclic Graphs (DAGs). It produces a linear ordering of vertices such that for every directed edge (u → v), vertex u appears before v. This is useful in task scheduling, where some tasks must be completed before others (e.g., course prerequisites in universities). It is implemented using DFS or Kahn’s Algorithm.
5. Array
An array is a collection of elements of the same data type stored in contiguous memory locations. It allows direct access to elements using indices, making retrieval very fast (O(1) time). Arrays can be one-dimensional (like a list of numbers) or multidimensional (such as matrices). They are widely used for storing data like student marks, employee records, or image pixels. However, arrays have fixed size and cannot dynamically expand, which limits flexibility. Operations such as traversal are simple, but insertion and deletion in the middle are costly as they require shifting elements. Arrays serve as the basis for implementing other data structures like stacks, queues, and matrices. They are efficient for random access but less suitable when frequent resizing or insertion is required.
________________________________________
6. Stack
A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. The element inserted last is removed first. The two main operations are push (insertion at the top) and pop (deletion from the top). Stacks can be implemented using arrays or linked lists. Applications of stacks are vast: they manage function calls in recursion, perform undo operations in text editors, evaluate mathematical expressions, and convert infix to postfix notation. They are also used in parsing expressions and backtracking algorithms (like maze-solving). The stack is simple yet powerful in solving real-life computational problems. Its limitation is fixed size when implemented using arrays, but this can be overcome using linked lists.
________________________________________
7. Queue
A queue is a FIFO (First In, First Out) data structure. The element inserted first is removed first, just like people waiting in a line. Basic operations include enqueue (insertion) and dequeue (removal). Variants include:
•	Circular Queue → Efficient use of space by connecting end to front.
•	Double-Ended Queue (Deque) → Insertion and deletion from both ends.
•	Priority Queue → Elements served based on priority, not position.
Queues are widely used in operating systems (process scheduling), printer spooling, and buffering in networks. Their simplicity makes them an integral part of real-world computing tasks.
________________________________________
8. Linked List
A linked list is a dynamic data structure made up of nodes, where each node contains data and a pointer to the next node. Unlike arrays, linked lists allow dynamic memory allocation and flexible insertion or deletion. Types include:
•	Singly Linked List → Each node points to the next.
•	Doubly Linked List → Nodes have pointers to both previous and next.
•	Circular Linked List → Last node connects back to the first.
Linked lists are useful when frequent insertion and deletion are required, such as in memory management and implementing stacks/queues. However, random access is inefficient (O(n)) compared to arrays.
________________________________________
9. Binary Tree
A binary tree is a hierarchical data structure where each node has at most two children, called the left and right child. Special types include Binary Search Tree (BST), where left child < root < right child, and AVL Tree, which maintains balance. Traversal methods include preorder, inorder, and postorder. Trees are used in expression parsing, searching, and file systems. They efficiently represent hierarchical data and enable faster search than linear structures. For instance, searching in a balanced BST takes O(log n), making trees fundamental in advanced data structures.
________________________________________
10. Graph
A graph consists of vertices (nodes) connected by edges. It can be directed or undirected, weighted or unweighted. Graphs represent real-world networks like social media, road maps, and communication systems. Common algorithms include Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra’s algorithm (shortest path), and Kruskal/Prim’s algorithm (minimum spanning tree). Graphs are powerful because they model relationships between objects. Applications include Google Maps (shortest routes), social networking (friend recommendations), and AI (state-space search). Graph theory is an essential foundation in computer science and real-world applications.

