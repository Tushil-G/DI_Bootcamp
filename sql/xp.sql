CREATE DATABASE Customer;
CREATE TABLE customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR (100),
    last_name VARCHAR (100)

);

CREATE TABLE items(
    item_id SERIAL PRIMARY KEY,
    price INTEGER,
    item VARCHAR (50)
);

INSERT INTO customer(first_name,last_name)
VALUES('Greg',' Jones'),
      ('Sandra','Jones'),
      ('Scott','Scott'),
      ('Trevor','Green'),
      ('Melanie','Johnson')


INSERT INTO items(item, item_price) 
VALUES('small Desk',100),
      ('large Desk',300),
      ('fan',80)

SELECT * FROM items
SELECT *FROM items where item_Price>80
SELECT * FROM customers where last_name ='Smith'--It might output null
SELECT * FROM customers where last_name ='Jones'
SELECT * FROM customers where last_name <>'Jone'

