USE stock_analysis;

SET SQL_SAFE_UPDATES = 0;
 
DELETE FROM stock WHERE date='2023-12-01';
DELETE FROM stock WHERE date='2023-12-11' AND stock_name='顶点软件';

SET SQL_SAFE_UPDATES = 1;