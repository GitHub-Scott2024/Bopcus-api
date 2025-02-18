-- Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role ENUM('admin', 'user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);

-- BOPCUS Categories table
CREATE TABLE bopcus_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT NOT NULL,
    required_documents TEXT
);

-- Search history table
CREATE TABLE search_history (
    search_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    search_term VARCHAR(255) NOT NULL,
    search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Logs table
CREATE TABLE logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    action TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Copyright table
CREATE TABLE copyright_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    creator_name VARCHAR(255) NOT NULL DEFAULT 'Karin E Scott',
    message TEXT NOT NULL DEFAULT 'This searchable database is created by Karin E Scott.',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert the creator's copyright entry
INSERT INTO copyright_log (creator_name, message) 
VALUES ('Karin E Scott', 'This searchable database is created by Karin E Scott.');
