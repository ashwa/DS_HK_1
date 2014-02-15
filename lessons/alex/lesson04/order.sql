-- What customers are from the UK
SELECT CustomerName FROM Customers WHERE city = 'UK'

-- What is the name of the customer who has the most orders?
SELECT Customers.CustomerName FROM Customers
INNER JOIN Orders on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Customers.CustomerID
ORDER BY COUNT(Customers.CustomerID) DESC
LIMIT 1

-- What supplier has the highest average product price?
SELECT Suppliers.SupplierName FROM Products
INNER JOIN Suppliers ON (Products.SupplierID = Suppliers.SupplierID)
GROUP BY Products.SupplierID
ORDER BY AVG(Products.Price) DESC
Limit 1

-- What category has the most orders?
SELECT Categories.CategoryName FROM OrderDetails
INNER JOIN Products ON (Products.ProductID = OrderDetails.ProductID)
INNER JOIN Categories ON (Categories.CategoryID = Products.CategoryID)
GROUP BY OrderDetails.ProductID
ORDER BY COUNT(OrderDetails.ProductID) DESC
LIMIT 5

-- What employee made the most sales (by number of sales)?
SELECT Employees.FirstName, Employees.LastName FROM Orders
INNER JOIN Employees ON (Orders.EmployeeID = Employees.EmployeeID)
GROUP BY Orders.EmployeeID
ORDER BY COUNT(Orders.EmployeeID) DESC
LIMIT 1

-- What employee made the most sales (by value of sales)?
SELECT Employees.FirstName, Employees.LastName, SUM(Products.Price * OrderDetails.Quantity) AS ValueOfSales FROM OrderDetails
INNER JOIN Orders ON (OrderDetails.OrderID = Orders.OrderID)
INNER JOIN Employees ON (Orders.EmployeeID = Employees.EmployeeID)
INNER JOIN Products ON (OrderDetails.ProductID = Products.ProductID)
GROUP BY Employees.EmployeeID
ORDER BY ValueOfSales DESC
LIMIT 1

-- What employees have BS degrees? (Hint: Look at LIKE operator)
SELECT FirstName, LastName FROM Employees WHERE Notes LIKE '%BS%'

-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT Suppliers.SupplierName FROM Products
INNER JOIN Suppliers ON (Products.SupplierID = Suppliers.SupplierID)
GROUP BY Products.SupplierID
HAVING COUNT(Products.SupplierID) > 1
ORDER BY AVG(Products.Price) DESC
LIMIT 1

