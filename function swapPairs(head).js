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

// Load Stripe.js asynchronously
var stripe = Stripe('YOUR_PUBLISHABLE_KEY');

// Create a checkout session
fetch('/create-checkout-session', {
    method: 'POST',
})
.then(function(response) {
    return response.json();
})
.then(function(session) {
    return stripe.redirectToCheckout({ sessionId: session.id });
})
.then(function(result) {
    // If `redirectToCheckout` fails due to a browser or network
    // error, you should display the localized error message to your
    // customer using `result.error.message`.
})
.catch(function(error) {
    console.error('Error:', error);
});

