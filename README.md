# 🛡️ Enterprise Security Scoring System

**Kapsamlı endpoint güvenlik değerlendirme ve skorlama sistemi**

Bu proje, endpoint'lerden toplanan telemetri verilerini analiz ederek güvenlik skorları oluşturan, otomatik düzeltme önerileri sunan ve enterprise-level güvenlik değerlendirmesi yapan kapsamlı bir sistemdir.

## 🚀 **Proje Özellikleri**

### **📊 Kapsamlı Telemetri Şeması**
- **552 satır** JSON şema
- **20+ güvenlik kategorisi**
- **Multi-platform** desteği (Windows, macOS, Linux)
- **Enterprise-level** güvenlik kapsamı

### **🔧 35 Güvenlik Kuralı**
- **Weight sistemi** (1-15 ağırlık)
- **4 severity seviyesi** (critical, high, medium, low)
- **18 güvenlik kategorisi**
- **Otomatik düzeltme** önerileri

### **📚 Kapsamlı Dokümantasyon**
- **Rule schema** validation
- **Operator rehberi** (15 operator)
- **Kategori açıklamaları**
- **Multi-platform** örnekler

## 🏗️ **Sistem Mimarisi**

### **Ana Bileşenler**
- **📡 Collector Agent**: Endpoint'lerden telemetri verilerini toplar
- **⚙️ Rule Engine**: YAML kuralları ile veri analizi yapar
- **📊 Scoring Service**: Ağırlıklı güvenlik skorları hesaplar
- **🤖 LLM Orchestrator**: Yapay zeka destekli analiz ve öneriler
- **🛡️ Policy & Guardrails**: Güvenlik politikaları ve onay süreçleri
- **🔗 MCP Integration Layer**: Sistem entegrasyonu
- **📱 Dashboard/API**: Kullanıcı arayüzü ve raporlama

### **Akış Diyagramları**
1. **Component Flow** (`diagram/1- Scoring System Component Flow.mmd`): Sistem bileşenlerinin genel mimarisi
2. **Sequence Flow** (`diagram/2- Scoring System Sequence Flow.mmd`): Sistem akışının sıralı diyagramı

## 📁 **Proje Yapısı**

```
ScoringSystem/
├── 📊 schemas/
│   ├── telemetry_schema.json          # Kapsamlı telemetri şeması (552 satır)
│   └── rule_schema.json              # Rule validation şeması
├── 🔧 rules/
│   ├── 01_firewall_enabled.yaml      # 35 güvenlik kuralı
│   ├── 02_antivirus_updated.yaml
│   ├── ... (33 more rules)
│   └── 35_password_policy.yaml
├── 📝 examples/
│   ├── sample_telemetry_windows.json # Windows örneği
│   ├── sample_telemetry_macos.json   # macOS örneği
│   └── sample_telemetry_linux.json   # Linux örneği
├── 📚 docs/
│   ├── rule_operators.md             # Operator rehberi (15 operator)
│   └── rule_categories.md            # Kategori açıklamaları (18 kategori)
├── 🖥️ collectors/
│   └── macos_collector_fixed.sh      # macOS collector örneği
├── 📊 diagram/
│   ├── 1- Scoring System Component Flow.mmd
│   └── 2- Scoring System Sequence Flow.mmd
├── 📄 project_documents/
│   ├── Project Proposal Form (4).docx
│   └── project_note
└── 📖 README files
    ├── README.md                     # Ana README
    ├── README_enhanced_schema.md     # Şema detayları
    └── README_step1.md              # Geliştirme adımları
```

## 🎯 **Güvenlik Kategorileri**

### **🌐 Network Security**
- Firewall durumu ve kuralları
- Port kontrolü ve ağ güvenliği
- VPN ve bağlantı kontrolleri

### **🛡️ Malware Protection**
- Antivirüs durumu ve güncellemeleri
- Tehdit tespiti ve analitik
- Quarantine ve temizleme

### **🔐 Access Control**
- Multi-Factor Authentication (MFA)
- Şifre politikaları ve güvenliği
- Oturum yönetimi ve ayrıcalık kontrolü

### **🔍 Vulnerability Management**
- Kritik güvenlik açıkları
- CVE takibi ve yamalar
- Tarama sıklığı ve güncellik

### **📝 Logging & SIEM**
- Güvenlik logları ve denetim
- SIEM entegrasyonu
- Log saklama ve şifreleme

### **🚨 Incident Response**
- Olay müdahale planları
- MTTR/MTTD metrikleri
- Yanıt süreleri ve süreçler

### **🔒 Data Protection**
- Veri şifreleme (rest/transit)
- Data Loss Prevention (DLP)
- Yedekleme ve kurtarma

### **📊 Performance & Health**
- Sistem performansı (CPU, RAM, Disk)
- Sistem kararlılığı
- Hata oranları ve sağlık

## ⚖️ **Weight Sistemi**

### **Kritik Weight (12-15)**
- Kritik güvenlik açıkları (15)
- Veri şifreleme (12)
- Antivirüs güncelleme (12)

### **Yüksek Weight (8-11)**
- Firewall, MFA, DLP (8-10)
- SIEM entegrasyonu (9)
- Log yönetimi (8)

### **Orta Weight (5-7)**
- Performans metrikleri (4-6)
- Sistem kararlılığı (7)
- Eğitim ve farkındalık (5)

## 🖥️ **Multi-Platform Desteği**

### **Windows Örneği**
- **OS**: Windows 10 Pro (19045.3930)
- **Güvenlik**: Windows Defender, BitLocker, UAC
- **Ağ**: Ethernet + WiFi, RDP, SMB
- **Uygulamalar**: Chrome, Office, Windows servisleri

### **macOS Örneği**
- **OS**: macOS Sonoma (14.2.1)
- **Güvenlik**: XProtect, FileVault, Touch ID
- **Ağ**: WiFi + Bluetooth, VPN, DNS over HTTPS
- **Uygulamalar**: Safari, Office, Apple servisleri

### **Linux Örneği**
- **OS**: Ubuntu 22.04.3 LTS
- **Güvenlik**: ClamAV, LUKS, SSH
- **Ağ**: Dual Ethernet, OpenVPN, Güvenli DNS
- **Uygulamalar**: Apache, MySQL, Nginx, Redis

## 🚀 **Sonraki Adımlar**

### **Geliştirme Roadmap**
1. **Collector POC** - Telemetri toplama scriptleri
2. **Rule Engine** - Kural işleme motoru
3. **Scoring Service** - Ağırlıklı skorlama sistemi
4. **Dashboard** - Kullanıcı arayüzü
5. **API** - RESTful API servisleri

### **Teknik Gereksinimler**
- **Python 3.8+** (Rule Engine, Scoring Service)
- **Node.js 16+** (Dashboard, API)
- **Docker** (Containerization)
- **PostgreSQL** (Veri saklama)
- **Redis** (Caching)

## 📊 **Proje İstatistikleri**

- **📄 552 satır** telemetri şeması
- **🔧 35 güvenlik kuralı**
- **📚 3 platform örneği**
- **📖 18 güvenlik kategorisi**
- **⚙️ 15 operator türü**
- **⚖️ 4 severity seviyesi**

## 🤝 **Katkıda Bulunma**

Bu proje aktif geliştirme aşamasındadır. Katkıda bulunmak için:

1. **Fork** yapın
2. **Feature branch** oluşturun
3. **Commit** yapın
4. **Pull Request** gönderin

### **Geliştirme Alanları**
- Yeni güvenlik kuralları
- Platform-specific collector'lar
- Dashboard geliştirme
- API entegrasyonları
- Test coverage

## 📄 **Lisans**

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 **İletişim**

Proje hakkında sorularınız için:
- **Issues**: GitHub Issues kullanın
- **Discussions**: GitHub Discussions
- **Email**: [Proje sahibi ile iletişim]

---

**Enterprise-level güvenlik skorlama sistemi için kapsamlı ve profesyonel bir çözüm!** 🎯
