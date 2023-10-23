function swapPairs(head) {
    /**
     * A dummy node used as the head of a linked list.
     * @type {ListNode}
     */
    const dummy = new ListNode(0);
    dummy.next = head;
    let current = dummy;
    
    while (current.next && current.next.next) {
        const first = current.next;
        const second = current.next.next;
        first.next = second.next;
        current.next = second;
        current.next.next = first;
        current = current.next.next;
    }
    
    return dummy.next;
}
