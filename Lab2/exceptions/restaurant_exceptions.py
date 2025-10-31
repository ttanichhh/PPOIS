class RestaurantException(Exception):
    """Базовое исключение для ресторана"""
    pass

class OrderException(RestaurantException):
    """Исключение для заказов"""
    pass

class PaymentException(RestaurantException):
    """Исключение для платежей"""
    pass

class ReservationException(RestaurantException):
    """Исключение для бронирований"""
    pass

class MenuException(RestaurantException):
    """Исключение для меню"""
    pass

class EmployeeException(RestaurantException):
    """Исключение для сотрудников"""
    pass

class TableException(RestaurantException):
    """Исключение для столов"""
    pass

class InventoryException(RestaurantException):
    """Исключение для инвентаря"""
    pass

class CustomerException(RestaurantException):
    """Исключение для клиентов"""
    pass

class KitchenException(RestaurantException):
    """Исключение для кухни"""
    pass

class DeliveryException(RestaurantException):
    """Исключение для доставки"""
    pass

class DiscountException(RestaurantException):
    """Исключение для скидок"""
    pass

class ValidationException(Exception):
    """Исключение для валидации"""
    pass

class AuthorizationException(Exception):
    """Исключение для авторизации"""
    pass

class DatabaseException(Exception):
    """Исключение для базы данных"""
    pass