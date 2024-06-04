import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function two_sum(nums: number[], target: number): number[] {
  const nums_map: Map<number, number> = new Map();
  for (let i = 0; i < nums.length; i += 1) {
    if (nums_map.has(nums[i])) {
      return [nums_map.get(nums[i])!, i];
    }
    nums_map.set(target - nums[i], i);
  }
  return [];
}

Deno.test("0001 Two Sum", async (t) => {
  const test_cases: [number[], number, number[]][] = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    await t.step(`Test case #${i}`, () => {
      const test_case = test_cases[i];

      const nums = test_case[0];
      const target = test_case[1];
      const expected = test_case[2];

      const actual = two_sum(nums, target);
      assertEquals(actual, expected);
    });
  }
});