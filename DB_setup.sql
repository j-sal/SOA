CREATE TABLE plans(
	planId SERIAL PRIMARY KEY,
	planName TEXT,
	planDescription TEXT,
	price REAL
);

CREATE TABLE customers(
	customerId SERIAL PRIMARY KEY,
	planId INT REFERENCES plans(planId),
	passportNumber CHAR(100),
	name TEXT,
	email TEXT,
	address TEXT,
	paid BOOLEAN
);

INSERT INTO plans (planName, planDescription, price) VALUES ('Basic Plan', 'The basic insurance plan offered. Limited coverage but at good value.', 49.95);
INSERT INTO plans (planName, planDescription, price) VALUES ('Premium Plan', 'The premium insurance plan offered. Comprehensive coverage but at a more substantial cost.', 99.95);

INSERT INTO customers (planId, passportNumber, name, email, address, paid) VALUES (1, 'AF726495', 'Jimmy George', 'jdawg@hotmail.com', '1264 Toronto Lane', FALSE);
INSERT INTO customers (planId, passportNumber, name, email, address, paid) VALUES (2, 'CX717852', 'Thomas Detlor', 'tdetz@gmail.com', '825 Vancouver Drive', FALSE);