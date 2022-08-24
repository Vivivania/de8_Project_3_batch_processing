SELECT 	order_item_id,
		a.order_id,
		a.product_id,
		b.product_name,
		order_item_quantity,
		b.product_discount,
		product_subdiscount,
		b.product_price,
		product_subprice,
		c.order_price,
		c.order_discount,
		c.order_total
FROM tb_order_items a
	LEFT JOIN tb_products b ON a.product_id = b.product_id
	LEFT JOIN tb_orders c ON a.order_id = c.order_id ;


