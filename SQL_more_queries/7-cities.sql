-- 1. Veritabanını oluştur (varsa hata verme)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Veritabanını seç
USE hbtn_0d_usa;

-- 3. cities tablosunu oluştur (varsa hata verme)
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
