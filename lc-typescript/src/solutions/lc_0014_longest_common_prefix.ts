import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function longest_common_prefix(strs: string[]): string {
  if (strs.length <= 1) {
    return strs[0] || "";
  }

  const j_max = strs.reduce((acc, curr) => Math.max(acc, curr.length), 0);

  let prefix = "";
  let mismatch = false;
  let j = 0;
  while (j < j_max) {
    const ch = strs[0][j];
    for (let i = 1; i < strs.length; i += 1) {
      if (ch != strs[i][j]) {
        mismatch = true;
        break;
      }
    }

    if (mismatch) {
      break;
    }

    prefix += ch;
    j += 1;
  }

  return prefix;
}

Deno.test("0014 Longest Common Prefix", () => {
  const test_cases: [string[], string][] = [
    [[], ""],
    [[""], ""],
    [["pewpew"], "pewpew"],
    [["", ""], ""],
    [["flower", "flow", "flight"], "fl"],
    [["dog", "racecar", "car"], ""],
    [["cir", "car"], "c"],
    [["reflower", "flow", "flight"], ""],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const strs = test_case[0];
    const expected = test_case[1];

    const actual = longest_common_prefix(strs);
    assertEquals(actual, expected);
  }
});
