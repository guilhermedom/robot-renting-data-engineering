SET DATESTYLE TO PostgreSQL,European;

CREATE SCHEMA relational;

CREATE SEQUENCE relational.model_id;
CREATE TABLE relational.models(
	model_id INT DEFAULT nextval('relational.model_id'::regclass) PRIMARY KEY,
	model_brand VARCHAR(200) NOT NULL,
	model_name VARCHAR(200) NOT NULL,
	operating_system VARCHAR(50) NOT NULL,
	cpu VARCHAR(50) NOT NULL,
	memory VARCHAR(50) NOT NULL,
	generation SMALLINT NOT NULL,
	service_category VARCHAR(50) NOT NULL,
	UNIQUE(model_brand, model_name, cpu, memory, generation)
);

CREATE SEQUENCE relational.robot_id;
CREATE TABLE relational.robots(
	robot_id BIGINT DEFAULT nextval('relational.robot_id'::regclass) PRIMARY KEY,
	model_id INT NOT NULL REFERENCES relational.models(model_id),
	register_plate VARCHAR(50) NOT NULL UNIQUE,
	acquisition_date DATE NOT NULL,
	daily_rate NUMERIC(8, 2) NOT NULL,
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.customer_id;
CREATE TABLE relational.customers(
	customer_id BIGINT DEFAULT nextval('relational.customer_id'::regclass) PRIMARY KEY,
	email VARCHAR(200) NOT NULL UNIQUE,
	name VARCHAR(200) NOT NULL,
	date_of_birth DATE NOT NULL,
	sex VARCHAR(12) NOT NULL,
	phone_number VARCHAR(20) NOT NULL,
	state_province VARCHAR(200) NOT NULL,
	city VARCHAR(200) NOT NULL,
	address VARCHAR(200) NOT NULL,
	date_of_registration DATE NOT NULL,
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.salesperson_id;
CREATE TABLE relational.salespersons(
	salesperson_id INT DEFAULT nextval('relational.salesperson_id'::regclass) PRIMARY KEY,
	email VARCHAR(200) NOT NULL UNIQUE,
	name VARCHAR(200) NOT NULL,
	branch VARCHAR(50) NOT NULL,
	status VARCHAR(50) NOT NULL
);

CREATE SEQUENCE relational.order_id;
CREATE TABLE relational.orders(
	order_id BIGINT DEFAULT nextval('relational.order_id'::regclass) PRIMARY KEY,
	robot_id BIGINT NOT NULL REFERENCES relational.robots(robot_id),
	customer_id BIGINT NOT NULL REFERENCES relational.customers(customer_id),
	salesperson_id INT NOT NULL REFERENCES relational.salespersons(salesperson_id),
	order_start_date DATE NOT NULL,
	order_end_date DATE,
	total_price NUMERIC(12, 2),
	discount_percentage NUMERIC(3, 2),
	discount NUMERIC(12, 2),
	discounted_total_price NUMERIC(12, 2)
);
