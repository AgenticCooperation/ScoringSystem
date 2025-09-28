# Scoring System - Gelişmiş Telemetri Şeması

## 🚀 Kapsamlı Telemetri Şeması Tamamlandı!

Telemetri alanlarını çok daha detaylı ve kapsamlı hale getirdik. Artık gerçek bir enterprise güvenlik skorlama sistemi için gerekli tüm veri alanları mevcut.

## 📊 Yeni Şema Özellikleri

### 🏗️ Ana Kategoriler

1. **System** - Detaylı sistem bilgileri
2. **Security** - Kapsamlı güvenlik durumu (11 alt kategori)
3. **Network** - Ağ güvenliği ve bağlantılar
4. **Applications** - Uygulama güvenliği
5. **Compliance** - Uyumluluk ve denetim
6. **Config Hygiene** - Konfigürasyon hijyeni
7. **Threat Intelligence** - Tehdit istihbaratı

### 🔍 Detaylı Alanlar

#### System Bölümü
- **OS**: İşletim sistemi detayları (build, edition, language, timezone)
- **Hardware**: Donanım bilgileri (CPU, RAM, disk, TPM, Secure Boot)
- **Network**: Hostname, domain, uptime, timezone

#### Security Bölümü (11 Alt Kategori)
- **Firewall**: Detaylı firewall durumu ve logları
- **Antivirus**: Kapsamlı AV durumu (cloud protection, behavior monitoring)
- **Updates**: Güncelleme durumu (critical, security, optional)
- **Users**: Kullanıcı yönetimi ve şifre politikaları
- **MFA**: Multi-Factor Authentication durumu ve kapsamı
- **Session Management**: Oturum yönetimi ve güvenliği
- **Privilege Management**: Ayrıcalık yönetimi ve hesap güvenliği
- **Access Control**: Erişim kontrolü ve RBAC
- **Authentication**: Kimlik doğrulama yöntemleri
- **Account Security**: Hesap güvenliği ve koruma
- **Vulnerabilities**: Güvenlik açıkları ve CVE durumu
- **Logging**: Log yönetimi ve SIEM entegrasyonu
- **Incident Response**: Olay müdahale ve yanıt süreleri
- **Performance**: Sistem performans metrikleri
- **Health**: Sistem sağlık durumu
- **Data Protection**: Veri koruma ve DLP
- **Backup Recovery**: Yedekleme ve kurtarma
- **Security Policies**: Güvenlik politikaları
- **Security Training**: Eğitim ve farkındalık
- **Threat Detection**: Tehdit tespiti ve analitik
- **Risk Assessment**: Risk değerlendirmesi
- **Services**: Servis durumları ve şüpheli servisler
- **Processes**: Çalışan süreçler ve güvenlik analizi
- **Files**: Dosya güvenliği ve şüpheli dosyalar
- **Registry**: Registry güvenliği ve persistence mekanizmaları
- **Certificates**: Sertifika durumu ve güvenlik

#### Network Bölümü
- **Interfaces**: Ağ arayüzleri (Ethernet, WiFi, VPN)
- **Connections**: Aktif bağlantılar ve portlar
- **DNS**: DNS konfigürasyonu ve güvenlik
- **Proxy**: Proxy ayarları
- **VPN**: VPN durumu ve şifreleme

#### Applications Bölümü
- **Installed Apps**: Yüklü uygulamalar ve güvenlik
- **Running Apps**: Çalışan uygulamalar ve kaynak kullanımı
- **Browsers**: Tarayıcı güvenliği ve eklentiler

#### Compliance Bölümü
- **Audit Logs**: Denetim logları ve güvenlik olayları
- **Encryption**: Disk şifreleme durumu
- **Backup**: Yedekleme durumu ve güvenlik
- **Policies**: Güvenlik politikaları

#### Threat Intelligence Bölümü
- **Suspicious IPs**: Şüpheli IP adresleri
- **Malicious Domains**: Kötü amaçlı domainler
- **Suspicious Hashes**: Şüpheli dosya hashleri
- **Network Anomalies**: Ağ anormallikleri

## 📈 Veri Toplama Kapsamı

### Güvenlik Alanları (20+ ana kategori)
1. **Network Security** - Firewall, portlar, bağlantılar
2. **Malware Protection** - Antivirüs, tehdit tespiti
3. **System Security** - OS yamaları, güvenlik güncellemeleri
4. **Access Control** - Kullanıcı yönetimi, şifre politikaları
5. **Multi-Factor Authentication** - MFA durumu ve kapsamı
6. **Session Management** - Oturum güvenliği
7. **Privilege Management** - Ayrıcalık yönetimi
8. **Authentication Methods** - Kimlik doğrulama yöntemleri
9. **Account Security** - Hesap güvenliği
10. **Vulnerability Management** - Güvenlik açıkları
11. **Log Management** - Log yönetimi ve SIEM
12. **Incident Response** - Olay müdahale
13. **Performance Monitoring** - Sistem performansı
14. **System Health** - Sistem sağlığı
15. **Data Protection** - Veri koruma ve DLP
16. **Backup & Recovery** - Yedekleme ve kurtarma
17. **Security Policies** - Güvenlik politikaları
18. **Security Training** - Eğitim ve farkındalık
19. **Threat Detection** - Tehdit tespiti
20. **Risk Assessment** - Risk değerlendirmesi
21. **Application Security** - Uygulama güvenliği, imzalama
22. **Compliance** - Denetim, politika uyumu
23. **Threat Intelligence** - Tehdit istihbaratı, anomali tespiti

### Toplanan Veri Türleri
- **Boolean**: Açık/kapalı durumlar
- **Numeric**: Sayısal değerler (portlar, günler, sayılar)
- **String**: Metin değerler (versiyonlar, isimler)
- **Arrays**: Liste değerler (portlar, servisler, dosyalar)
- **Objects**: Karmaşık yapılar (politikalar, donanım)

## 🎯 Kural Geliştirme Potansiyeli

Bu kapsamlı şema ile artık **100+ farklı güvenlik kuralı** yazabiliriz:

### ✅ **Mevcut 35 Kural (Tamamlandı)**

#### **Temel Güvenlik Kuralları (10 kural)**
- Firewall durumu ve kuralları
- Antivirüs güncelleme ve tarama
- Kritik güvenlik yamaları
- Boş şifre kontrolü
- Misafir hesap kontrolü
- Uzak masaüstü kontrolü
- Admin hesap sayısı
- Açık portlar
- Sistem uptime
- Otomatik giriş

#### **Yeni Eklenen Kurallar (25 kural)**

**Multi-Factor Authentication (2 kural)**
- MFA etkinlik kontrolü
- MFA kapsam kontrolü

**Session & Access Management (3 kural)**
- Oturum zaman aşımı
- Ayrıcalık yükseltme
- Şifre politikası

**Vulnerability Management (3 kural)**
- Kritik güvenlik açıkları
- Yüksek risk açıklar
- Tarama yaşı

**Logging & SIEM (3 kural)**
- Güvenlik logları
- SIEM entegrasyonu
- Log saklama süresi

**Incident Response (2 kural)**
- Olay müdahale planı
- MTTR performansı

**Performance & Health (3 kural)**
- CPU kullanımı
- Bellek kullanımı
- Sistem kararlılığı

**Data Protection (4 kural)**
- DLP kontrolü
- Veri şifreleme
- Yedekleme sıklığı
- Yedekleme şifreleme

**Security Training (2 kural)**
- Güvenlik eğitimi
- Phishing simülasyonu

**Threat Detection & Risk (3 kural)**
- Tehdit tespiti
- Risk skoru
- Risk değerlendirmesi

## ⚖️ **Weight (Ağırlık) Sistemi**

### **Weight Dağılımı (1-15 arası)**

#### **Kritik Weight (12-15)**
- `weight: 15` - Kritik güvenlik açıkları
- `weight: 12` - Veri şifreleme, Antivirüs güncelleme
- `weight: 10` - Firewall, MFA, Ayrıcalık yükseltme

#### **Yüksek Weight (8-11)**
- `weight: 9` - SIEM entegrasyonu, DLP
- `weight: 8` - Log yönetimi, Yedekleme sıklığı, Risk skoru

#### **Orta Weight (5-7)**
- `weight: 7` - Sistem kararlılığı, Yedekleme şifreleme
- `weight: 6` - MFA kapsamı, Log saklama, MTTR
- `weight: 5` - Oturum zaman aşımı, CPU/Bellek kullanımı

#### **Düşük Weight (1-4)**
- `weight: 4` - Performans metrikleri
- `weight: 3` - Eğitim ve farkındalık
- `weight: 2` - Genel sistem durumu

### **Scoring Hesaplaması**

```python
# Weight bazlı scoring formülü
total_score = 0
max_possible_score = 0

for rule in rules:
    if rule.check_passes():
        total_score += rule.weight
    max_possible_score += rule.weight

security_score = (total_score / max_possible_score) * 100
```

### **Kategori Bazlı Weight Örnekleri**

| Kategori | Ortalama Weight | Örnek Kural |
|----------|----------------|-------------|
| **Vulnerability Management** | 12.5 | Kritik açıklar (15) |
| **Data Protection** | 9.5 | Veri şifreleme (12) |
| **Access Control** | 8.0 | MFA etkinlik (10) |
| **Logging & SIEM** | 7.3 | SIEM entegrasyonu (9) |
| **Performance** | 4.5 | CPU kullanımı (4) |
| **Training** | 3.5 | Güvenlik eğitimi (5) |

### 🔮 **Gelecek Kural Potansiyeli (65+ kural)**
- Servis güvenliği
- Registry güvenliği
- Ağ konfigürasyonu
- Uygulama güvenliği
- VPN kullanımı
- Güvenlik politikaları
- Donanım güvenliği
- Tarayıcı eklentileri
- Coğrafi anormallikler
- Kimlik doğrulama yöntemleri
- Erişim kontrolü
- Hesap kilitleme
- Şüpheli giriş tespiti

## 📁 Güncellenmiş Dosya Yapısı

```
ScoringSystem/
├── schemas/
│   └── telemetry_schema.json (KAPSAMLI ŞEMA)
├── rules/
│   ├── 01_firewall_enabled.yaml
│   ├── 02_antivirus_updated.yaml
│   ├── ... (35 kapsamlı kural)
│   └── (65+ yeni kural yazılabilir)
├── examples/
│   └── sample_telemetry.json (KAPSAMLI ÖRNEK)
└── README_enhanced_schema.md
```

## 🚀 Sonraki Adımlar

Bu kapsamlı şema ile artık:

1. **Collector POC** geliştirebiliriz - Bu şemaya uygun veri toplayan script
2. **35 YAML kural** tamamlandı - Tüm güvenlik alanlarını kapsayan
3. **Rule Engine** geliştirebiliriz - Karmaşık kuralları işleyen
4. **Scoring Service** oluşturabiliriz - Ağırlıklı skorlama sistemi

## ✅ Hazır Olan Bileşenler

- ✅ **Kapsamlı JSON şema** (552 satır, 7 ana kategori, 20+ alt kategori)
- ✅ **Detaylı örnek veri** (400+ satır, gerçekçi veriler)
- ✅ **35 kapsamlı kural** (10 mevcut + 25 yeni)
- ✅ **100+ kural potansiyeli** (yeni şemaya göre)
- ✅ **Enterprise seviye** güvenlik kapsamı
- ✅ **Modern güvenlik standartları** (MFA, DLP, SIEM, Risk Assessment)

## 🆕 Yeni Eklenen Alanlar

### User Access & Authentication
- **MFA**: Multi-Factor Authentication durumu
- **Session Management**: Oturum güvenliği
- **Privilege Management**: Ayrıcalık yönetimi
- **Access Control**: Erişim kontrolü
- **Authentication**: Kimlik doğrulama yöntemleri
- **Account Security**: Hesap güvenliği

### Security Operations
- **Vulnerabilities**: Güvenlik açıkları ve CVE
- **Logging**: Log yönetimi ve SIEM
- **Incident Response**: Olay müdahale
- **Threat Detection**: Tehdit tespiti
- **Risk Assessment**: Risk değerlendirmesi

### Data & System Protection
- **Data Protection**: Veri koruma ve DLP
- **Backup Recovery**: Yedekleme ve kurtarma
- **Security Policies**: Güvenlik politikaları
- **Security Training**: Eğitim ve farkındalık
- **Performance**: Sistem performansı
- **Health**: Sistem sağlığı

**Sonraki adım**: Collector POC geliştirme veya yeni kural yazma!

Bu şema artık gerçek bir enterprise güvenlik skorlama sistemi için yeterli kapsamda. Hangi yönde devam etmek istiyorsun?
