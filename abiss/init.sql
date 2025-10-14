-- ABISS Database Initialization Script
-- Bu dosya PostgreSQL container'ı ilk başlatıldığında çalışır

-- Veritabanını oluştur (zaten docker-compose.yml'de oluşturuluyor)
-- CREATE DATABASE abiss_db;

-- Veritabanına bağlan
\c abiss_db;

-- Gerekli extension'ları yükle
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Kullanıcı izinlerini ayarla
GRANT ALL PRIVILEGES ON DATABASE abiss_db TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA public TO postgres;

-- Başlangıç mesajı
DO $$
BEGIN
    RAISE NOTICE 'ABISS database initialized successfully!';
END $$;
