export class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

export function array_to_linked_list(arr: number[]): ListNode | null {
    if (arr.length == 0) {
        return null;
    }
    const l = new ListNode(arr[0]);
    let ptr: ListNode | null = l;
    for (let i = 1; i < arr.length; i += 1) {
        ptr.next = new ListNode(arr[i]);
        ptr = ptr.next;
    }
    return l;
}


export function linked_list_to_array(l: ListNode | null): number[] {
    const arr = [];
    let ptr: ListNode | null = l;
    while (ptr != null) {
        arr.push(ptr.val);
        ptr = ptr.next;
    }
    return arr;
}

export class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

export function array_to_tree(arr: number[]): TreeNode | null {
    if (arr.length == 0) {
        return null;
    }

    const t = new TreeNode(arr[0]);
    if (arr.length === 1) {
        return t;
    }

    const q = [t];
    let i = 1;
    while (q.length > 0 && i < arr.length) {
        const n = q.shift();
        if (n == null) {
            continue;
        }

        n.left = new TreeNode(arr[i]);
        n.right = new TreeNode(arr[i + 1]);

        q.push(n.left);
        q.push(n.right);

        i += 2;
    }

    return t;
}

export function tree_to_array(tree: TreeNode | null): number[] {
    if (tree == null) {
        return [];
    }

    const arr = [];
    const q: [TreeNode | null] = [tree];
    while (q.length > 0) {
        const n = q.shift();
        if (n == null) {
            continue;
        }

        arr.push(n.val);

        q.push(n.left);
        q.push(n.right);
    }

    return arr;
}
