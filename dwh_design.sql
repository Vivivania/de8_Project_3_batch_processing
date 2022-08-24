DROP TABLE dim_orders
DROP TABLE dim_users
DROP TABLE fact_orders

CREATE TABLE dim_orders (
	order_id INT NOT NULL,
	order_date DATE NOT NULL,
	user_id INT NOT NULL,
	payment_name VARCHAR(255),
	shipper_name VARCHAR(255),
	order_price INT,
	order_discount INT,
	voucher_name VARCHAR(255),
	voucher_price INT,
	order_total INT,
	rating_status VARCHAR(255)
	);

CREATE TABLE dim_users (
	user_id INT NOT NULL,
	user_first_name VARCHAR(255) NOT NULL,
	user_last_name VARCHAR(255) NOT NULL,
	user_gender VARCHAR(50) NOT NULL,
	user_address VARCHAR(255),
	user_birthday DATE NOT NULL,
	user_join DATE NOT NULL,
	order_id INT NOT NULL,
	voucher_id INT NOT NULL
	);

CREATE TABLE fact_orders (
	order_item_id INT NOT NULL,
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	product_name VARCHAR(255) NOT NULL,
	order_item_quantity INT,
	product_discount INT,
	product_subdiscount INT,
	product_price INT NOT NULL,
	product_subprice INT NOT NULL,
    order_price INT NOT NULL,
	order_discount INT,
	order_total INT NOT NULL
	);