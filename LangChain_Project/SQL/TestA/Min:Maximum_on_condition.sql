USE stock_analysis;


SELECT MIN(low_price) AS '12.1-12.13 最低值'
FROM stock
WHERE date BETWEEN '2023-12-01' AND '2023-12-13' 
		AND
	stock_name='恒生电子'
	