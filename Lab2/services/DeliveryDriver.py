from entities.Order import Order


class DeliveryDriver:
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.vehicle = ""
        self.delivery_area = ""

    def calculate_delivery_time(self, distance):
        base_time = 15  # minutes
        traffic_factor = 1.2 if distance > 5 else 1.0
        weather_factor = 1.1  # slight delay for safety

        if self.vehicle.lower() == "motorcycle":
            speed_factor = 0.8
        elif self.vehicle.lower() == "car":
            speed_factor = 1.0
        else:
            speed_factor = 1.2

        estimated_time = base_time + (distance * 3 * traffic_factor * weather_factor * speed_factor)
        return f"Estimated delivery time: {estimated_time:.0f} minutes for {distance}km"

    def update_delivery_status(self, order):
        status_stages = [
            "Order received at restaurant",
            "Food being prepared",
            "Driver dispatched",
            "On the way to customer",
            "Arrived at destination",
            "Delivered successfully"
        ]

        current_stage = status_stages[2]  # Assuming driver is dispatched
        status_update = f"Delivery Update - Order {order.order_id}\n"
        status_update += f"Driver: {self.name}\n"
        status_update += f"Vehicle: {self.vehicle}\n"
        status_update += f"Status: {current_stage}\n"
        status_update += f"Area: {self.delivery_area}"
        return status_update