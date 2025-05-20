package com.morfanos.solutions;

class LT0136SingleNumber {

    static int singleNumber(int[] nums) {
        var single = nums[0];
        for (var i = 1; i < nums.length; i++) {
            single ^= nums[i];
        }
        return single;
    }

}
