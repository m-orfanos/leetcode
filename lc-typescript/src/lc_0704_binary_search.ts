import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function binary_search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;
    while (left <= right) {
        const mid = Math.floor(right - (right - left) / 2);
        if (target == nums[mid]) {
            return mid;
        } else if (target < nums[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

Deno.test("0740 Binary Search", () => {
    const test_cases: [number[], number, number][] = [
        [[-1, 0, 3, 5, 9, 12], 9, 4],
        [[-1, 0, 3, 5, 9, 12], 2, -1],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const nums = test_case[0];
        const target = test_case[1];
        const expected = test_case[2];

        const actual = binary_search(nums, target);
        assertEquals(actual, expected);
    }
});
