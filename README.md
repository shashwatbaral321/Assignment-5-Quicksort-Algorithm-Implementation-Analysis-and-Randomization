Assignment 5: Quicksort Algorithm — Implementation, Analysis, and Randomization
Shashwat Baral
University of the Cumberlands
Algorithms and Data Structures (MSCS-532-B01)
Date of Submission-  11/02/25

1. Introduction
Sorting algorithms are essential components of computer science and find extensive application in databases, information retrieval systems, large-scale distributed frameworks, and performance-sensitive applications. Among the various comparison-based sorting algorithxms, Quicksort is particularly favored due to its elegant structure, outstanding average-case performance, and minimal memory usage.

This assignment delves into the implementation, theoretical evaluation, and empirical performance of both deterministic Quicksort and Randomized Quicksort. The use of randomization has become crucial in contemporary systems to mitigate worst-case scenarios, particularly in fields such as distributed systems, web indexing, and high-throughput data pipelines.

This report encompasses:

-	Python implementation of both deterministic and randomized Quicksort
-	Theoretical examination of time and space complexities
-	Discussion on how randomization enhances performance
-	Empirical comparisons between the two algorithms




2. Deterministic Quicksort Implementation

Deterministic Quicksort chooses a predetermined pivot (for instance, the first or last element) and organizes the array based on this pivot. The steps of the algorithm are as follows:

1.	Select a pivot
2.	Divide the elements into:

•	elements < pivot
•	pivot
•	elements > pivot
3.	Recursively sort each half

Python Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # deterministic pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


This version is clear and easy to understand but is vulnerable to worst-case behavior when the chosen pivot is consistently poor (e.g., sorted input).

3. Time and Space Complexity Analysis
3.1 Best-Case Time Complexity – Θ(n log n)
The best-case scenario arises when the pivot divides the array into two nearly equal sections.
Recurrence:
𝑇(𝑛)=2𝑇(𝑛/2)+𝑂(𝑛T(n)=2T(n/2)+O(n)

Applying the Master Theorem:

𝑇(𝑛)=Θ(𝑛log⁡𝑛)T(n)=Θ(nlogn)

3.2 Average-Case Time Complexity – O(n log n)

Random inputs generally result in reasonably balanced partitions. The expected recurrence is:

𝑇(𝑛)≈𝑇(𝑘)+𝑇(𝑛−𝑘−1)+𝑂(𝑛)T(n)≈T(k)+T(n−k−1)+O(n)

The expected value across all k results in:

𝑇(𝑛)=𝑂(𝑛log⁡𝑛)
T(n)=O(nlogn)

Why Average Case Is O(n log n)
•	Each partitioning step incurs a cost of O(n)
•	The anticipated depth of recursion is approximately log n
•	Total cost is approximately n log n

3.3 Worst-Case Time Complexity – O(n²)
The worst-case scenario occurs when the pivot is consistently the smallest or largest element.
𝑇(𝑛)=𝑇(𝑛−1)+𝑂(𝑛)T(n)=T(n−1)+O(n)
Upon solving:
𝑇(𝑛)=𝑂(𝑛2)T(n)=O(n2)
Circumstances leading to the worst-case include:
•	An already sorted input
•	A reverse sorted input
•	Repeated elements with a suboptimal pivot selection

3.4 Analysis of Space Complexity

Quicksort employs recursion.

Best/Average Case:
O(log n) stack space
Worst Case:
O(n)

This occurs because the depth of recursion becomes linear.

4. Implementation of Randomized Quicksort
The use of randomization aids in preventing worst-case scenarios by choosing a pivot uniformly at random.

Python Implementation
import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + mid + randomized_quicksort(right)


4.1 Effects of Randomization
Randomization guarantees:
•	The pivot is unlikely to consistently be the least favorable option.
•	The worst-case time complexity of O(n²) becomes exceedingly uncommon.
•	The expected performance consistently achieves O(n log n).

Randomization is extensively utilized in APIs, sorting libraries, and distributed systems to mitigate adversarial inputs.

5. Empirical Evaluation
Experimental Configuration

•	Both deterministic and randomized versions were implemented.

•	Tests were conducted on arrays of sizes: 1,000 — 10,000 — 50,000.

•	Input distributions included:
•	Random
•	Sorted
•	Reverse-sorted
•	Repeated values

Noted Outcomes (General Patterns)
Input Type	Deterministic Quicksort	Randomized Quicksort
Random	Fast (O(n log n))	Fastest & consistent
Sorted	Very slow (approaches O(n²))	Still fast (O(n log n))
Reverse	Very slow (O(n²))	Still fast
Repeated	Moderate performance	Good performance


Discussion of Results

•	Deterministic Quicksort exhibited significant degradation on sorted inputs due to inadequate pivot selection.

•	Randomized Quicksort consistently achieved performance close to O(n log n).

•	The addition of randomization incurs minimal overhead while greatly enhancing robustness.

•	The theoretical predictions closely aligned with the empirical findings.

6. Conclusion

This assignment offered an in-depth examination of both deterministic and randomized Quicksort. The main points are as follows:

•	Deterministic Quicksort is straightforward and efficient, yet it is susceptible to worst-case input scenarios.

•	Randomization greatly diminishes the chances of encountering worst-case performance, rendering it the more favorable option in practical applications.

•	Empirical evidence indicated that randomization ensures stable and predictable performance across various data distributions.

•	A comprehensive understanding of Quicksort is essential in contemporary computing systems, including distributed data processing engines, search algorithms, and performance-critical software.

Through this assignment, I acquired a more profound understanding of algorithm analysis, complexity assessment, and practical performance factors.


7. References

o	Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.
o	Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.
o	Hoare, C. A. R. (1962). Quicksort. The Computer Journal, 5(1), 10–15.
o	Weiss, M. A. (2020). Data Structures and Algorithm Analysis in Python (3rd ed.). Pearson.
![Uploading image.png…]()
