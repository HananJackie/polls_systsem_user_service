DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL,
    address VARCHAR(255),
    joining_date DATE NOT NULL,
    is_registered BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO users (first_name, last_name, email, age, address, joining_date, is_registered) VALUES
('Avichai', 'Buzaglo', 'Avichai.Buzaglo@mail.com', 40, '20 Saharov David, Rishon Lezion, Israel', '2024-12-01', TRUE),
('Ann', 'Kerry', 'Ann.Kerry@mail.com', 30, '32 Larissa Court St, Cabarita, Victoria, Australia', '2023-01-01', TRUE),
('Amit', 'Pratesh', 'Amit.Patesh@mail.com', 20, '7, Atlanta, Evershine Nagar, Malad (west), Mumbai, Maharashtra, India', '2022-05-20', FALSE);
