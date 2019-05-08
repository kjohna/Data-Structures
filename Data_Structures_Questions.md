Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1)

2. What is the runtime complexity of `dequeue`?
   O(1)

3. What is the runtime complexity of `len`?
   O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   O(n), n is height of bst if bst is perfectly unbalanced
   O(log(n)) if bst is perfectly balanced
2. What is the runtime complexity of `contains`?
   O(n), n is height of bst if bst is perfectly unbalanced
   O(log(n)) if bst is perfectly balanced
3. What is the runtime complexity of `get_max`?
   O(n), n is height of bst if bst is perfectly unbalanced with min as root. O(1) if max is root.
   O(log(n)) if bst is perfectly balanced

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log(n))

2. What is the runtime complexity of `_sift_down`?
   O(log(n))

3. What is the runtime complexity of `insert`?
   O(log(n)) - same as \_bubble_up

4. What is the runtime complexity of `delete`?
   O(log(n)) - same as \_bubble_up

5. What is the runtime complexity of `get_max`?
   O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   O(1)
3. What is the runtime complexity of `ListNode.delete`?
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    JS worst case is O(n)
    https://stackoverflow.com/questions/11514308/big-o-of-javascript-arrays
