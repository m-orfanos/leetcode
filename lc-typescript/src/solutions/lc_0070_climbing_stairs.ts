import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function climb_stairs1(n: number): number {
    const factorial = function fact() {
        const mem: { [key: number]: number } = {};
        return (n: number) => {
            if (n <= 1) {
                return 1;
            }

            if (mem[n] != null) {
                return mem[n];
            }

            mem[n] = n * factorial(n - 1);
            return mem[n];
        }
    }();

    let total = 0;
    let cnt1 = n;
    let cnt2 = 0;
    while (cnt1 >= 0 && cnt2 >= 0) {
        const top = factorial(cnt1 + cnt2);
        const bottom = factorial(cnt1) * factorial(cnt2);
        total += top / bottom;

        cnt1 -= 2;
        cnt2 += 1;
    }

    return total;
}

function climb_stairs2(n: number): number {
    let a = 0;
    let b = 1;
    while (n > 0) {
        const t = b;
        b += a;
        a = t;
        n -= 1;
    }
    return b;
}

Deno.test("0070 Climbing Stairs", () => {
    const test_cases = [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 5],
        [5, 8],
        [6, 13],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const n = test_case[0];

        const expected = test_case[1];

        const actual1 = climb_stairs1(n);
        const actual2 = climb_stairs2(n);

        assertEquals(actual1, expected, `failed soln#1 for n=${n}`);
        assertEquals(actual2, expected, `failed soln#2 for n=${n}`);
    }
});
