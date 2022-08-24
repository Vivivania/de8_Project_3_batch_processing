SELECT 	a.user_id,
		user_first_name,
		user_last_name,
		user_gender,
		user_address,
		user_birthday,
		user_join,
		b.order_id,
		c.voucher_id
FROM tb_users a
	LEFT JOIN tb_orders b ON a.user_id = b.user_id
	LEFT JOIN tb_vouchers c ON a.user_id = c.user_id ;
