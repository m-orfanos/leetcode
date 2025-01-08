package com.morfanos;

class LT0977_SquaresSortedArray {

    static int[] sortedSquares(int[] nums) {
        var ans = new int[nums.length];
        var i = nums.length - 1;
        var lhs = 0;
        var rhs = nums.length - 1;
        while (lhs <= rhs) {
            var l = nums[lhs] * nums[lhs];
            var r = nums[rhs] * nums[rhs];
            if (l > r) {
                ans[i] = l;
                lhs += 1;
            } else {
                ans[i] = r;
                rhs -= 1;
            }
            i -= 1;
        }
        return ans;
    }

}
