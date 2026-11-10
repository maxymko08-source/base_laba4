-- =============================================================
-- data.sql — Test data dump + Stored Procedure + Trigger
-- Run against schema created by Lab #3 DDL
-- =============================================================

USE mydb;

-- ----------------------------
-- Car Brands
-- ----------------------------
INSERT INTO car_brands (brand_name) VALUES
('Toyota'), ('BMW'), ('Mercedes'), ('Audi'), ('Honda'),
('Ford'), ('Volkswagen'), ('Hyundai'), ('Kia'), ('Lexus');

-- ----------------------------
-- Car Categories
-- ----------------------------
INSERT INTO car_categories (category_name, daily_price) VALUES
('Economy', 30), ('Compact', 45), ('Midsize', 60),
('SUV', 80), ('Luxury', 120), ('Minivan', 70),
('Electric', 90), ('Sports', 150), ('Truck', 65), ('Premium', 200);

-- ----------------------------
-- Car Models
-- ----------------------------
INSERT INTO car_models (model_name, car_brands_id) VALUES
('Corolla', 1), ('Camry', 1), ('RAV4', 1),
('3 Series', 2), ('5 Series', 2),
('C-Class', 3), ('E-Class', 3),
('A4', 4), ('Q5', 4),
('Civic', 5);

-- ----------------------------
-- Locations
-- ----------------------------
INSERT INTO locations (city, street_address) VALUES
('Kyiv', 'Khreshchatyk 1'), ('Lviv', 'Rynok Square 5'),
('Odesa', 'Derybasivska 10'), ('Kharkiv', 'Sumska 20'),
('Dnipro', 'Nauky Ave 15'), ('Kyiv', 'Peremohy Ave 3'),
('Kyiv', 'Borispolska 7'), ('Lviv', 'Lychakivska 12'),
('Odesa', 'Pushkinska 4'), ('Zaporizhzhia', 'Metalurhiv 8');

-- ----------------------------
-- Cars
-- ----------------------------
INSERT INTO cars (license_plate, year, car_models_id, car_categories_id, locations_id) VALUES
('AA1234BB', 2020, 1, 1, 1), ('BB5678CC', 2021, 2, 3, 2),
('CC9012DD', 2022, 3, 4, 3), ('DD3456EE', 2019, 4, 5, 4),
('EE7890FF', 2023, 5, 6, 5), ('FF1234GG', 2021, 6, 2, 6),
('GG5678HH', 2022, 7, 7, 7), ('HH9012II', 2020, 8, 8, 8),
('II3456JJ', 2023, 9, 4, 9), ('JJ7890KK', 2018, 10, 1, 10);

-- ----------------------------
-- Fine Types
-- ----------------------------
INSERT INTO fine_types (name, standard_amount) VALUES
('Speeding', 150.00), ('Parking violation', 80.00),
('Traffic light violation', 200.00), ('No seatbelt', 50.00),
('Phone use while driving', 100.00), ('Car damage', NULL),
('Fuel shortage', 30.00), ('Late return', 50.00),
('Smoking in car', 70.00), ('Unauthorized driver', 300.00);

-- ----------------------------
-- Users
-- ----------------------------
INSERT INTO users (first_name, last_name, email, phone, driver_license) VALUES
('Oleksii', 'Kovalenko', 'o.kovalenko@mail.ua', '+380501234567', 'DL-UA-001'),
('Maria', 'Bondarenko', 'm.bondarenko@mail.ua', '+380672345678', 'DL-UA-002'),
('Ivan', 'Shevchenko', 'i.shevchenko@mail.ua', '+380933456789', 'DL-UA-003'),
('Olena', 'Petrenko', 'o.petrenko@mail.ua', '+380504567890', 'DL-UA-004'),
('Dmytro', 'Lysenko', 'd.lysenko@mail.ua', '+380675678901', 'DL-UA-005'),
('Yulia', 'Kravchenko', 'y.kravchenko@mail.ua', '+380936789012', 'DL-UA-006'),
('Andriy', 'Moroz', 'a.moroz@mail.ua', '+380507890123', 'DL-UA-007'),
('Svitlana', 'Tkachenko', 's.tkachenko@mail.ua', '+380678901234', 'DL-UA-008'),
('Mykola', 'Savchenko', 'm.savchenko@mail.ua', '+380939012345', 'DL-UA-009'),
('Iryna', 'Hrytsenko', 'i.hrytsenko@mail.ua', '+380500123456', 'DL-UA-010');

-- ----------------------------
-- Rental Statuses
-- ----------------------------
INSERT INTO rental_statuses (status_name) VALUES
('Active'), ('Completed'), ('Cancelled'),
('Pending'), ('Overdue'), ('Reserved'),
('In Progress'), ('Closed'), ('Disputed'), ('Refunded');

-- ----------------------------
-- Rentals
-- ----------------------------
INSERT INTO rentals
  (start_date, end_date, users_id, cars_id, rental_statuses_id, pickup_location_id, dropoff_location_id)
VALUES
('2024-01-10', '2024-01-15', 1, 1, 2, 1, 2),
('2024-02-05', '2024-02-10', 2, 2, 2, 2, 3),
('2024-03-01', '2024-03-07', 3, 3, 1, 3, 4),
('2024-04-12', '2024-04-18', 4, 4, 2, 4, 5),
('2024-05-20', '2024-05-25', 5, 5, 2, 5, 6),
('2024-06-01', '2024-06-05', 6, 6, 1, 6, 7),
('2024-07-10', '2024-07-15', 7, 7, 2, 7, 8),
('2024-08-03', '2024-08-08', 8, 8, 3, 8, 9),
('2024-09-14', '2024-09-20', 9, 9, 2, 9, 10),
('2024-10-01', '2024-10-05', 10, 10, 1, 10, 1);

-- ----------------------------
-- Fines
-- ----------------------------
INSERT INTO fines (issue_date, actual_amount, rentals_id, fine_types_id) VALUES
('2024-01-15 12:00:00', 150.00, 1, 1),
('2024-02-10 09:30:00', 80.00, 2, 2),
('2024-04-18 15:00:00', 300.00, 4, 10),
('2024-07-15 11:00:00', 50.00, 7, 8),
('2024-09-20 10:00:00', 70.00, 9, 9);

-- ----------------------------
-- Payments
-- ----------------------------
INSERT INTO payments (amount, payment_date, rentals_id) VALUES
(150.00, '2024-01-10 10:00:00', 1),
(225.00, '2024-02-05 11:00:00', 2),
(360.00, '2024-03-01 09:00:00', 3),
(480.00, '2024-04-12 14:00:00', 4),
(400.00, '2024-05-20 16:00:00', 5),
(180.00, '2024-06-01 12:00:00', 6),
(400.00, '2024-07-10 10:00:00', 7),
(1200.00, '2024-08-03 15:00:00', 8),
(720.00, '2024-09-14 11:00:00', 9),
(120.00, '2024-10-01 09:00:00', 10);

-- ----------------------------
-- Services
-- ----------------------------
INSERT INTO services (services_name, price) VALUES
('GPS Navigation', 10.00), ('Child Seat', 8.00),
('Additional Driver', 15.00), ('Full Insurance', 25.00),
('Roadside Assistance', 12.00), ('Wi-Fi Hotspot', 7.00),
('Airport Pickup', 20.00), ('Car Wash', 5.00),
('Fuel Top-up', 50.00), ('Ski Rack', 10.00);

-- ----------------------------
-- Rental Services (M:M)
-- ----------------------------
INSERT INTO rental_services (rentals_id, services_id, quantity, fixed_price) VALUES
(1, 1, 1, 10.00), (1, 4, 1, 25.00),
(2, 2, 1, 8.00), (2, 3, 1, 15.00),
(3, 1, 1, 10.00), (3, 5, 1, 12.00),
(4, 4, 1, 25.00), (4, 7, 1, 20.00),
(5, 6, 1, 7.00), (6, 8, 1, 5.00);

-- ----------------------------
-- User Passports
-- ----------------------------
INSERT INTO user_passports (passport_number, users_id) VALUES
('AA123456', 1), ('BB234567', 2), ('CC345678', 3),
('DD456789', 4), ('EE567890', 5), ('FF678901', 6),
('GG789012', 7), ('HH890123', 8), ('II901234', 9),
('JJ012345', 10);


-- =============================================================
-- STORED PROCEDURE: get_rental_summary
-- Call via: CALL get_rental_summary(1);
-- API endpoint: GET /api/rentals/{id}/summary
-- =============================================================
DROP PROCEDURE IF EXISTS get_rental_summary;

DELIMITER $$
CREATE PROCEDURE get_rental_summary(IN p_rental_id INT)
BEGIN
    SELECT
        r.id                                          AS rental_id,
        CONCAT(u.first_name, ' ', u.last_name)       AS client_name,
        CONCAT(cb.brand_name, ' ', cm.model_name)    AS car,
        c.license_plate,
        r.start_date,
        r.end_date,
        DATEDIFF(r.end_date, r.start_date)           AS rental_days,
        cc.daily_price * DATEDIFF(r.end_date, r.start_date) AS total_cost,
        rs.status_name                                AS status
    FROM rentals r
    JOIN users u              ON r.users_id = u.id
    JOIN cars c               ON r.cars_id = c.id
    JOIN car_models cm        ON c.car_models_id = cm.id
    JOIN car_brands cb        ON cm.car_brands_id = cb.id
    JOIN car_categories cc    ON c.car_categories_id = cc.id
    JOIN rental_statuses rs   ON r.rental_statuses_id = rs.id
    WHERE r.id = p_rental_id;
END$$
DELIMITER ;


-- =============================================================
-- TRIGGER: trg_fine_default_amount
-- Automatically sets actual_amount from fine_types.standard_amount
-- when actual_amount is 0 or not set meaningfully on INSERT.
-- This trigger fires on INSERT INTO fines.
-- =============================================================
DROP TRIGGER IF EXISTS trg_fine_default_amount;

DELIMITER $$
CREATE TRIGGER trg_fine_default_amount
BEFORE INSERT ON fines
FOR EACH ROW
BEGIN
    IF NEW.actual_amount = 0 THEN
        SELECT standard_amount INTO @std
        FROM fine_types
        WHERE id = NEW.fine_types_id;

        IF @std IS NOT NULL THEN
            SET NEW.actual_amount = @std;
        END IF;
    END IF;
END$$
DELIMITER ;
