package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0121BestTimeToBuyAndSellStock.maxProfit;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0121BestTimeToBuyAndSellStockTest {

    @Test
    void maxProfit1() {
        var prices = to1DArray(7, 1, 5, 3, 6, 4);
        var ans = maxProfit(prices);
        assertEquals(5, ans);
    }

}
