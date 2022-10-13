Quick Sort
Sort Color
Merge Sort
Merge interval
Range module
Bubble game & balloon game
Minimum number of arrow to burst balloons
Sort list
Insertion Sort
Insertion Sort List
Largest number - Sorting via custom comparator

Binary Search
Search in rotated array
Search insert position
Search in 2D matrix
Search in 2D matrix-ii
Find minimum in rotated sorted array
Find minimum in rotated sorted array-ii
Linked List
Add two numbers
Remove nth element from the end of the list
Merge k sorted list
Swap nodes in pair

Stack
Monolithic stack
Tapping rain water
Largest rectangle
Next greater element
Implement stack using Queue
Circular Tour Problem
Implement LRU Cache
Largest Rectangle in the Histogram

Queue
Find Right Side view of binary tree
Find sum of rectangle no larger than k

Graph
Kahn’s Indegree method for cycle detection
Topological sort for cycle detection
Graph Coloring to detect cycle detection
Detect cycle in directed & undirected graph
Possible Bipartition(Bipartite graph)
Course Schedule (i & ii)
Cheapest Flights within k-stops

Game Theory




String 
LCP Array
Suffix array


Rabin Karp algorithm - pattern matching algorithm
Take a rolling hash function in the following format 10^m-1 + 10^m-2 + ….+ 10^0 here m is the length of pattern string
If you want to avoid the integer overflow then you can mod with the max int value
Compare sum with the pattern hash sum if it's matching then compare individual characters. If all individual characters are matching then it's a match otherwise move to the next character.
Rolling hash function
- spurious hits
  Spurious hits means for the same hash value different strings are possible and we are still checking whether it is matching or not in the string


Longest Prefix Suffix
initialize lps[0] and len as 0. If pat[len] and pat[i] match, we increment len by 1 and assign the incremented value to lps[i]. If pat[i] and pat[len] do not match and len is not 0, we update len to lps[len-1] else set lps[i] = 0 and increment i by 1.

KMP String Matching Algorithm
First we calculate LPS of pattern string, then take 2 pointers i = j = 0, search character wise if character is not matching then check whether j != 0 if yes then set j = lps[j-1] else increment i by 1. If j == M where M is length of pattern then it's a match



Lexicographically inc/dec - dictionary order
