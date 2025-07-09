CREATE DATABASE IF NOT EXISTS email_sorter_db;
USE email_sorter_db;

-- Users Table (stores authenticated users)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    google_id VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    access_token TEXT NOT NULL,
    refresh_token TEXT NOT NULL,
    token_expiry DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Emails Table (stores processed emails)
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    gmail_message_id VARCHAR(255) NOT NULL,
    thread_id VARCHAR(255),
    sender VARCHAR(255) NOT NULL,
    recipient VARCHAR(255) NOT NULL,
    subject VARCHAR(255),
    snippet TEXT,
    body LONGTEXT,
    received_date DATETIME NOT NULL,
    is_read BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE (user_id, gmail_message_id)
);

-- Categories Table (email classification)
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Email-Category Mapping (many-to-many relationship)
CREATE TABLE email_categories (
    email_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (email_id, category_id),
    FOREIGN KEY (email_id) REFERENCES emails(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Initial Categories
INSERT INTO categories (name, description) VALUES
('Primary', 'Important emails'),
('Social', 'Social media notifications'),
('Promotions', 'Marketing and promotional emails'),
('Updates', 'System and application updates'),
('Spam', 'Junk emails');