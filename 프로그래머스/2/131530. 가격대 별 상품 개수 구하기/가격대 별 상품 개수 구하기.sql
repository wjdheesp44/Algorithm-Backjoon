SELECT FLOOR((PRICE / 10000)) * 10000 PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT 
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP