# 1. Quick Sort
Imagine you have a bunch of numbered cards in your hand, and you want to put them in order from smallest to largest. Here's how you might do it using Quick Sort:

1. Choose a card in your hand. This is called the "pivot".
2. Look at all the other cards in your hand, and divide them into two piles: one pile for cards that are smaller than the pivot, and another pile for cards that are larger than the pivot.
3. Put the cards in the "smaller than pivot" pile to the left of the pivot card, and the cards in the "larger than pivot" pile to the right of the pivot card.
4. Now you have three smaller piles: the pile to the left of the pivot (which should be smaller), the pile to the right of the pivot (which should be larger), and the pivot card in the middle.

Repeat steps 1-4 for each of the two smaller piles until everything is in order.

Now, let's see how we can implement Quick Sort using Python:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller_arr = [x for x in arr[1:] if x <= pivot]
        larger_arr = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller_arr) + [pivot] + quick_sort(larger_arr)
```
Here's how this implementation works:

1. If the input array has one or zero elements, return the array.
2. Otherwise, choose the first element of the array as the pivot.
3. Divide the rest of the array into two piles: one pile for elements smaller than the pivot, and another pile for elements larger than the pivot.
4. Recursively apply Quick Sort to each of the two piles and combine the sorted piles along with the pivot in the middle.
5. Return the sorted array.

And that's it! Quick Sort is a really useful algorithm for sorting large sets of data.

The time complexity of the Quick Sort algorithm is O(n log n) in the average case, where "n" is the number of elements in the input array. This is because the algorithm recursively partitions the input array into two smaller sub-arrays until each sub-array contains only one element. The partitioning process takes O(n) time, and the recursive calls are made log n times since each partition reduces the size of the array by half.

In the worst case, however, when the input array is already sorted in reverse order or in a similar configuration, the time complexity of Quick Sort becomes O(n^2). This is because each partition operation will only remove one element from the sub-array and, in the worst case, the algorithm will have to perform n partitions.

As for the space complexity, the implementation of Quick Sort using Python's list comprehensions will create two additional lists for each recursive call, resulting in a space complexity of O(n log n) in the average case. However, in the worst case, where the depth of the recursive calls is n, the space complexity will be O(n) due to the recursive function calls.

# 2. Merge Sort
Let's say you have a bunch of numbered cards in your hand, and you want to put them in order from smallest to largest. Here's how you might do it using Merge Sort:

1. First, you divide all the cards in half and give one half to a friend.
2. You both repeat step 1 until you each have only one card in your hand.
3. Then, you and your friend compare your cards and put them in order.
4. Now, you each have a sorted pile of cards in your hand.
5. You and your friend then take turns taking one card from your pile and putting it in a new pile, always taking the smallest card available.
6. Eventually, you will both have no cards left, and the new pile will be sorted from smallest to largest.

Now, let's see how we can implement Merge Sort using Python:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]

    return result
```
Here's how this implementation works:

1. If the input array has one or zero elements, return the array.

2. Otherwise, divide the array into two halves, and recursively apply Merge Sort to each half.
3. When each half is sorted, merge the two halves by comparing the smallest element of each half and adding the smaller element to a new list.
4. Continue the previous step until all elements have been added to the new list.
5. Return the sorted list.

And that's it! Merge Sort is a really useful algorithm for sorting large sets of data.

The Merge Sort algorithm has a time complexity of O(n log n) in all cases, where "n" is the number of elements in the input array. This means that the time it takes to sort an array of n elements grows logarithmically with respect to n.

The reason why the time complexity of Merge Sort is O(n log n) is because the algorithm recursively divides the input array into halves until it has only one or zero elements. This division process takes O(log n) time since the array is divided into halves at each recursive call.

After the array has been divided into its smallest components, the algorithm then merges the smaller arrays into larger ones in O(n) time, where n is the total number of elements in the smaller arrays.

Thus, the total time complexity of Merge Sort is the product of the time complexity of the division process and the merging process, which is O(n log n).

It is worth noting that Merge Sort is an efficient sorting algorithm and it is widely used in practice because of its stable performance and ability to handle large datasets.
