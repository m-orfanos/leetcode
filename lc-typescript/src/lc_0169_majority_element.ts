import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function majority_element1(nums: number[]): number {
    const counter = new Map<number, number>()
    for (const n of nums) {
        const cnt = (counter.get(n) || 0) + 1;
        if (cnt > Math.floor(nums.length / 2)) {
            return n;
        }
        counter.set(n, cnt);
    }
    return NaN;
}

function majority_element2(nums: number[]): number {
    let cnt = 1;
    let majority = nums[0];
    for (const n of nums) {
        cnt += majority === n ? 1 : -1;
        if (cnt === 0) {
            cnt = 1;
            majority = n;
        }
    }
    return majority;
}

Deno.test("0169 Majority Element", () => {
    const test_cases: [number[], number][] = [
        [[3, 2, 3], 3],
        [[2, 2, 1, 1, 1, 2, 2], 2],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const nums = test_case[0];
        const expected = test_case[1];

        const actual1 = majority_element1(nums);
        const actual2 = majority_element2(nums);

        assertEquals(actual1, expected);
        assertEquals(actual2, expected);
    }
});
