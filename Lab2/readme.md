Customer 5 2 ->  
Employee 5 2 ->  
MenuItem 5 2 ->  
Order 5 3 -> Customer, MenuItem  
Reservation 5 2 -> Customer  
Table 4 3 ->  
Payment 5 2 -> Order  
Review 5 2 -> Customer, Order  
Invoice 5 2 -> Order  
LoyaltyMember 4 2 -> Customer  

RestaurantManager 4 3 -> Employee  
KitchenManager 4 2 -> Chef  
InventoryManager 4 2 -> StockItem  
HRManager 4 2 -> Employee  
FinanceManager 4 2 -> ExpenseTracker  
OrderManager 3 2 -> Order  
MenuManager 3 2 -> MenuItem  
ReservationManager 3 2 -> Reservation  
QualityManager -> 4 2   

Chef 4 2 -> Recipe  
SousChef 3 2 -> Chef  
LineCook 4 2 -> Dish  
PastryChef 3 2 -> Recipe   
Dish 4 2 -> Ingredient   
Recipe 4 2 -> Ingredient  
Ingredient 4 1 -> StockItem  
KitchenStation 4 2 -> LineCook  
FoodPreparation 3 2 -> Dish  

Waiter 4 2 -> Order, Customer  
Bartender 3 2 -> Order  
Host 3 2 -> Reservation   
DeliveryService 4 2 -> Order  
CustomerService 3 2 -> Customer  
CleaningStaff 3 2 ->   
Cashier 3 2 Payment ->  
Sommelier 3 2 ->  
Barista 3 2 ->  

StockItem 5 2 ->  
Supplier 4 2 ->  
InventoryTracker 3 2 -> StockItem  
StorageUnit 4 2 -> StockItem  
WasteTracker 3 2 ->  
OrderProcessor 2 2 -> Supplier  

ExpenseTracker 3 2 ->  
ProfitAnalyzer 3 2 ->  
TaxCalculator 2 2 ->  
PayrollManager 2 2 -> Employee  
BudgetPlanner 2 2 ->  

DateUtils 1 2 ->  
ValidationUtils 1 2 ->  
ReportGenerator 1 2 ->  

Exceptions(12):  
CustomerException 0 0 ->  
DeliveryException 0 0 ->  
EmployeeException 0 0 ->  
FinanceException 0 0 ->  
InventoryException 0 0 ->  
KitchenException 0 0 ->  
MenuException 0 0 ->  
OrderException 0 0 ->  
PaymentException 0 0 ->  
ReservationException 0 0 ->  
RestaurantException 0 0 ->  
ServiceException 0 0 ->  

Классы: 51  
Поля: 179  
Методы: 104  
Ассоциации: 36  
Исключения: 12  
