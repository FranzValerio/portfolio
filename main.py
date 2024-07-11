from food_delivery import FoodDeliverySystem

def main():

    fds = FoodDeliverySystem()

    # Display the menu

    menu = fds.display_menu()

    print("Menu: ")

    for item, price in menu.items():

        print(f"{item}: $ {price}")

    print()

    # Place an order

    customer_name = "Paquita Cabeza"

    cx_2 = "Don Gato"

    cx_3 = "Peperina"

    order_items = {"Burger": 2, "Pizza": 1}

    order_2 = {"Pasta": 3, "Sushi": 1, "Beverages": 4}

    order_3 = {"Noodles": 1, "Bakery": 3, "Salad": 1, "Beverages": 2}

    result = fds.place_order(customer_name, order_items)

    result_order_2 = fds.place_order(cx_2, order_2)

    result_order_3 = fds.place_order(cx_3, order_3)

    print("\n Orders placed:")
    print(f"Order no. 1: {result}")
    print(f"Order no. 2: {result_order_2}")
    print(f"Order no. 3: {result_order_3}")

    print()

    # Pickup the order

    pickup_result = fds.pickup_order(1)
    pickup_result_2 = fds.pickup_order(2)

    print("\n Order picked up:")
    print(pickup_result)
    print(pickup_result_2)

    print()

    # Deliver the order

    delivery_result = fds.deliver_order(1)
    delivery_result_2 = fds.deliver_order(2)

    print("\n Order delivered:")
    print(delivery_result)
    print(delivery_result_2)

    print()

    # Generate bill

    bill = fds.generate_bill(1)
    bill_2 = fds.generate_bill(2)
    bill_3 = fds.generate_bill(3)

    print("\n Total bill:")
    print(bill)
    print(bill_2)
    print(bill_3)

    print()

    # Cancel an order

    cancel_result = fds.cancel_order(1)
    cancel_result_3 = fds.cancel_order(3)

    print("\n Order cancelled:")
    print(cancel_result)
    print(cancel_result_3)


if __name__ == "__main__":

    main()