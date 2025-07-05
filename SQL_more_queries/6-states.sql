-- 1. Veritabanını oluştur (varsa hata verme)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Oluşturulan veritabanını kullan
USE hbtn_0d_usa;

-- 3. Tabloyu oluştur (varsa hata verme)
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
