package com.morfanos.solutions;

import java.util.HashMap;

class LT0001TwoSum {

    static int[] twoSum1(int[] nums, int target) {
        for (var i = 0; i < nums.length; i++) {
            for (var j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return null;
    }

    static int[] twoSum2(int[] nums, int target) {
        var cache = new HashMap<Integer, Integer>();
        for (var i = 0; i < nums.length; i++) {
            if (!cache.containsKey(target - nums[i])) {
                cache.put(nums[i], i);
            } else {
                return new int[] { cache.get(target - nums[i]), i };
            }
        }
        return null;
    }
}
