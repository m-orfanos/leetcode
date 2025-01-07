package com.morfanos.solutions;

class LT0268_MissingNumber {

    static int missingNumber(int[] nums) {
        // sum(0..n) = n*(n+1)/2
        var sum = 0;
        var max = Integer.MIN_VALUE;
        for (var n : nums) {
            sum += n;
            if (max < n) {
                max = n;
            }
        }

        if (max == nums.length - 1) {
            max += 1;
        }

        var e = max * (max + 1) / 2;

        return e - sum;
    }

}
