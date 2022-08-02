SET DATESTYLE TO PostgreSQL,European;

CREATE SCHEMA relational;

CREATE SEQUENCE relational.model_id;
CREATE TABLE relational.models(
	model_id INT DEFAULT nextval('relational.model_id'::regclass) PRIMARY KEY,
	generation INT,
	operating_system VARCHAR(50) NOT NULL,
	cpu VARCHAR(50) NOT NULL,
	memory VARCHAR(50) NOT NULL,
	service_category VARCHAR(50)
);

CREATE SEQUENCE relational.robot_id;
CREATE TABLE relational.robots(
	robot_id INT DEFAULT nextval('relational.robot_id'::regclass) PRIMARY KEY,
	model_id INT NOT NULL REFERENCES relational.models(model_id),
	acquisition_date DATE NOT NULL,
	register_plate VARCHAR(50) NOT NULL UNIQUE,
	daily_rate NUMERIC(10, 2) NOT NULL,
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.customer_id;
CREATE TABLE relational.customers(
	customer_id INT DEFAULT nextval('relational.customer_id'::regclass) PRIMARY KEY,
	document_number VARCHAR(50) NOT NULL UNIQUE,
	name VARCHAR(200) NOT NULL,
	date_of_birth DATE NOT NULL,
	phone_number VARCHAR(20) NOT NULL,
	address VARCHAR(200),
	date_of_registration DATE NOT NULL,
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.salesman_id;
CREATE TABLE relational.salesmen(
	salesman_id INT DEFAULT nextval('relational.salesman_id'::regclass) PRIMARY KEY,
	name VARCHAR(200) NOT NULL,
	branch VARCHAR(50),
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.order_id;
CREATE TABLE relational.orders(
	order_id INT DEFAULT nextval('relational.order_id'::regclass) PRIMARY KEY,
	robot_id INT NOT NULL REFERENCES relational.robots(robot_id),
	customer_id INT NOT NULL REFERENCES relational.customers(customer_id),
	salesman_id INT NOT NULL REFERENCES relational.salesmen(salesman_id),
	order_start_date DATE NOT NULL,
	order_end_date DATE,
	total_price NUMERIC(10, 2)
);
