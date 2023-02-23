CREATE DATABASE Customer;

CREATE TABLE Customer(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (100),
	last_name VARCHAR (100) NOT NULL
);
CREATE TABLE Customer_Profile(
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT false,
	customer_id integer,
	FOREIGN kEY (customer_id) REFERENCES Customer(id)
);


SELECT * FROM customer
SELECT table_name,column_name,data_type FROM information_schema.columns WHERE table_name='customer_profile'
INSERT INTO Customer(first_name,last_name) 
VALUES ('Jhon','Doe'),
       ('Jerome','Lalu'),
       ('lea','Rive');


INSERT INTO Customer_Profile (isLoggedIn, customer_id) 
SELECT true, id 
FROM Customer 
WHERE first_name='John' AND last_name='Doe';
INSERT INTO Customer_Profile (isLoggedIn, customer_id) 
SELECT false,id 
FROM Customer  
WHERE first_name IN ('Jerome', 'Lea');



SELECT customer.first_name
FROM customer
INNER JOIN Customer_Profile
ON customer.id = Customer_Profile.Customer_id
WHERE customer_Profile.isLoggedIn = true;


SELECT customer.first_name, customer_Profile.isLoggedIn
FROM customer 
LEFT JOIN Customer_Profile  
ON Customer.id = Customer_Profile.customer_id;


SELECT COUNT (*) FROM Customer 
LEFT OUTER JOIN Customer_Profile 
On customer.id = Customer_Profile.customer_id 
WHERE customer_profile.isLoggedIn = false;



CREATE TABLE Book(
	book_id SERIAL PRIMARY KEY,
	title varchar(500) NOT NULL,
	author varchar(500) NOT NULL
)

INSERT INTO Book (title,author) 
VALUES ('Alice in WonderLand','Lewis Carrol'),
       ('Harry Potter', 'J.K Rowling'),
       ('to kill a mockingbird','Harper lee');


CREATE TABLE Student(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE,
	age INTEGER CHECK (age <=15)
)

INSERT INTO Student (name,age) 
VALUES ('John','12'),
       ('Lera', '10'),
       ('Bob','14');


CREATE TABLE Library(
	book_fk_id INTEGER REFERENCES Book(Book_id)ON DELETE CASCADE ON UPDATE CASCADE,
	student_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,	PRIMARY KEY (book_fk_id,student_id)
)
INSERT INTO 
Library(book_fk_id,student_id,borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE 'book.titile' = 'Alice in wonderland'),
(SELECT student_id FROM Student WHERE name='John'),'15/02/2022'),
((SELECT book_id FROM Book WHERE 'book.titile'  = 'To Kill A Mockingbird'),
(SElECT Student_id FROM Student WHERE name='Bod'),'03/03/2021'),
((SELECT book_id FROM Book WHERE 'book.titile'  = 'Alice In Wonderland'),
(SELECT student_id FROM Student WHERE name = 'Lera'),'23/05/2021'),
((SELECT book_id FROM Book WHERE 'book.titile'  = 'Harry Potter'),
(SELECT student_id FROM Student WHERE name = 'Bob'),'12/08/2021');
