import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function sorted_squares0(nums: number[]): number[] {
  return (nums.map(x => x * x)).sort((a, b) => a - b);
}

function sorted_squares1(nums: number[]): number[] {
  const squares = Array(nums.length).fill(0);

  let left = 0;
  let right = nums.length - 1;

  let i = nums.length - 1;
  while (left <= right) {
    const lhs = nums[left] * nums[left];
    const rhs = nums[right] * nums[right];
    if (lhs > rhs) {
      squares[i] = lhs;
      left += 1;
    } else {
      squares[i] = rhs;
      right -= 1;
    }
    i -= 1;
  }

  return squares;
}

Deno.test("0977 Squares of Sorted Array", () => {
  const test_cases: [number[], number[]][] = [
    [[-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]],
    [[-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums0 = test_case[0];
    const nums1 = [...nums0];

    const expected = test_case[1];

    const actual0 = sorted_squares0(nums0);
    const actual1 = sorted_squares1(nums1);

    assertEquals(actual0, expected, `solution 1 - test case ${i}`);
    assertEquals(actual1, expected, `solution 2 - test case ${i}`);
  }
});
