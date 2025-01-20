import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function move_zeroes(nums: number[]): void {
  nums.sort((a, b) => {
    if (a === 0) {
      return Number.POSITIVE_INFINITY;
    } else if (b === 0) {
      return Number.NEGATIVE_INFINITY;
    } else {
      return 0;
    }
  });
}

Deno.test("0283 Move Zeroes", () => {
  const test_cases: [number[], number[]][] = [
    [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
    [[0], [0]],
    [[2, 1], [2, 1]],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums = test_case[0];
    const expected = test_case[1];

    move_zeroes(nums);
    assertEquals(nums, expected);
  }
});
