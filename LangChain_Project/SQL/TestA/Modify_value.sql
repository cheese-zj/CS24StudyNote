USE stock_analysis;

SET SQL_SAFE_UPDATES = 0;
 
UPDATE stock

SET volume = 0
WHERE date="2023-12-13" AND stock_name='恒生电子';

SET SQL_SAFE_UPDATES = 1;