import sqlite3
import create_db

#path_to_db = r"D:\project price\db\\" + str(db_file) + ".db"


def create_table_for_category(category, path_to_db, is_stock):
	try:
		conn = sqlite3.connect(path_to_db)
	except (sqlite3.OperationalError):
		create_db.create_new_db(path_to_db)
		conn = sqlite3.connect(path_to_db)
	c = conn.cursor()
	if is_stock == True:
		create_table = "CREATE TABLE IF NOT EXISTS [" + category + "] (title, old_price, new_price, product_weight, product_url, image_urls, product_availability BOOLEAN)"
	else:
		create_table = "CREATE TABLE IF NOT EXISTS [" + category + "] (title, price, product_weight, product_url, image_urls, product_availability BOOLEAN)"
	c.execute(create_table)
	conn.commit()


def set_new_row_data(category, data_el, path_to_db, is_stock):
	conn = sqlite3.connect(path_to_db)
	c = conn.cursor()
	if is_stock == True:
		insert_data = "INSERT INTO [" + category + "] (title, old_price, new_price, product_weight, product_url, image_urls, product_availability) VALUES  (?, ?, ?, ?, ?, ?, ?)"
	else:
		insert_data = "INSERT INTO [" + category + "] (title, price, product_weight, product_url, image_urls, product_availability) VALUES  (?, ?, ?, ?, ?, ?)"
	data_tuple = (data_el[0], data_el[1], data_el[2], data_el[3], data_el[4], data_el[5])
	
	c.execute(insert_data, data_tuple)
	conn.commit()

if __name__ == '__main__':
	create_table_for_category("М'ясо, риба, птиця")
#title, beautiful_prices, product_weight, product_url, image_urls, product_availability  ({category})
