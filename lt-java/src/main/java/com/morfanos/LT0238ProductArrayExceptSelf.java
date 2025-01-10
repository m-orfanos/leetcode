package com.morfanos;

import java.util.Arrays;

class LT0238ProductArrayExceptSelf {

    static int[] productExceptSelf(int[] nums) {
        var n = nums.length;

        var lhs = new int[n];
        Arrays.fill(lhs, 1);
        lhs[0] = nums[0];

        var rhs = new int[n];
        Arrays.fill(rhs, 1);
        rhs[n - 1] = nums[n - 1];

        for (var i = 1; i < n; i++) {
            lhs[i] = lhs[i - 1] * nums[i];
            rhs[n - 1 - i] = rhs[n - 1 - i + 1] * nums[n - 1 - i];
        }

        var ans = new int[n];
        ans[0] = rhs[1];
        ans[n - 1] = lhs[n - 1 - 1];
        for (var i = 1; i < n - 1; i++) {
            ans[i] = lhs[i - 1] * rhs[i + 1];
        }

        return ans;
    }

}
