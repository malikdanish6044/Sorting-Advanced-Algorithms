# Sorting-Advanced-Algorithms
Performance analysis of core sorting algorithms
1. Selection Sort
Selection Sort is an in place comparison based algorithm. It maintains a sorted and unsorted region, repeatedly picking the minimum element from the unsorted side.
2. Bubble Sort
Bubble Sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
3. Quick Sort
Quick Sort is a divide and conquer algorithm that picks an element as a 'pivot' and partitions the array around it.
4. Merge Sort
Merge Sort is a stable, divide and conquer algorithm that recursively splits the list and merges the sorted sub lists.
Comprehensive Analysis
Comparative Performance:
For the small dataset (n=5), Bubble Sort and Insertion Sort were fastest on sorted data due to early exit optimizations. At n=100, Merge Sort dominated the field. While O(n^2) algorithms performed nearly 5,000 comparisons, Merge Sort completed the task with significantly fewer operations.

Effect of Input Order:
Input order impacts Bubble Sort and Quick Sort significantly. Bubble Sort drops to O(n) for sorted arrays. Selection Sort remains indifferent to order, performing the same comparisons regardless. Quick Sort underperformed on sorted arrays due to the pivot selection strategy.

Memory Usage:
Merge Sort utilized the most auxiliary space (O(n)). Selection and Bubble sort were the most efficient in terms of memory, operating entirely in place (O(1)).
Conclusion
For small datasets, simpler in place algorithms like Bubble or Selection Sort are sufficient. For large scale data, the logarithmic efficiency of Merge Sort is essential despite higher memory requirements.
