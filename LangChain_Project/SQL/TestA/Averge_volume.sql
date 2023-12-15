USE stock_analysis;


SELECT AVG(volume)
FROM stock
WHERE 
NOT volume is NULL 
AND
stock_name='恒生电子'