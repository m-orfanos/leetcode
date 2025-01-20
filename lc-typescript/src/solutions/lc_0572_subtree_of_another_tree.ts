import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "../shared/utils.ts";

function is_subtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  function is_equals(node1: TreeNode | null, node2: TreeNode | null): boolean {
    if (node1 == null && node2 == null) {
      return true;
    } else if (node1 == null || node2 == null || node1.val !== node2.val) {
      return false;
    } else {
      return is_equals(node1.left, node2.left) && is_equals(node1.right, node2.right);
    }
  }

  function traverse(node: TreeNode | null): boolean {
    if (node == null) {
      return false;
    } else if (is_equals(node, subRoot)) {
      return true;
    } else {
      return traverse(node.left) || traverse(node.right);
    }
  }

  return traverse(root);
}

Deno.test("0572 Subtree of Another Tree", () => {
  const test_cases: [(number | null)[], (number | null)[], boolean][] = [
    [
      [3, 4, 5, 1, 2],
      [4, 1, 2],
      true
    ],
    [
      [3, 4, 5, 1, 2, null, null, null, null, 0],
      [4, 1, 2],
      false
    ],
    [
      [4, -9, 5, null, -1, null, 8, -6, 0, 7, null, null, -2, null, null, null, null, -3,],
      [5],
      false,
    ],
    [
      [1, 1],
      [1],
      true,
    ]
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const root = array_to_tree(test_case[0]);
    const subroot = array_to_tree(test_case[1]);
    const expected = test_case[2];

    const actual = is_subtree(root, subroot);
    assertEquals(actual, expected, `iteration # ${i}`);
  }
});
