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
