# Rule Categories - Kategori Açıklamaları

## 📋 **Güvenlik Kategorileri**

### **🌐 Network Security**
- **Açıklama**: Ağ güvenliği ve bağlantı kontrolleri
- **Örnek Kurallar**: Firewall, port kontrolü, VPN
- **Weight Aralığı**: 8-12
- **Örnekler**:
  - `01_firewall_enabled.yaml`
  - `08_open_ports.yaml`

### **🛡️ Malware Protection**
- **Açıklama**: Kötü amaçlı yazılım koruması
- **Örnek Kurallar**: Antivirüs, tehdit tespiti
- **Weight Aralığı**: 10-15
- **Örnekler**:
  - `02_antivirus_updated.yaml`
  - `32_threat_detection.yaml`

### **🔧 System Security**
- **Açıklama**: Sistem güvenliği ve yamalar
- **Örnek Kurallar**: OS yamaları, güncellemeler
- **Weight Aralığı**: 8-12
- **Örnekler**:
  - `03_os_patches.yaml`
  - `09_system_uptime.yaml`

### **🔐 Access Control**
- **Açıklama**: Erişim kontrolü ve kimlik doğrulama
- **Örnek Kurallar**: MFA, şifre politikaları, hesap güvenliği
- **Weight Aralığı**: 8-12
- **Örnekler**:
  - `04_empty_passwords.yaml`
  - `11_mfa_enabled.yaml`
  - `35_password_policy.yaml`

### **🔍 Vulnerability Management**
- **Açıklama**: Güvenlik açığı yönetimi
- **Örnek Kurallar**: CVE kontrolü, tarama yaşı
- **Weight Aralığı**: 10-15
- **Örnekler**:
  - `15_critical_vulnerabilities.yaml`
  - `16_high_vulnerabilities.yaml`
  - `17_vulnerability_scan_age.yaml`

### **📝 Logging**
- **Açıklama**: Log yönetimi ve SIEM
- **Örnek Kurallar**: Log etkinliği, SIEM entegrasyonu
- **Weight Aralığı**: 6-9
- **Örnekler**:
  - `18_security_logs_enabled.yaml`
  - `19_siem_integration.yaml`
  - `20_log_retention.yaml`

### **🚨 Incident Response**
- **Açıklama**: Olay müdahale ve yanıt
- **Örnek Kurallar**: Müdahale planı, MTTR
- **Weight Aralığı**: 6-8
- **Örnekler**:
  - `21_incident_response_plan.yaml`
  - `22_mttr_performance.yaml`

### **⚡ Performance**
- **Açıklama**: Sistem performansı
- **Örnek Kurallar**: CPU, bellek kullanımı
- **Weight Aralığı**: 4-6
- **Örnekler**:
  - `23_cpu_usage.yaml`
  - `24_memory_usage.yaml`

### **🏥 System Health**
- **Açıklama**: Sistem sağlığı ve kararlılık
- **Örnek Kurallar**: Sistem kararlılığı, hata oranları
- **Weight Aralığı**: 5-7
- **Örnekler**:
  - `25_system_stability.yaml`

### **🔒 Data Protection**
- **Açıklama**: Veri koruma ve şifreleme
- **Örnek Kurallar**: DLP, veri şifreleme
- **Weight Aralığı**: 9-12
- **Örnekler**:
  - `26_dlp_enabled.yaml`
  - `27_encryption_at_rest.yaml`

### **💾 Backup Recovery**
- **Açıklama**: Yedekleme ve kurtarma
- **Örnek Kurallar**: Yedekleme sıklığı, şifreleme
- **Weight Aralığı**: 7-9
- **Örnekler**:
  - `28_backup_frequency.yaml`
  - `29_backup_encryption.yaml`

### **📋 Security Policies**
- **Açıklama**: Güvenlik politikaları
- **Örnek Kurallar**: Politika güncelliği, uygulama
- **Weight Aralığı**: 5-8
- **Örnekler**:
  - `security_policies` (gelecekte eklenecek)

### **🎓 Security Training**
- **Açıklama**: Eğitim ve farkındalık
- **Örnek Kurallar**: Eğitim tamamlama, phishing simülasyonu
- **Weight Aralığı**: 3-5
- **Örnekler**:
  - `30_security_training.yaml`
  - `31_phishing_simulation.yaml`

### **🔍 Threat Detection**
- **Açıklama**: Tehdit tespiti ve analitik
- **Örnek Kurallar**: Davranışsal analitik, ML tespiti
- **Weight Aralığı**: 8-10
- **Örnekler**:
  - `32_threat_detection.yaml`

### **📊 Risk Assessment**
- **Açıklama**: Risk değerlendirmesi
- **Örnek Kurallar**: Risk skoru, değerlendirme yaşı
- **Weight Aralığı**: 6-8
- **Örnekler**:
  - `33_risk_score.yaml`
  - `34_risk_assessment_age.yaml`

### **💻 Application Security**
- **Açıklama**: Uygulama güvenliği
- **Örnek Kurallar**: Uygulama imzalama, güvenlik
- **Weight Aralığı**: 5-8
- **Örnekler**:
  - `application_security` (gelecekte eklenecek)

### **✅ Compliance**
- **Açıklama**: Uyumluluk ve denetim
- **Örnek Kurallar**: Denetim logları, politika uyumu
- **Weight Aralığı**: 6-9
- **Örnekler**:
  - `compliance` (gelecekte eklenecek)

### **🧠 Threat Intelligence**
- **Açıklama**: Tehdit istihbaratı
- **Örnek Kurallar**: IOC eşleşmeleri, şüpheli aktiviteler
- **Weight Aralığı**: 7-10
- **Örnekler**:
  - `threat_intelligence` (gelecekte eklenecek)

## 🎯 **Kategori Seçim Rehberi**

### **Yeni Kural Yazarken**
1. **Ana güvenlik alanını** belirle
2. **En uygun kategoriyi** seç
3. **Weight aralığını** kategorinin önemine göre ayarla
4. **Severity seviyesini** belirle

### **Kategori Öncelikleri**
- **Kritik**: Vulnerability Management, Malware Protection
- **Yüksek**: Network Security, Access Control, Data Protection
- **Orta**: Logging, Incident Response, System Health
- **Düşük**: Performance, Security Training

### **Weight Dağılımı**
- **15**: Kritik güvenlik açıkları
- **12**: Veri şifreleme, antivirüs
- **10**: Firewall, MFA, tehdit tespiti
- **8**: Log yönetimi, yedekleme
- **6**: Performans, eğitim
- **4**: Genel sistem durumu
