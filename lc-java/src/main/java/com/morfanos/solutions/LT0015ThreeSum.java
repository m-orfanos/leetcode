package com.morfanos.solutions;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class LT0015ThreeSum {

    static List<List<Integer>> threeSum1(int[] nums) {
        // divide-and-conquer approach

        var pos = new HashMap<Integer, Integer>();
        var neg = new HashMap<Integer, Integer>();
        var zeroes = 0;
        for (var n : nums) {
            if (n > 0) {
                pos.put(n, 1 + pos.getOrDefault(n, 0));
            } else if (n < 0) {
                neg.put(n, 1 + neg.getOrDefault(n, 0));
            } else {
                zeroes += 1;
            }
        }

        var triples = new ArrayList<List<Integer>>();
        if (zeroes > 0) {
            // case (-p,0,p)
            for (var p : pos.keySet()) {
                if (neg.containsKey(-p)) {
                    triples.add(List.of(-p, 0, p));
                }
            }
            // case (0,0,0)
            if (zeroes > 2) {
                triples.add(List.of(0, 0, 0));
            }
        }

        // case (n1,n2,p)
        for (var n1 : neg.keySet()) {
            for (var n2 : neg.keySet()) {
                if (n1 > n2 || (n1 == n2 && neg.get(n1) < 2)) {
                    continue;
                }
                if (pos.containsKey(-(n1 + n2))) {
                    triples.add(List.of(n1, n2, -(n1 + n2)));
                }
            }

        }

        // case (n,p1,p2)
        for (var p1 : pos.keySet()) {
            for (var p2 : pos.keySet()) {
                if (p1 > p2 || (p1 == p2 && pos.get(p1) < 2)) {
                    continue;
                }
                if (neg.containsKey(-(p1 + p2))) {
                    triples.add(List.of(-(p1 + p2), p1, p2));
                }
            }
        }

        return triples;
    }

    static List<List<Integer>> threeSum2(int[] nums) {
        // two-pointer approach

        Arrays.sort(nums);

        var triples = new ArrayList<List<Integer>>();
        var prev = Integer.MIN_VALUE;
        for (var i = 0; i < nums.length; i++) {
            // skip duplicates
            if (nums[i] == prev) {
                continue;
            }
            prev = nums[i];

            var target = -nums[i];

            var l = i + 1;
            var r = nums.length - 1;
            while (l < r) {
                if (nums[l] + nums[r] < target) {
                    l += 1;
                } else if (nums[l] + nums[r] > target) {
                    r -= 1;
                } else {
                    triples.add(List.of(nums[i], nums[l], nums[r]));

                    l += 1;
                    r -= 1;

                    // skip duplicates
                    while (l < r && nums[l] == nums[l - 1]) {
                        l += 1;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r -= 1;
                    }
                }
            }
        }

        return triples;
    }

}
