package com.morfanos.solutions;

import java.util.Arrays;

class LT0322CoinChange {

    static int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);

        var m = new int[amount + 1];
        Arrays.fill(m, Integer.MAX_VALUE);
        m[0] = 0;

        for (var a = 1; a < amount + 1; a++) {
            for (var c : coins) {
                if (a - c < 0) {
                    break;
                }
                if (m[a - c] != Integer.MAX_VALUE) {
                    m[a] = Math.min(m[a], 1 + m[a - c]);
                }
            }
        }

        if (m[m.length - 1] == Integer.MAX_VALUE) {
            return -1;
        }
        return m[m.length - 1];
    }

}
