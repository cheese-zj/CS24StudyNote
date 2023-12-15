USE stock_analysis;


SELECT 
	s1.date,
	s1.stock_name,
    s1.open_price AS '恒生电子开盘价',
    s1.close_price AS '恒生电子收盘价',
    s1.close_price AS '恒生电子交易量',
	s2.stock_name,
    s2.open_price AS '顶点证券开盘价',
    s2.close_price AS '顶点证券收盘价',
    s2.close_price AS '顶点证券交易量'
FROM stock AS s1
JOIN stock AS s2
	ON s1.date=s2.date AND s1.stock_name='恒生电子' AND s2.stock_name='顶点软件'
    AND
    s1.date >= '2023-12-02'
    