import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "./shared/utils.ts";

function same_tree(p: TreeNode | null, q: TreeNode | null): boolean {
  function dfs(n1: TreeNode | null, n2: TreeNode | null): boolean {
    if (n1 === null && n2 === null) {
      return true;
    } else if (n1 === null || n2 === null || n1.val !== n2.val) {
      return false;
    } else {
      return dfs(n1.left, n2.left) && dfs(n1.right, n2.right);
    }
  }
  return dfs(p, q);
}

Deno.test("0100 Same Tree", () => {
  const test_cases: [(number | null)[], (number | null)[], boolean][] = [
    [[1, 2, 3], [1, 2, 3], true],
    [[1, 2], [1, null, 2], false],
    [[1, 2, 1], [1, 1, 2], false],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const p = array_to_tree(test_case[0]);
    const q = array_to_tree(test_case[1]);
    const expected = test_case[2];

    const actual = same_tree(p, q);
    assertEquals(actual, expected);
  }
});
