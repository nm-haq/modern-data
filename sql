-- 1. Remove exact duplicates
DELETE FROM RetailSales
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM RetailSales
    GROUP BY TransactionID, Date, CustomerID, Product, Quantity, PricePerUnit, PaymentMethod, StoreLocation, TotalAmount
);

-- 2. Handle missing CustomerID (set to "Unknown")
UPDATE RetailSales
SET CustomerID = 'Unknown'
WHERE CustomerID IS NULL OR TRIM(CustomerID) = '';

-- 3. Handle missing Product (set to "Unspecified")
UPDATE RetailSales
SET Product = 'Unspecified'
WHERE Product IS NULL OR TRIM(Product) = '';

-- 4. Fix PaymentMethod inconsistencies
UPDATE RetailSales SET PaymentMethod = 'Cash' 
WHERE LOWER(PaymentMethod) = 'cash';

UPDATE RetailSales SET PaymentMethod = 'E-Wallet'
WHERE LOWER(PaymentMethod) IN ('ewallet','e-wallet');

UPDATE RetailSales SET PaymentMethod = 'Credit Card'
WHERE LOWER(PaymentMethod) = 'credit card';

UPDATE RetailSales SET PaymentMethod = 'Unknown'
WHERE PaymentMethod IS NULL OR TRIM(PaymentMethod) = '';

-- 5. Convert Quantity and PricePerUnit into numeric values
-- (If DB allows type change, else cast them during queries)
-- Example for SQLite/MySQL: create a new cleaned table
CREATE TABLE CleanedRetail AS
SELECT 
    TransactionID,
    Date,
    CustomerID,
    Product,
    CASE 
        WHEN Quantity GLOB '*[^0-9]*' THEN NULL
        ELSE CAST(Quantity AS FLOAT)
    END AS Quantity,
    CASE 
        WHEN PricePerUnit GLOB '*[^0-9.]*' THEN NULL
        ELSE CAST(PricePerUnit AS FLOAT)
    END AS PricePerUnit,
    PaymentMethod,
    StoreLocation,
    TotalAmount
FROM RetailSales;

-- 6. Replace negative or unrealistic values
UPDATE CleanedRetail
SET Quantity = NULL
WHERE Quantity < 0;

UPDATE CleanedRetail
SET PricePerUnit = NULL
WHERE PricePerUnit > 1000;

-- 7. Fix mismatched TotalAmount
UPDATE CleanedRetail
SET TotalAmount = Quantity * PricePerUnit
WHERE TotalAmount <> Quantity * PricePerUnit;
