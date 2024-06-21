

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INT NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE borrowings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_name VARCHAR(255) NOT NULL,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

CREATE TABLE user_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    request TEXT NOT NULL,
    request_date DATE
);

INSERT INTO books (title, author, publication_year, available) VALUES
('Chí Phèo', 'Nam Cao', 1941, FALSE),
('Tắt Đèn', 'Ngô Tất Tố', 1939, TRUE),
('Số Đỏ', 'Vũ Trọng Phụng', 1936, FALSE),
('Vợ Nhặt', 'Kim Lân', 1962, TRUE),
('Lão Hạc', 'Nam Cao', 1943, TRUE),
('Những Ngày Thơ Ấu', 'Nguyên Hồng', 1938, TRUE),
('Giông Tố', 'Vũ Trọng Phụng', 1936, TRUE),
('Đôi Lứa Xứng Đôi', 'Nam Cao', 1941, TRUE),
('Bỉ Vỏ', 'Nguyên Hồng', 1937, TRUE),
('Người Thầy Đầu Tiên', 'Chinghiz Aitmatov', 1962, TRUE);

INSERT INTO borrowings (book_id, user_name, borrow_date, return_date) VALUES
(1, 'Nguyen Van A', '2024-06-01', NULL),
(3, 'Le Thi B', '2024-06-02', NULL);
