import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function contains_duplicate1(nums: number[]): boolean {
    return new Set(nums).size !== nums.length;
}

function contains_duplicate2(nums: number[]): boolean {
    nums.sort();
    for (let i = 1; i < nums.length; i += 1) {
        if (nums[i - 1] === nums[i]) {
            return true;
        }
    }
    return false;
}

function contains_duplicate3(nums: number[]): boolean {
    const counter: { [key: number]: number } = {};
    for (const n of nums) {
        counter[n] = (counter[n] || 0) + 1;
        if (counter[n] > 1) {
            return true;
        }
    }
    return false;
}

Deno.test("0217 Contains Duplicate", () => {
    const test_cases: [number[], boolean][] = [
        [[1, 2, 3, 1], true],
        [[1, 2, 3, 4], false],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], true],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const nums = test_case[0];
        const expected = test_case[1];

        const actual1 = contains_duplicate1(nums);
        const actual2 = contains_duplicate2(nums);
        const actual3 = contains_duplicate3(nums);

        assertEquals(actual1, expected);
        assertEquals(actual2, expected);
        assertEquals(actual3, expected);
    }
});
