import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

class MyQueue {

    first: number[];
    second: number[];

    constructor() {
        this.first = [];
        this.second = [];
    }

    push(x: number): void {
        this.move_to_first();
        this.first.push(x);
    }

    pop(): number {
        this.move_to_second();
        return this.second.pop()!;
    }

    peek(): number {
        this.move_to_second();
        return this.second[this.second.length - 1];
    }

    empty(): boolean {
        return this.first.length === 0 && this.second.length === 0;
    }

    private move_to_first() {
        while (this.second.length > 0) {
            this.first.push(this.second.pop()!);
        }
    }

    private move_to_second() {
        while (this.first.length > 0) {
            this.second.push(this.first.pop()!);
        }
    }
}

Deno.test("0232 Implement Queue Using Stacks", () => {
    const q = new MyQueue()

    q.push(1)
    assertEquals(q.first, [1])
    assertEquals(q.second, [])

    q.push(2)
    assertEquals(q.first, [1, 2])
    assertEquals(q.second, [])

    assertEquals(q.peek(), 1)
    assertEquals(q.first, [])
    assertEquals(q.second, [2, 1])

    assertEquals(q.pop(), 1)
    assertEquals(q.first, [])
    assertEquals(q.second, [2])

    assertEquals(q.empty(), false)
    assertEquals(q.first, [])
    assertEquals(q.second, [2])
});
