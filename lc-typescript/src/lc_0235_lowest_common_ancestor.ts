import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "./shared/utils.ts";

function lowest_common_ancestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (p == null || q == null) {
        return null;
    }
    const [low, high] = p.val < q.val ? [p.val, q.val] : [q.val, p.val];

    function dfs(node: TreeNode | null): TreeNode | null {
        if (node == null || p == null || q == null) {
            return null;
        }

        const curr = node.val;

        if (curr < low && curr < high) {
            return dfs(node.right);
        } else if (curr > low && curr > high) {
            return dfs(node.left);
        } else {
            return node;
        }
    }

    return dfs(root);
};

Deno.test("0235 Lowest Common Ancestor", () => {
    const test_cases: [(number | null)[], number, number, number][] = [
        [[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], 2, 8, 6],
        [[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], 2, 4, 2],
        [[2, 1], 2, 1, 2],
        [[2, 1, 3], 3, 1, 2],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const root = array_to_tree(test_case[0]);

        const p = new TreeNode(test_case[1]);
        const q = new TreeNode(test_case[2]);

        const actual = lowest_common_ancestor(root, p, q);
        const expected = test_case[3];

        assertEquals(actual?.val, expected);
    }
});
