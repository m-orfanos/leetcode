package com.morfanos.solutions;

class LT0121BestTimeToBuyAndSellStock {

    static int maxProfit(int[] prices) {
        var current = 0;
        var best = 0;
        for (var i = 1; i < prices.length; i++) {
            current += prices[i] - prices[i - 1];
            if (current < 0) {
                current = 0;
            }
            if (current > best) {
                best = current;
            }
        }
        return best;
    }

}
