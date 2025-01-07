package com.morfanos.solutions;

class LT0704_BinarySearch {

    static int search(int[] nums, int target) {
        var lhs = 0;
        var rhs = nums.length - 1;
        while (lhs <= rhs) {
            var mid = lhs + (rhs - lhs) / 2;
            var n = nums[mid];
            if (n < target) {
                lhs = mid + 1;
            } else if (n > target) {
                rhs = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

}
