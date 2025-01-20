import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode } from "../shared/utils.ts";

function sorted_array_to_bst(nums: number[]): TreeNode | null {
  function traverse(low: number, high: number): TreeNode | null {
    if (low > high) {
      return null;
    }
    const mid = low + Math.floor((high - low) / 2);
    return new TreeNode(nums[mid], traverse(low, mid - 1), traverse(mid + 1, high));
  }

  return traverse(0, nums.length - 1);
}

function convert(node: TreeNode | null): (number | null)[] {
  if (node == null) {
    return [];
  }

  const xs: (number | null)[] = [node.val];
  const q = [node.left, node.right];
  while (q.length > 0) {
    const n = q.shift();
    if (n == null) {
      xs.push(null);
      continue;
    }
    xs.push(n.val);
    q.push(n.left);
    q.push(n.right);
  }

  return xs;
}

Deno.test("0108 Convert Sorted Array to Binary Search Tree", () => {
  const test_cases: [number[], (number | null)[]][] = [
    [
      [-10, -3, 0, 5, 9],
      [0, -10, 5, null, -3, null, 9, null, null, null, null]
    ],
    [
      [1, 3],
      [1, null, 3, null, null]
    ],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const nums = test_case[0];
    const expected = test_case[1];

    const actual = convert(sorted_array_to_bst(nums));

    assertEquals(actual, expected);
  }
});
