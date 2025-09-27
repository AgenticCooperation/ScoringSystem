# Scoring System - Adım 1: Gereksinimler & Şema

## 📋 Tamamlanan İşler

### 1. JSON Telemetri Şeması
- **Dosya**: `schemas/telemetry_schema.json`
- **İçerik**: Endpoint'lerden toplanacak tüm telemetri alanlarının JSON şeması
- **Kapsam**: Sistem bilgileri, güvenlik durumu, konfigürasyon hijyeni

### 2. 10 Örnek YAML Kural Dosyası
- **Klasör**: `rules/`
- **Kurallar**:
  1. `01_firewall_enabled.yaml` - Firewall etkinlik kontrolü
  2. `02_antivirus_updated.yaml` - Antivirüs güncelleme kontrolü
  3. `03_os_patches.yaml` - OS yama kontrolü
  4. `04_empty_passwords.yaml` - Boş şifre kontrolü
  5. `05_guest_account.yaml` - Misafir hesap kontrolü
  6. `06_remote_desktop.yaml` - Uzak masaüstü güvenlik kontrolü
  7. `07_admin_accounts.yaml` - Yönetici hesap sayısı kontrolü
  8. `08_open_ports.yaml` - Açık port kontrolü
  9. `09_system_uptime.yaml` - Sistem çalışma süresi kontrolü
  10. `10_auto_login.yaml` - Otomatik giriş kontrolü

### 3. Örnek Telemetri Verisi
- **Dosya**: `examples/sample_telemetry.json`
- **İçerik**: Gerçekçi bir endpoint telemetri verisi örneği

## 🏗️ Kural Yapısı

Her YAML kural dosyası şu yapıya sahip:

```yaml
rule:
  id: "unique_rule_id"
  name: "Kural Adı"
  description: "Kural açıklaması"
  category: "kategori"
  severity: "low|medium|high|critical"
  weight: sayısal_değer

check:
  field: "json.field.path"
  operator: "equals|less_than|greater_than|contains|not_contains"
  expected_value: beklenen_değer

message:
  pass: "Başarılı mesaj"
  fail: "Başarısız mesaj"

remediation:
  action: "eylem_adı"
  script: "script_yolu"
  description: "Düzeltme açıklaması"
```

## 📊 Kategori Dağılımı

- **Network Security**: 2 kural (firewall, ports)
- **Access Control**: 4 kural (passwords, guest, admin, auto-login)
- **Malware Protection**: 1 kural (antivirus)
- **System Security**: 1 kural (OS patches)
- **Remote Access**: 1 kural (remote desktop)
- **System Health**: 1 kural (uptime)

## 🎯 Sonraki Adım

**Adım 2: Collector (POC)** için hazırız!
- Tek OS ile başlayabiliriz (Windows PowerShell önerilir)
- Bu şemaya uygun veri toplayan küçük bir script yazabiliriz
- JSON formatında çıktı üretebiliriz

## 📁 Dosya Yapısı

```
ScoringSystem/
├── schemas/
│   └── telemetry_schema.json
├── rules/
│   ├── 01_firewall_enabled.yaml
│   ├── 02_antivirus_updated.yaml
│   ├── 03_os_patches.yaml
│   ├── 04_empty_passwords.yaml
│   ├── 05_guest_account.yaml
│   ├── 06_remote_desktop.yaml
│   ├── 07_admin_accounts.yaml
│   ├── 08_open_ports.yaml
│   ├── 09_system_uptime.yaml
│   └── 10_auto_login.yaml
├── examples/
│   └── sample_telemetry.json
└── README_step1.md
```

## ✅ Hazır Olan Bileşenler

- ✅ JSON şema tanımı
- ✅ 10 çalışır durumda YAML kural
- ✅ Örnek telemetri verisi
- ✅ Kural yapısı standardı
- ✅ Kategori ve severity tanımları
- ✅ Remediation script referansları

**Sonraki adım**: Collector POC geliştirme!
