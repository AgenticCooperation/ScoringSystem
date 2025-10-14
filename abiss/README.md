# ABISS - Advanced Backend Intelligence Scoring System

ABISS, endpoint güvenlik durumunu değerlendiren ve skorlayan modern bir FastAPI uygulamasıdır.

## Özellikler

- **Endpoint Yönetimi**: Hostname, platform ve risk seviyesi ile endpoint'leri yönetin
- **Telemetry Toplama**: JSONB formatında esnek telemetry verisi toplama
- **Policy Değerlendirme**: Otomatik güvenlik kuralları ile endpoint'leri değerlendirme
- **Skorlama Sistemi**: 0-100 arası risk skorları ve detaylı breakdown
- **Finding Yönetimi**: Güvenlik bulgularını kategorize etme ve takip etme
- **Remediation**: Otomatik düzeltme işlemleri ve audit log

## Teknolojiler

- **FastAPI**: Modern, hızlı web framework
- **SQLAlchemy 2.x**: Modern ORM
- **PostgreSQL**: Güçlü ilişkisel veritabanı
- **Pydantic v2**: Veri validasyonu
- **Alembic**: Veritabanı migration'ları

## Kurulum

### 🐳 Docker ile Hızlı Başlangıç (Önerilen)

```bash
# Projeyi klonlayın
git clone <repository-url>
cd abiss

# Docker Compose ile başlatın
docker-compose up -d

# Logları takip edin
docker-compose logs -f abiss
```

Bu komutlar:
- PostgreSQL 15 veritabanını başlatır
- ABISS FastAPI uygulamasını başlatır
- Alembic migration'larını otomatik çalıştırır

**Erişim Adresleri:**
- ABISS API: http://localhost:8000
- API Dokümantasyonu: http://localhost:8000/docs

**DBeaver Bağlantı Bilgileri:**
- Host: localhost
- Port: 5432
- Database: abiss_db
- Username: postgres
- Password: password

### 🔧 Manuel Kurulum

#### 1. Gereksinimler

- Python 3.8+
- PostgreSQL 12+
- pip

#### 2. Projeyi Klonlayın

```bash
git clone <repository-url>
cd abiss
```

#### 3. Virtual Environment Oluşturun

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

#### 4. Bağımlılıkları Yükleyin

```bash
pip install -e .
```

#### 5. Environment Dosyasını Ayarlayın

```bash
cp env.example .env
```

`.env` dosyasını düzenleyerek veritabanı bağlantı bilgilerinizi güncelleyin:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/abiss_db
```

#### 6. PostgreSQL Veritabanını Oluşturun

```sql
CREATE DATABASE abiss_db;
```

#### 7. Alembic Migration'larını Çalıştırın

```bash
alembic upgrade head
```

#### 8. Uygulamayı Başlatın

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Uygulama `http://localhost:8000` adresinde çalışacaktır.

## API Dokümantasyonu

Uygulama çalıştıktan sonra aşağıdaki adreslerde API dokümantasyonuna erişebilirsiniz:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Endpoints
- `POST /endpoints` - Yeni endpoint oluştur
- `GET /endpoints/{id}` - Endpoint detayını getir
- `GET /endpoints` - Endpoint'leri listele

### Telemetry
- `POST /telemetry` - Telemetry verisi gönder (otomatik scoring tetikler)

### Findings
- `GET /findings` - Finding'leri filtrele ve getir
- `GET /findings/{id}` - Finding detayını getir

### Scores
- `GET /scores/{endpoint_id}` - Endpoint skorlarını getir
- `GET /scores/{endpoint_id}/latest` - En son skoru getir

### Remediations
- `POST /remediations/execute` - Remediation çalıştır (idempotent)
- `GET /remediations/{id}` - Remediation detayını getir
- `GET /remediations` - Remediation'ları listele

## Örnek Kullanım

### Endpoint Oluşturma

```bash
curl -X POST "http://localhost:8000/endpoints" \
  -H "Content-Type: application/json" \
  -d '{
    "hostname": "server-01",
    "platform": "windows",
    "owner_label": "IT Department",
    "tags": ["production", "web-server"]
  }'
```

### Telemetry Gönderme

```bash
curl -X POST "http://localhost:8000/telemetry" \
  -H "Content-Type: application/json" \
  -d '{
    "endpoint_id": 1,
    "payload": {
      "system": {
        "platform": "windows",
        "updates": [
          {"id": "KB123456", "severity": "critical", "installed": false}
        ],
        "memory": {"usage_percent": 85},
        "disks": [
          {"mount_point": "C:", "usage_percent": 95}
        ]
      },
      "security": {
        "firewall": {"enabled": false},
        "antivirus": {"enabled": true}
      }
    },
    "schema_version": "1.0"
  }'
```

## Docker Komutları

### Temel Docker Komutları

```bash
# Servisleri başlat
docker-compose up -d

# Servisleri durdur
docker-compose down

# Logları görüntüle
docker-compose logs -f abiss

# Sadece veritabanını başlat
docker-compose up -d postgres

# Servisleri yeniden başlat
docker-compose restart abiss

# Veritabanını sıfırla
docker-compose down -v
docker-compose up -d
```

### Geliştirme

```bash
# Development modunda çalıştır
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# Test çalıştır
docker-compose exec abiss pytest

# Migration oluştur
docker-compose exec abiss alembic revision --autogenerate -m "Description"

# Migration uygula
docker-compose exec abiss alembic upgrade head
```

### Test Çalıştırma

```bash
# Docker ile
docker-compose exec abiss pytest

# Manuel
pytest
```

### Kod Formatlama

```bash
# Docker ile
docker-compose exec abiss black app/
docker-compose exec abiss isort app/

# Manuel
black app/
isort app/
```

### Migration Oluşturma

```bash
# Docker ile
docker-compose exec abiss alembic revision --autogenerate -m "Description of changes"
docker-compose exec abiss alembic upgrade head

# Manuel
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Lisans

MIT License
