CREATE TABLE Customer (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  phone_number VARCHAR(20) NOT NULL UNIQUE,
  address VARCHAR(255)
);

CREATE TABLE Enquiry (
  id INT PRIMARY KEY AUTO_INCREMENT,
  enquiry_description VARCHAR(255) NOT NULL,
  booking_date DATE NOT NULL,
  vehicle_category ENUM('small', 'family', 'van') NOT NULL,
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

CREATE TABLE Vehicle (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category ENUM('small', 'family', 'van') NOT NULL,
  model VARCHAR(255) NOT NULL,
  daily_rate DECIMAL(10, 2) NOT NULL,
  year YEAR NOT NULL
);

CREATE TABLE Booking (
  id INT PRIMARY KEY AUTO_INCREMENT,
  return_date DATE NOT NULL,
  hire_date DATE NOT NULL,
  vehicle_id INT,
  customer_id INT,
  FOREIGN KEY (vehicle_id) REFERENCES Vehicle(id),
  FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

DELIMITER //
CREATE TRIGGER check_booking_dates
BEFORE INSERT ON Booking
FOR EACH ROW
BEGIN
    IF NEW.hire_date >= NEW.return_date THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Hire date must be before return date';
    END IF;
    IF DATEDIFF(NEW.return_date, NEW.hire_date) > 7 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Hire duration cannot exceed 7 days';
    END IF;
END //
DELIMITER ;

CREATE TABLE Payment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  amount DECIMAL(10, 2) NOT NULL,
  payment_date DATE NOT NULL
);

ALTER TABLE Booking 
ADD CONSTRAINT fk_Bookings_Payments 
FOREIGN KEY (payment_id) 
REFERENCES Payment(id) 
ON DELETE RESTRICT
ON UPDATE CASCADE;