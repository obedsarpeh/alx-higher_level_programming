-- Convert the database to UTF8MB4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table to UTF8MB4
ALTER TABLE hbtn_0c_0.first_table CONVERT TO utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field to UTF8MB4
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
