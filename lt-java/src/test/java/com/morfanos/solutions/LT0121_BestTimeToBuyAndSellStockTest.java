package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0121_BestTimeToBuyAndSellStock.maxProfit;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0121_BestTimeToBuyAndSellStockTest {

    @Test
    void maxProfit1() {
        var prices = toArray(7, 1, 5, 3, 6, 4);
        var ans = maxProfit(prices);
        assertEquals(5, ans);
    }

}
