-- Create Categories Table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Subcategories Table
CREATE TABLE subcategories (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Products Table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    subcategory_id INT REFERENCES subcategories(id) ON DELETE SET NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    minimum_stock_level INT DEFAULT 10
);

-- Create Stock Entries Table
CREATE TABLE stock_entries (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    supplier_name VARCHAR(255) NOT NULL,
    batch_number VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Sales Table
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity_sold INT NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    batch_number VARCHAR(255)
);

-- Create Audit Logs Table
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    action VARCHAR(255) NOT NULL,
    product_id INT REFERENCES products(id) ON DELETE SET NULL,
    old_value TEXT,
    new_value TEXT,
    performed_by VARCHAR(255),
    date_performed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

