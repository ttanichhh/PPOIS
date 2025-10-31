``` Customer 6 3 -> Order, Reservation, LoyaltyProgram, Address
Employee 7 2 -> Shift, Department, Payroll
Chef 4 1 -> Order, Kitchen, Equipment
Waiter 4 1 -> Table, Order, Customer
Manager 3 1 -> Employee, Department, Report
Menu 3 3 -> MenuCategory, MenuItem
MenuCategory 3 1 -> MenuItem, Menu
MenuItem 4 1 -> Category, Recipe, Order
Order 8 3 -> Customer, OrderItem, Table, Payment
OrderItem 4 1 -> MenuItem, Order
Table 4 2 -> Reservation, Order
Restaurant 6 4 -> Employee, Table, Menu, Customer
Bill 4 1 -> Order, Payment, Tax
BillGenerator 2 2 -> Bill, TaxCalculator
ExpenseTracker 2 3 -> Expense, Budget
LoyaltyPayment 4 2 -> LoyaltyManager, PaymentProcessor, Customer
PaymentProcessor 2 2 -> Payment, Transaction
Payroll 5 1 -> Employee, Payment
PayrollSystem 1 1 -> Payroll, Employee
RevenueManager 2 4 -> Revenue, Report
TaxCalculator 1 2 -> Tax, Calculation
CookingEquipment 4 0 -> Equipment
Ingredient 4 0 -> Recipe
InventoryItem 5 2 -> Supplier, Category
Supplier 4 0 -> InventoryItem, Address
Kitchen 5 2 -> Chef, Order, Equipment
Recipe 4 2 -> Ingredient, MenuItem
Supplier 4 0 -> InventoryItem, Address
CustomerManagement 2 3 -> Customer, LoyaltyProgram
LoyaltyProgram 1 2 -> Customer
EmployeeManagement 2 3 -> Employee, Chef, Waiter, Manager
InventoryManagement 2 4 -> InventoryItem, Supplier
ReservationManagement 2 3 -> Reservation, Table
RestaurantManagement 3 4 -> Restaurant, Order, Payment
SupplierManagement 1 2 -> Supplier
DeliveryService 3 3 -> Delivery, Employee
FeedbackService 1 2 -> Customer, Order
KitchenService 2 3 -> Kitchen, Order, Chef
OrderingService 3 4 -> Order, MenuItem, Customer, Table
ReportingService 1 1 -> Restaurant
TableManagementService 1 2 -> Table
Address 3 0 -> Customer, Restaurant, Delivery
Delivery 5 3 -> Order, Employee, Address
Discount 5 2 -> Order
Payment 4 1 -> Order
Person 4 0 -> Customer, Employee
Promotion 5 2 -> Order
Reservation 5 1 -> Customer, Table
Review 4 0 -> Customer
Shift 4 1 -> Employee
LoyaltyManager 1 4 -> Customer
NotificationService 1 2 -> Customer, Employee
ReportGenerator 2 1 -> Restaurant
SecurityManager 1 2 -> User management
ValidationUtils 1 11 -> Input validation
```

### Результат
- 55 классов
- 178 полей
- 113 методов
- 12 исключений

### Исключения:
```
RestaurantException 00 →
OrderException 00 →
PaymentException 00 →
ReservationException 00 →
MenuException 00 →
EmployeeException 00 →
TableException 00 →
InventoryException 00 →
CustomerException 00 →
KitchenException 00 →
DeliveryException 00 →
DiscountException 00 →
```
