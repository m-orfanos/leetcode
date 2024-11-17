import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { ListNode } from "./shared/utils.ts";

function has_cycle1(head: ListNode | null): boolean {
    let slow = head;
    let fast = head;
    while (slow != null && fast != null) {
        slow = slow.next;
        fast = fast?.next?.next || null;
        if (slow != null && fast != null && slow == fast) {
            return true;
        }
    }
    return false;
}

function has_cycle2(head: ListNode | null): boolean {
    let slow = head;
    let fast = head != null ? head.next : null;

    if (!head) {
        return false;
    }

    while (slow != null && fast != null && slow != fast) {
        slow = slow.next;
        fast = fast.next != null ? fast.next.next : null;
    }

    return slow == fast;
}

Deno.test("0141 Linked List Cycle", () => {
    // test case 1
    const head_a = new ListNode(3);
    const tail_a = new ListNode(2, new ListNode(0, new ListNode(-4, head_a)));
    head_a.next = tail_a;

    // test case 2
    const head_b = new ListNode(1);
    const tail_b = new ListNode(2, head_a);
    head_b.next = tail_b;

    // merge test cases
    const test_cases: [ListNode, boolean][] = [
        [head_a, true],
        [head_b, true],
        [new ListNode(1), false],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const head = test_case[0];
        const expected = test_case[1];
        
        const actual1 = has_cycle1(head);
        assertEquals(actual1, expected);

        const actual2 = has_cycle2(head);
        assertEquals(actual2, expected);
    }
});
