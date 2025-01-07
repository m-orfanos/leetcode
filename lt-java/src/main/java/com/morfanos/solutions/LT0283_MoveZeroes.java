package com.morfanos.solutions;

class LT0283_MoveZeroes {

    static void moveZeroes(int[] nums) {
        // find first zero
        var zi = -1;
        for (var i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zi = i;
                break;
            }

        }

        // no zero found
        if (zi == -1) {
            return;
        }

        // swap zero with next non-zero, repeat
        // takes into account consecutive zeroes
        for (var i = zi + 1; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[zi] = nums[i];
                nums[i] = 0;
                zi += 1;
            }
        }
    }

}
