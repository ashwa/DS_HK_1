-- What customers are from the UK
SELECT CustomerName FROM Customers WHERE city = 'UK'

-- What is the name of the customer who has the most orders?
SELECT MAX(Quantity) FROM OrderDetails
JOIN Orders on (OrderDetails.OrderID = Orders.OrderID)
JOIN Customers on (Orders.CustomerID = Customers.CustomersID)
SELECT CustomerName FROM Customers

-- What supplier has the highest average product price?
SELECT 

-- What category has the most orders?
SELECT 

-- What employee made the most sales (by number of sales)?
SELECT 

-- What employee made the most sales (by value of sales)?
SELECT 

-- What employees have BS degrees? (Hint: Look at LIKE operator)What supplier has the highest average product price assuming they have at least 2 
SELECT 

-- products (Hint: Look at the HAVING operator)
SELECT 

