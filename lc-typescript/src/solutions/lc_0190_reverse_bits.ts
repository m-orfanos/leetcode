import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function reverse_bits(n: number): number {
  let ans = 0;
  for (let i = 0; i < 32; i += 1) {
    ans = ans * 2 + n % 2;
    n = Math.floor(n / 2);
  }
  return ans;
}

Deno.test("0190 Reverse Bits", () => {
  const test_cases: [number, number][] = [
    [43261596, 964176192],
    [4294967293, 3221225471],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums = test_case[0];
    const expected = test_case[1];

    const actual = reverse_bits(nums);

    assertEquals(actual, expected);
  }
});
