document.addEventListener('DOMContentLoaded', function () {
    calculateTotal();
});

function placeOrder(event) {
    event.preventDefault();

    const customerName = document.getElementById('customer_name').value;
    const customerAddress = document.getElementById('customer_address').value;
    const customerEmail = document.getElementById('customer_email').value;
    const customerPhone = document.getElementById('customer_phone').value;
    const orderItems = {};

    document.querySelectorAll('.menu-item input').forEach(input => {
        if (parseInt(input.value) > 0) {
            orderItems[input.name] = input.value;
        }
    });

    if (Object.keys(orderItems).length === 0) {
        alert("Please select at least one item to place an order.");
        return;
    }

    fetch('/place_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            customer_name: customerName,
            customer_address: customerAddress,
            customer_email: customerEmail,
            customer_phone: customerPhone,
            ...orderItems
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === "Order placement failed") {
            alert(data.status);
        } else {
            alert("Order placed successfully!");
            displayTotal(data);
            displayOrderSummary(data);
        }
    })
    .catch(error => console.error('Error:', error));
}

function calculateTotal() {
    let total = 0;

    document.querySelectorAll('.menu-item input').forEach(input => {
        const price = parseInt(input.closest('.menu-item').querySelector('label').textContent.match(/\((\d+)\)/)[1]);
        const quantity = parseInt(input.value);
        total += price * quantity;
    });

    document.getElementById('total').textContent = total.toFixed(2);
    const taxRate = total > 1000 ? 0.10 : 0.05;
    const tax = total * taxRate;
    document.getElementById('tax').textContent = tax.toFixed(2);
    document.getElementById('total_bill').textContent = (total + tax).toFixed(2);
}

function displayTotal(order) {
    document.getElementById('total').textContent = order.total_amount.toFixed(2);
    document.getElementById('tax').textContent = order.tax.toFixed(2);
    document.getElementById('total_bill').textContent = order.total_bill_amount.toFixed(2);
}

function displayOrderSummary(order) {
    const orderSummary = document.getElementById('order-summary');
    orderSummary.innerHTML = `
        <h3>Order Summary</h3>
        <p><strong>Order ID:</strong> ${order.order_id}</p>
        <p><strong>Name:</strong> ${order.customer_info.name}</p>
        <p><strong>Address:</strong> ${order.customer_info.address}</p>
        <p><strong>Email:</strong> ${order.customer_info.email}</p>
        <p><strong>Phone:</strong> ${order.customer_info.phone}</p>
        <ul>
            ${Object.entries(order.order_items).map(([item, quantity]) => `<li>${item}: ${quantity}</li>`).join('')}
        </ul>
        <p><strong>Total Amount:</strong> $${order.total_amount.toFixed(2)}</p>
        <p><strong>Tax:</strong> $${order.tax.toFixed(2)}</p>
        <p><strong>Total Bill:</strong> $${order.total_bill_amount.toFixed(2)}</p>
    `;
}

function checkDeliveryStatus() {
    const orderId = document.getElementById('order_id').value;

    fetch(`/order_status/${orderId}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(`Order Status: ${data.status}`);
        }
    })
    .catch(error => console.error('Error:', error));
}

function cancelOrder() {
    const orderId = document.getElementById('order_id').value;

    fetch(`/cancel_order/${orderId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(`Order cancelled successfully!`);
        }
    })
    .catch(error => console.error('Error:', error));
}
