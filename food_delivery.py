class FoodDeliverySystem:
    """
    This is a food delivery system implemented in Python

    The user must be able to order food using this system, so it should do the following:

    - Add food order details to the orders log
    - Update the order pickup and delivery status
    - Modify order items only if the order is not picked up yet
    - Cancel the order if the order is not picked up
    - Generate a total bill, as follows:
        - if $amount > 1000 --> $total_bill = $amount + 10% tax
        - if $amount < 1000 --> $total_bill = $amount + 5% tax 
    """

    order_id = 0

    orders_log = {}

    def __init__(self):

        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350
        }

        self.bill_amount = 0

    def display_menu(self):

        return self.menu
        
    def place_order(self, customer_info, order_items):

        self.order_id += 1

        total_amount = 0

        for item, quantity in order_items.items():

            if item in self.menu:

                total_amount += self.menu[item] * quantity

            else:

                return {"status": "Order placement failed, try again please."}
            
        tax_rate = 0.10 if total_amount > 1000 else 0.05

        tax = total_amount * tax_rate

        total_bill_amount = total_amount + tax
                
        order_details = {
                "order_id": self.order_id,
                "customer_name": customer_info,
                "order_items": order_items,
                "status": "Placed",
                "total_amount": total_amount,
                "tax": tax,
                "total_bill_amount": total_bill_amount
            }
        
        self.orders_log[self.order_id] = order_details

        return order_details
    
    def pickup_order(self, order_id):

        if order_id in self.orders_log:

            self.orders_log[order_id]["status"] = "Picked Up"

            return self.orders_log[order_id]
        
        return "Order ID not found"

    def deliver_order(self, order_id):

        if order_id in self.orders_log:

            self.orders_log[order_id]["status"] = "Delivered"

            return self.orders_log[order_id]

        return "Order ID not found"

    def modify_order(self, order_id, new_items):

        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":

            total_amount = 0

            for item, quantity in new_items.items():

                if item in self.menu:

                    total_amount += self.menu[item] * quantity

                else:

                    return "Order modification failed"
                
            self.orders_log[order_id]["order_items"] = new_items
            self.orders_log[order_id]["total_amount"] = total_amount

            return self.orders_log[order_id]
        
        return "Order ID not found or already picked up"
    
    def generate_bill(self, order_id):

        if order_id in self.orders_log:

            total_amount = self.orders_log[order_id]["total_amount"]

            if total_amount > 1000:

                total_bill_amount = total_amount * 1.10

            else:

                total_bill_amount = total_amount * 1.05

            return total_bill_amount
        
        return "Order ID not found"
    
    def cancel_order(self, order_id):

        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":

            del self.orders_log[order_id]

            sorted_orders = dict(list(self.orders_log.items())[:2])

            return sorted_orders
        
        return "Order ID not found or already picked up"


