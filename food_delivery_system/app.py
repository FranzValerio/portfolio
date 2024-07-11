from flask import Flask, render_template, request, jsonify
from food_delivery_system.food_delivery import FoodDeliverySystem

app = Flask(__name__)

fds = FoodDeliverySystem()

@app.route('/')
def index():
    return render_template('index.html', menu=fds.display_menu())

@app.route('/place_order', methods=['POST'])
def place_order():
    customer_info = {
        "name": request.json['customer_name'],
        "address": request.json['customer_address'],
        "email": request.json['customer_email'],
        "phone": request.json['customer_phone']
    }

    order_items = request.json
    del order_items['customer_name']
    del order_items['customer_address']
    del order_items['customer_email']
    del order_items['customer_phone']

    for item in order_items:
        order_items[item] = int(order_items[item])

    result = fds.place_order(customer_info, order_items)
    return jsonify(result)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(fds.orders_log)

@app.route('/generate_bill/<int:order_id>', methods=['GET'])
def generate_bill(order_id):
    total_bill = fds.generate_bill(order_id)
    return jsonify(total_bill)

@app.route('/order_status/<int:order_id>', methods=['GET'])
def order_status(order_id):
    order = fds.orders_log.get(order_id, None)
    if order:
        return jsonify({"status": order["status"]})
    return jsonify({"error": "Order ID not found"}), 404

@app.route('/cancel_order/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    result = fds.cancel_order(order_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
