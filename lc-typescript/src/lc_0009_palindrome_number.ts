import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function is_palindrome0(x: number): boolean {
  let copy = x;
  let rev = 0;
  while (copy > 0) {
    rev = rev * 10 + copy % 10;
    copy = Math.floor(copy / 10);
  }
  return x === rev;
}

function is_palindrome1(x: number): boolean {
  if (x < 0 || (x !== 0 && x % 10 == 0)) {
    return false;
  }

  let rev = 0;
  while (rev < x) {
    rev = (10 * rev) + (x % 10);
    x = Math.floor(x / 10);
  }

  return x === rev || x === Math.floor(rev / 10);
}

Deno.test("0009 Palindrome Number", () => {
  const test_cases: [number, boolean][] = [
    [1221, true],
    [121, true],
    [-121, false],
    [10, false],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const n = test_case[0];
    const expected = test_case[1];

    const actual0 = is_palindrome0(n);
    const actual1 = is_palindrome1(n);

    assertEquals(actual0, expected, `solution 1 - test case ${i}`);
    assertEquals(actual1, expected, `solution 2 - test case ${i}`);
  }
});
