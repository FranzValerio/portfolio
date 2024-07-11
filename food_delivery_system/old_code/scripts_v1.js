document.getElementById('order-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    
    fetch('/place_order', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-result').innerText = `Order placed successfully. Order details: ${JSON.stringify(data, null, 2)}`;
        // Clear the form
        event.target.reset();
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('order-result').innerText = 'Error placing order.';
    });
});
function getTotalBill(orderId) {
    fetch(`/generate_bill/${orderId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-result').innerText = `Total bill for order ${orderId}: ${data}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('order-result').innerText = 'Error getting total bill.';
    });
}

function checkDeliveryStatus(orderId) {
    fetch(`/order_status/${orderId}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-result').innerText = `Order ${orderId} status: ${data.status}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('order-result').innerText = 'Error checking delivery status.';
    });
}

// Function to cancel an order
function cancelOrder(orderId) {
    fetch(`/cancel_order/${orderId}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('order-result').innerText = `Order ${orderId} canceled. Remaining orders: ${JSON.stringify(data, null, 2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('order-result').innerText = 'Error canceling order.';
    });
}