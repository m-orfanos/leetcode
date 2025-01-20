import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

import { TreeNode, array_to_tree, tree_to_array } from "../shared/utils.ts";

function invert_tree0(root: TreeNode | null): TreeNode | null {
    const stack = [root];
    while (stack.length > 0) {
        const n = stack.pop();
        if (n == null) {
            continue;
        }

        // swap
        const t = n.left;
        n.left = n.right;
        n.right = t;

        // traverse
        stack.push(n.left);
        stack.push(n.right);
    }

    return root;
};

function invert_tree1(root: TreeNode | null): TreeNode | null {
    function dfs(node: TreeNode | null) {
        if (node == null) {
            return;
        }

        // swap
        const t = node.left;
        node.left = node.right;
        node.right = t;

        // traverse
        dfs(node.left);
        dfs(node.right);
    }

    dfs(root);

    return root;
}

Deno.test("0226 Invert Binary Tree", async (t) => {
    const test_cases = [
        [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
        [[2, 1, 3], [2, 3, 1]],
        [[], []],
    ];

    await t.step(`Iterative DFS`, () => {
        for (let i = 0; i < test_cases.length; i += 1) {
            const test_case = test_cases[i];

            const tree1 = array_to_tree(test_case[0]);
            const tree3 = invert_tree0(tree1);

            const actual = tree_to_array(tree3);
            const expected = test_case[1];

            assertEquals(actual, expected);
        }
    });

    await t.step(`Recursive DFS`, () => {
        for (let i = 0; i < test_cases.length; i += 1) {
            const test_case = test_cases[i];

            const tree1 = array_to_tree(test_case[0]);
            const tree3 = invert_tree1(tree1);

            const actual = tree_to_array(tree3);
            const expected = test_case[1];

            assertEquals(actual, expected);
        }
    });

});
