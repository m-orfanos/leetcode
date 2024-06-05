import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function max_profit(prices: number[]): number {
    if (prices.length <= 1) {
        return 0;
    }

    let best = 0;
    let curr = 0;
    for (let i = 1; i < prices.length; i += 1) {
        const diff = prices[i] - prices[i - 1];
        curr += diff;
        if (curr < 0) {
            curr = 0;
        }
        if (curr > best) {
            best = curr;
        }
    }

    return best;
}

Deno.test("0121 Best Time to Buy and Sell Stocks", async (t) => {
    const test_cases: [number[], number][] = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        await t.step(`Test case #${i}`, () => {
            const test_case = test_cases[i];

            const nums = test_case[0];
            const expected = test_case[1];

            const actual = max_profit(nums);
            assertEquals(actual, expected);
        });
    }
});
