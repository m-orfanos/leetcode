import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function count_bits1(n: number): number[] {
    const ans = [];
    for (let i = 0; i <= n; i += 1) {
        let curr = i;
        let cnt = 0;
        while (curr > 0) {
            cnt += curr % 2;
            curr = Math.floor(curr / 2);
        }
        ans.push(cnt);
    }
    return ans;
}

function count_bits2(n: number): number[] {
    const ans = [0];
    let offset = 1;
    for (let i = 1; i <= n; i += 1) {
        if (i == 2 * offset) {
            offset *= 2;
        }
        ans.push(ans[i - offset] + 1);
    }
    return ans;
}

function count_bits3(n: number): number[] {
    // dp[0]  =    0
    //
    // dp[1]  =    1 = dp[0] + 1
    //
    // dp[2]  =   10 = dp[1] + 0
    // dp[3]  =   11 = dp[1] + 1
    //
    // dp[4]  =  100 = dp[2] + 0
    // dp[5]  =  101 = dp[2] + 1
    //
    // dp[6]  =  110 = dp[3] + 0
    // dp[7]  =  111 = dp[3] + 1
    //
    // dp[8]  = 1000 = dp[4] + 0
    // dp[9]  = 1001 = dp[4] + 1
    //
    // dp[10] = 1010 = dp[5] + 0
    // dp[11] = 1011 = dp[5] + 1
    //
    // dp[12] = 1100 = dp[6] + 0
    // dp[13] = 1101 = dp[6] + 1
    //
    // dp[14] = 1110 = dp[7] + 0
    // dp[15] = 1111 = dp[7] + 1
    // ...
    const dp = [0];
    for (let i = 1; i <= n; i++) {
        dp.push(dp[Math.floor(i / 2)] + i % 2);
    }
    return dp;
}

Deno.test("0038 Counting Bits", () => {
    const test_cases: [number, number[]][] = [
        [0, [0]],
        [1, [0, 1]],
        [2, [0, 1, 1]],
        [3, [0, 1, 1, 2]],
        [4, [0, 1, 1, 2, 1]],
        [5, [0, 1, 1, 2, 1, 2]],
        [6, [0, 1, 1, 2, 1, 2, 2]],
        [7, [0, 1, 1, 2, 1, 2, 2, 3]],
        [8, [0, 1, 1, 2, 1, 2, 2, 3, 1]],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const n = test_case[0];
        const expected = test_case[1];

        const actual1 = count_bits1(n);
        const actual2 = count_bits2(n);
        const actual3 = count_bits3(n);

        assertEquals(actual1, expected, `failed for ${n}`);
        assertEquals(actual2, expected, `failed for ${n}`);
        assertEquals(actual3, expected, `failed for ${n}`);
    }
});
