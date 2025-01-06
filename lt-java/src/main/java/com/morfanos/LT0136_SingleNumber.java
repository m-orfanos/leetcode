package com.morfanos;

class LT0136_SingleNumber {

    static int singleNumber(int[] nums) {
        var single = nums[0];
        for (var i = 1; i < nums.length; i++) {
            single ^= nums[i];
        }
        return single;
    }

}
