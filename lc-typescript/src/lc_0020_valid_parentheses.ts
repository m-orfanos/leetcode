import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function is_valid(s: string): boolean {
  if (s.length % 2 !== 0) {
    return false;
  }

  const open_brackets = "({[";
  const matching_brackets: { [key: string]: string } = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  const stack: string[] = [];
  for (let i = 0; i < s.length; i += 1) {
    if (open_brackets.includes(s[i])) {
      stack.push(s[i]);
      continue;
    }

    if (stack.length === 0) {
      return false;
    }

    const ch = stack.pop()!;
    if (s[i] !== matching_brackets[ch]) {
      return false;
    }
  }

  return stack.length === 0;
}

Deno.test("0020 Valid Parenthesis", () => {
  const test_cases: [string, boolean][] = [
    ["()", true],
    ["()[]{}", true],
    ["(]", false],
    ["[", false],
    ["]", false],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const str = test_case[0];
    const expected = test_case[1];

    const actual = is_valid(str);

    assertEquals(actual, expected);
  }
});
