# Rule Operators - Detaylı Açıklamalar

## 📋 **Operator Türleri ve Kullanımları**

### **🔍 Temel Karşılaştırma Operatörleri**

#### **`equals`**
- **Açıklama**: Değer tam olarak eşit mi?
- **Kullanım**: Boolean, string, number değerler için
- **Örnek**: `security.firewall.enabled` == `true`
```yaml
check:
  field: "security.firewall.enabled"
  operator: "equals"
  expected_value: true
```

#### **`not_equals`**
- **Açıklama**: Değer eşit değil mi?
- **Kullanım**: Boolean, string, number değerler için
- **Örnek**: `security.firewall.enabled` != `false`
```yaml
check:
  field: "security.firewall.enabled"
  operator: "not_equals"
  expected_value: false
```

### **📊 Sayısal Karşılaştırma Operatörleri**

#### **`greater_than`**
- **Açıklama**: Değer beklenenden büyük mü?
- **Kullanım**: Number değerler için
- **Örnek**: `security.vulnerabilities.critical_vulns` > `0`
```yaml
check:
  field: "security.vulnerabilities.critical_vulns"
  operator: "greater_than"
  expected_value: 0
```

#### **`less_than`**
- **Açıklama**: Değer beklenenden küçük mü?
- **Kullanım**: Number değerler için
- **Örnek**: `security.performance.cpu_usage_percent` < `80`
```yaml
check:
  field: "security.performance.cpu_usage_percent"
  operator: "less_than"
  expected_value: 80
```

#### **`greater_than_or_equal`**
- **Açıklama**: Değer büyük eşit mi?
- **Kullanım**: Number değerler için
- **Örnek**: `security.mfa.coverage_percent` >= `80`
```yaml
check:
  field: "security.mfa.coverage_percent"
  operator: "greater_than_or_equal"
  expected_value: 80
```

#### **`less_than_or_equal`**
- **Açıklama**: Değer küçük eşit mi?
- **Kullanım**: Number değerler için
- **Örnek**: `security.performance.memory_usage_percent` <= `85`
```yaml
check:
  field: "security.performance.memory_usage_percent"
  operator: "less_than_or_equal"
  expected_value: 85
```

### **🔍 String İşlem Operatörleri**

#### **`contains`**
- **Açıklama**: String içeriyor mu?
- **Kullanım**: String değerler için
- **Örnek**: `security.antivirus.vendor` contains `"Microsoft"`
```yaml
check:
  field: "security.antivirus.vendor"
  operator: "contains"
  expected_value: "Microsoft"
```

#### **`not_contains`**
- **Açıklama**: String içermiyor mu?
- **Kullanım**: String değerler için
- **Örnek**: `security.antivirus.vendor` not contains `"Unknown"`
```yaml
check:
  field: "security.antivirus.vendor"
  operator: "not_contains"
  expected_value: "Unknown"
```

#### **`starts_with`**
- **Açıklama**: String ile başlıyor mu?
- **Kullanım**: String değerler için
- **Örnek**: `system.os.name` starts with `"Windows"`
```yaml
check:
  field: "system.os.name"
  operator: "starts_with"
  expected_value: "Windows"
```

#### **`ends_with`**
- **Açıklama**: String ile bitiyor mu?
- **Kullanım**: String değerler için
- **Örnek**: `system.os.version` ends with `".0"`
```yaml
check:
  field: "system.os.version"
  operator: "ends_with"
  expected_value: ".0"
```

### **📋 Liste İşlem Operatörleri**

#### **`in`**
- **Açıklama**: Değer listede var mı?
- **Kullanım**: String, number değerler için
- **Örnek**: `security.mfa.method` in `["TOTP", "Hardware", "Biometric"]`
```yaml
check:
  field: "security.mfa.method"
  operator: "in"
  expected_value: ["TOTP", "Hardware", "Biometric"]
```

#### **`not_in`**
- **Açıklama**: Değer listede yok mu?
- **Kullanım**: String, number değerler için
- **Örnek**: `security.antivirus.status` not in `["disabled", "unknown"]`
```yaml
check:
  field: "security.antivirus.status"
  operator: "not_in"
  expected_value: ["disabled", "unknown"]
```

### **🔍 Null Kontrol Operatörleri**

#### **`is_null`**
- **Açıklama**: Değer null/undefined mı?
- **Kullanım**: Tüm tipler için
- **Örnek**: `security.incident_response.team_contact` is null
```yaml
check:
  field: "security.incident_response.team_contact"
  operator: "is_null"
  expected_value: null
```

#### **`is_not_null`**
- **Açıklama**: Değer null/undefined değil mi?
- **Kullanım**: Tüm tipler için
- **Örnek**: `security.incident_response.team_contact` is not null
```yaml
check:
  field: "security.incident_response.team_contact"
  operator: "is_not_null"
  expected_value: null
```

### **🔧 Gelişmiş Operatörler**

#### **`regex_match`**
- **Açıklama**: Regex pattern ile eşleşiyor mu?
- **Kullanım**: String değerler için
- **Örnek**: `system.hostname` matches `"^[A-Z0-9-]+$"`
```yaml
check:
  field: "system.hostname"
  operator: "regex_match"
  expected_value: "^[A-Z0-9-]+$"
```

## 🎯 **Kullanım Senaryoları**

### **1. Boolean Kontroller**
```yaml
# Firewall etkin mi?
check:
  field: "security.firewall.enabled"
  operator: "equals"
  expected_value: true
```

### **2. Sayısal Eşik Kontrolleri**
```yaml
# CPU kullanımı %80'den az mı?
check:
  field: "security.performance.cpu_usage_percent"
  operator: "less_than"
  expected_value: 80
```

### **3. String İçerik Kontrolleri**
```yaml
# Antivirüs Microsoft mu?
check:
  field: "security.antivirus.vendor"
  operator: "contains"
  expected_value: "Microsoft"
```

### **4. Liste Üyelik Kontrolleri**
```yaml
# MFA yöntemi güvenli mi?
check:
  field: "security.mfa.method"
  operator: "in"
  expected_value: ["TOTP", "Hardware", "Biometric"]
```

### **5. Null Kontrolleri**
```yaml
# Incident response team contact var mı?
check:
  field: "security.incident_response.team_contact"
  operator: "is_not_null"
  expected_value: null
```

## ⚠️ **Önemli Notlar**

### **Tip Uyumluluğu**
- **Boolean**: `equals`, `not_equals`
- **Number**: `equals`, `not_equals`, `greater_than`, `less_than`, `greater_than_or_equal`, `less_than_or_equal`
- **String**: `equals`, `not_equals`, `contains`, `not_contains`, `starts_with`, `ends_with`, `regex_match`
- **Array**: `in`, `not_in`

### **Performance İpuçları**
- **`equals`** en hızlı operatör
- **`regex_match`** en yavaş operatör
- **`contains`** büyük string'lerde yavaş olabilir
- **`in`** küçük listeler için hızlı

### **Hata Yönetimi**
- Geçersiz field yolları için hata
- Tip uyumsuzlukları için uyarı
- Null değerler için güvenli kontrol
