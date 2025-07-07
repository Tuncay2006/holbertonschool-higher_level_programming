-- 1-create_user.sql

-- Kullanıcıyı oluştur, varsa hata verme
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Tüm veritabanları ve tablolar üzerinde tüm ayrıcalıkları ver
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Ayrıcalık değişikliklerini uygula
FLUSH PRIVILEGES;
