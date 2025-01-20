import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function missing_number(nums: number[]): number {
  const n = nums.length;
  const sum = nums.reduce((a, b) => a + b, 0)
  return Math.floor(n * (n + 1) / 2) - sum;
}

Deno.test("0268 Missing Number", () => {
  const test_cases: [number[], number][] = [
    [[3, 0, 1], 2],
    [[0, 1], 2],
    [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
    [[1], 0],
    [[0], 1],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums = test_case[0];
    const expected = test_case[1];

    const actual = missing_number(nums);
    assertEquals(actual, expected);
  }
});
