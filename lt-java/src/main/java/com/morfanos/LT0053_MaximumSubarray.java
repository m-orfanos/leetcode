package com.morfanos;

class LT0053_MaximumSubarray {

    static int maxSubArray1(int[] nums) {
        var best = nums[0];
        var curr = nums[0];
        for (var i = 1; i < nums.length; i++) {
            curr = Math.max(nums[i], curr + nums[i]);
            best = Math.max(best, curr);
        }
        return best;
    }

    // **** Solution 2 **** //
    // Divide and conquer approach
    // Time complexity.: O(n*log(n))
    // Space complexity: O(log(n))
    private static int go(int[] nums, int lo, int hi) {
        // base case
        if (lo == hi) {
            return nums[lo];
        }

        var mid = lo + (hi - lo) / 2;

        // find the largest sum of elements
        // from mid to some point on the left
        var lcurr = 0;
        var lbest = Integer.MIN_VALUE;
        for (var i = mid; i >= lo; i--) {
            lcurr += nums[i];
            lbest = Math.max(lbest, lcurr);
        }

        // find the largest sum of elements
        // from mid to some point on the right
        var rcurr = 0;
        var rbest = Integer.MIN_VALUE;
        for (var i = mid; i <= hi; i++) {
            rcurr += nums[i];
            rbest = Math.max(rbest, rcurr);
        }

        // recursive step
        var best = lbest + rbest - nums[mid]; // nums[mid] is double counted
        var left = go(nums, lo, mid);
        var right = go(nums, mid + 1, hi);

        return Math.max(best, Math.max(left, right));
    }

    static int maxSubArray2(int[] nums) {
        return go(nums, 0, nums.length - 1);
    }

}
