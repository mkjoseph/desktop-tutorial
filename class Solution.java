class Solution {
  int[] nums;  // This line declares an array called "nums" to store some numbers.
  int target;  // This line declares a variable called "target" to store a specific number.

  public int find_rotate_index(int left, int right) {
    if (nums[left] < nums[right])
      return 0;  // This function checks if the numbers in the "nums" array are rotated or not and returns an index.
    // If they are not rotated, it returns 0.
    // If they are rotated, it finds the index where the rotation occurs.
    // It does this by comparing numbers in the array.

    while (left <= right) {
      int pivot = (left + right) / 2;  // This line calculates the middle of the current range.
      if (nums[pivot] > nums[pivot + 1])
        return pivot + 1;  // If it finds a point where the numbers are in descending order, it returns that index.
      else {
        if (nums[pivot] < nums[left])
          right = pivot - 1;  // If not, it adjusts the range to the left or right based on comparisons.
        else
          left = pivot + 1;
      }
    }
    return 0;  // If it doesn't find a rotation point, it returns 0
  }

  public int search(int left, int right) {
    /*
    Binary search
    */
    while (left <= right) {
      int pivot = (left + right) / 2;  // This line calculates the middle of the current range.
      if (nums[pivot] == target)
        return pivot;  // If it finds the target number, it returns the index where the target is located.
      else {
        if (target < nums[pivot])
          right = pivot - 1;  // If not, it adjusts the range to the left or right based on comparisons.
        else
          left = pivot + 1;
      }
    }
    return -1;  // If it doesn't find the target number, it returns -1
  }

  public int search(int[] nums, int target) {
    this.nums = nums;  // This line assigns the input "nums" and "target" values to the class's variables.
    this.target = target;

    int n = nums.length;  // This line calculates the length of the "nums" array.

    if (n == 1)
      return this.nums[0] == target ? 0 : -1;  // If there is only one number in the array, it checks if it's the target.

    int rotate_index = find_rotate_index(0, n - 1);  // This line finds the rotation point (if any) in the array.

    // if target is the smallest element
    if (nums[rotate_index] == target)
      return rotate_index;  // If the target is found at the rotation point, it returns that index.

    // if array is not rotated, search in the entire array
    if (rotate_index == 0)
      return search(0, n - 1);  // If there's no rotation, it searches the whole array for the target.

    if (target < nums[0])
      // search in the right side
      return search(rotate_index, n - 1);  // If the target is smaller than the first element, it searches the right side.

    // search in the left side
    return search(0, rotate_index);  // Otherwise, it searches the left side of the array for the target.
  }
}
