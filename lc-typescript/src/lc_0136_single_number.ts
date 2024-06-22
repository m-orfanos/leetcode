import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function single_number(nums: number[]): number {
  return nums.reduce((acc, curr) => acc ^ curr, 0);
}

Deno.test("0136 Single Number", () => {
  const test_cases: [number[], number][] = [
    [[2, 2, 1], 1],
    [[4, 1, 2, 1, 2], 4],
    [[1], 1],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums = test_case[0];
    const expected = test_case[1];

    const actual = single_number(nums);
    assertEquals(actual, expected);
  }
});
