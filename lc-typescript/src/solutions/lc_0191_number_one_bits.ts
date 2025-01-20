import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function hamming_weight(n: number): number {
  let cnt = 0;
  while (n > 0) {
    cnt += n % 2;
    n = Math.floor(n / 2);
  }
  return cnt;
};

Deno.test("0191 Number of One Bits", () => {
  const test_cases: [number, number][] = [
    [11, 3],
    [128, 1],
    [2147483645, 30],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const n = test_case[0];
    const expected = test_case[1];

    const actual = hamming_weight(n);
    assertEquals(actual, expected);
  }
});
