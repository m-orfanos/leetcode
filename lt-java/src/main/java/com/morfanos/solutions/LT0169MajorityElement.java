package com.morfanos.solutions;

class LT0169MajorityElement {

    static int majorityElement(int[] nums) {
        var num = nums[0];
        var cnt = 1;

        for (var i = 1; i < nums.length; i++) {
            if (nums[i] == num) {
                cnt += 1;
            } else {
                cnt -= 1;
            }
            if (cnt < 0) {
                num = nums[i];
                cnt = 0;
            }
        }

        return num;
    }

}
