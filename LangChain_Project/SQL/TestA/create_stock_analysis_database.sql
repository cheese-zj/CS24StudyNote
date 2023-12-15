CREATE DATABASE stock_analysis;

USE stock_analysis;

CREATE TABLE stock (
	stock_id varchar(16) NOT NULL,
    stock_name varchar(64) NOT NULL,
    date DATE NOT NULL,
    
    open_price DECIMAL(10,2) DEFAULT NULL,
    close_price DECIMAL(10,2) DEFAULT NULL,
    high_price DECIMAL(10,2) DEFAULT NULL,
    low_price DECIMAL(10,2) DEFAULT NULL,
    volume DECIMAL(10,2) DEFAULT NULL,
	-- For Holidays and Weekends, they might not have valid data
    -- 暂时考虑周末和假期为NULL
    PRIMARY KEY (stock_id, date)
);


