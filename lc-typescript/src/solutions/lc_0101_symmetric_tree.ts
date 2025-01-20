import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "../shared/utils.ts";

function is_symmetric(root: TreeNode | null): boolean {
  function traverse(n1: TreeNode | null, n2: TreeNode | null): boolean {
    if (n1 == null && n2 == null) {
      return true;
    } else if (n1 == null || n2 == null || n1.val !== n2.val) {
      return false;
    } else {
      return traverse(n1.left, n2.right) && traverse(n1.right, n2.left);
    }
  }

  if (root == null) {
    return true;
  }

  return traverse(root.left, root.right);
}

Deno.test("0101 Symmetric Tree", () => {
  const test_cases: [(number | null)[], boolean][] = [
    [[1], true],
    [[1, 2, 2, 3, 4, 4, 3], true],
    [[1, 2, 2, null, 3, null, 3], false],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const root = array_to_tree(test_case[0]);
    const expected = test_case[1];

    const actual = is_symmetric(root);
    assertEquals(actual, expected);
  }
});
