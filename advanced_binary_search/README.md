# advanced_binary_search

This interview algorithm project works with binary search. Basic binary search does not necessarily return the index of the first value in the array that matches the given value (if this value appears more than once). Advanced binary search not only finds the matching value, but returns the index of the first matching value.

[Advanced Binary Search](/advanced_binary_search/0-advanced_binary.c)

Write a function that searches for a value in a sorted array of integers.

- Prototype : `int advanced_binary(int \*array, size_t size, int value);`
- `array` is a pointer to the first element of the array to search in
- `size` is the number of elements in `array`
- `value` is the value to search for
- Your function must return the index where `value` is located
- You can assume that `array` will be sorted in ascending order
- If `value` is not present in `array` or if `array` is `NULL`, your function must return `-1`
- Every time you split the array, you have to print the new array (or subarray) you’re searching in (See example)
- You have to use recursion. You may only use one loop (`while`, `for`, `do while`, etc.) in order to print the array
