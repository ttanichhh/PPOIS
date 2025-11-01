class RestaurantException(Exception):
    """Базовое исключение для всех исключений ресторана"""
    pass

class OrderException(RestaurantException):
    """Исключение для ошибок заказов"""
    pass

class PaymentException(RestaurantException):
    """Исключение для ошибок оплаты"""
    pass

class ReservationException(RestaurantException):
    """Исключение для ошибок бронирования"""
    pass

class MenuException(RestaurantException):
    """Исключение для ошибок меню"""
    pass

class EmployeeException(RestaurantException):
    """Исключение для ошибок сотрудников"""
    pass

class TableException(RestaurantException):
    """Исключение для ошибок столов"""
    pass

class InventoryException(RestaurantException):
    """Исключение для ошибок инвентаря"""
    pass

class CustomerException(RestaurantException):
    """Исключение для ошибок клиентов"""
    pass

class KitchenException(RestaurantException):
    """Исключение для ошибок кухни"""
    pass

class DeliveryException(RestaurantException):
    """Исключение для ошибок доставки"""
    pass

class DiscountException(RestaurantException):
    """Исключение для ошибок скидок"""
    pass

# ДОБАВЬТЕ ЭТИ НЕДОСТАЮЩИЕ ИСКЛЮЧЕНИЯ:

class LoyaltyException(RestaurantException):
    """Исключение для ошибок лояльности"""
    pass

class FeedbackException(RestaurantException):
    """Исключение для ошибок отзывов"""
    pass

class SecurityBreachException(RestaurantException):
    """Исключение для ошибок безопасности"""
    pass

class IntegrationException(RestaurantException):
    """Исключение для ошибок интеграции"""
    pass

# НЕЗАВИСИМЫЕ ИСКЛЮЧЕНИЯ (наследуются напрямую от Exception):

class ValidationException(Exception):
    """Исключение для ошибок валидации"""
    pass

class AuthorizationException(Exception):
    """Исключение для ошибок авторизации"""
    pass

class DatabaseException(Exception):
    """Исключение для ошибок базы данных"""
    pass