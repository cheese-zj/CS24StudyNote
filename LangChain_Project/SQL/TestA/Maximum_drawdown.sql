USE stock_analysis;

SELECT MAX(drawdown_data) AS 'Maximum_drawdown'
FROM  (
	SELECT 
    stock_id,
    date,
    low_price,
    (
		SELECT MAX(low_price) 
        FROM stock AS s2
        WHERE s2.stock_id = s1.stock_id AND s2.date < s1.date
    )AS peak_low_price,
    (
		(
		SELECT MAX(low_price) 
        FROM stock AS s3
        WHERE s3.stock_id = s1.stock_id AND s3.date < s1.date
		)
        - low_price
    ) / (
		SELECT MAX(low_price) 
        FROM stock AS s4
        WHERE s4.stock_id = s1.stock_id AND s4.date < s1.date
	) AS drawdown_data
    -- why does this drawdown_data is necessary?
	FROM stock AS s1
    WHERE stock_id='600570' 
    AND 
    -- 选定时间区间
    s1.date >= '2023-12-08'
    
) AS drawdown_data