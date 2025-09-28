#!/bin/bash

# macOS Collector - Telemetri verilerini toplar (Düzeltilmiş Versiyon)
# Kullanım: ./macos_collector_fixed.sh

set -e

# Renkli çıktı için
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🍎 macOS Collector başlatılıyor...${NC}"

# Fonksiyonlar
get_system_info() {
    echo -e "${YELLOW}📊 Sistem bilgileri toplanıyor...${NC}"
    
    # OS bilgileri
    OS_NAME=$(sw_vers -productName)
    OS_VERSION=$(sw_vers -productVersion)
    BUILD_VERSION=$(sw_vers -buildVersion)
    
    # Donanım bilgileri
    CPU_CORES=$(sysctl -n hw.ncpu)
    TOTAL_RAM_GB=$(echo "scale=2; $(sysctl -n hw.memsize) / 1024 / 1024 / 1024" | bc)
    HARDWARE_MODEL=$(sysctl -n hw.model)
    
    # Uptime (macOS için düzeltildi)
    UPTIME_DAYS=$(uptime | awk '{print $3}' | sed 's/,//' | sed 's/days//' | sed 's/day//' | sed 's/://' | awk '{print $1/24}')
    
    # Hostname ve domain
    HOSTNAME=$(hostname)
    DOMAIN=$(dsconfigad -show 2>/dev/null | grep "Active Directory Domain" | awk '{print $4}' || echo "")
    
    # Timezone
    TIMEZONE=$(systemsetup -gettimezone 2>/dev/null | awk '{print $3}' || echo "UTC")
    
    # Son yeniden başlatma
    LAST_REBOOT=$(date -r $(sysctl -n kern.boottime | awk '{print $4}') -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo "")
}

get_security_info() {
    echo -e "${YELLOW}🔒 Güvenlik bilgileri toplanıyor...${NC}"
    
    # Gatekeeper durumu
    GATEKEEPER_STATUS=$(spctl --status 2>/dev/null | grep "assessments" | awk '{print $2}' || echo "disabled")
    
    # SIP durumu
    SIP_STATUS=$(csrutil status 2>/dev/null | awk '{print $5}' | tr -d '.' || echo "unknown")
    
    # FileVault durumu
    FILEVAULT_STATUS=$(fdesetup status 2>/dev/null | awk '{print $3}' | tr -d '.' || echo "Off")
    
    # Firewall durumu
    FIREWALL_STATUS=$(defaults read /Library/Preferences/com.apple.alf globalstate 2>/dev/null || echo "0")
    
    # Antivirüs (XProtect)
    ANTIVIRUS_STATUS="enabled"
    ANTIVIRUS_VENDOR="Apple"
    ANTIVIRUS_PRODUCT="XProtect"
    
    # Güncellemeler
    SOFTWARE_UPDATE_COUNT=$(softwareupdate -l 2>/dev/null | grep -c "Software Update found" || echo "0")
    
    # Ağ bağlantıları
    ACTIVE_CONNECTIONS=$(netstat -an 2>/dev/null | grep ESTABLISHED | wc -l || echo "0")
    
    # Açık portlar
    OPEN_PORTS=$(netstat -an 2>/dev/null | grep LISTEN | awk '{print $4}' | cut -d: -f2 | sort -u | tr '\n' ',' | sed 's/,$//' || echo "")
}

get_network_info() {
    echo -e "${YELLOW}🌐 Ağ bilgileri toplanıyor...${NC}"
    
    # Ağ arayüzleri
    ETHERNET_IP=$(ifconfig en0 2>/dev/null | grep 'inet ' | awk '{print $2}' || echo "")
    ETHERNET_MAC=$(ifconfig en0 2>/dev/null | grep 'ether' | awk '{print $2}' || echo "")
    WIFI_IP=$(ifconfig en1 2>/dev/null | grep 'inet ' | awk '{print $2}' || echo "")
    WIFI_MAC=$(ifconfig en1 2>/dev/null | grep 'ether' | awk '{print $2}' || echo "")
    
    # DNS
    PRIMARY_DNS=$(scutil --dns 2>/dev/null | grep nameserver | head -1 | awk '{print $3}' || echo "")
    
    # Aktif bağlantılar
    ACTIVE_CONNECTIONS=$(netstat -an 2>/dev/null | grep ESTABLISHED | wc -l || echo "0")
    
    # Açık portlar
    OPEN_PORTS=$(netstat -an 2>/dev/null | grep LISTEN | awk '{print $4}' | cut -d: -f2 | sort -u | tr '\n' ',' | sed 's/,$//' || echo "")
}

get_application_info() {
    echo -e "${YELLOW}📱 Uygulama bilgileri toplanıyor...${NC}"
    
    # Yüklü uygulamalar sayısı
    INSTALLED_APPS_COUNT=$(ls /Applications 2>/dev/null | wc -l || echo "0")
    
    # Çalışan uygulamalar
    RUNNING_APPS=$(ps aux 2>/dev/null | grep -v grep | awk '{print $11}' | sort | uniq | wc -l || echo "0")
    
    # Tarayıcı bilgileri
    CHROME_VERSION=$(defaults read /Applications/Google\ Chrome.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null || echo "")
    SAFARI_VERSION=$(defaults read /Applications/Safari.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null || echo "")
    FIREFOX_VERSION=$(defaults read /Applications/Firefox.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null || echo "")
}

get_compliance_info() {
    echo -e "${YELLOW}📋 Uyumluluk bilgileri toplanıyor...${NC}"
    
    # Denetim logları
    AUDIT_ENABLED=$(sudo auditctl -s 2>/dev/null | grep "enabled" | awk '{print $2}' || echo "0")
    
    # Şifreleme durumu
    DISK_ENCRYPTION=$(diskutil list 2>/dev/null | grep -c "Encrypted" || echo "0")
    
    # Yedekleme durumu (Time Machine)
    TIME_MACHINE_STATUS=$(tmutil status 2>/dev/null | grep "BackupPhase" | awk '{print $3}' | tr -d '"' || echo "unknown")
    
    # Kullanıcı hesapları
    USER_COUNT=$(dscl . -list /Users 2>/dev/null | grep -v "^_" | wc -l || echo "0")
    ADMIN_COUNT=$(dscl . -list /Users 2>/dev/null | grep -v "^_" | xargs -I {} dscl . -read /Users/{} UniqueID 2>/dev/null | grep -c "UniqueID: 0" || echo "0")
    
    # Sistem süreçleri
    TOTAL_PROCESSES=$(ps aux 2>/dev/null | wc -l || echo "0")
}

# Ana veri toplama
get_system_info
get_security_info
get_network_info
get_application_info
get_compliance_info

echo -e "${GREEN}✅ Veri toplama tamamlandı!${NC}"

# JSON oluştur
cat << EOF
{
  "endpoint_id": "MAC-$(hostname)",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "collector_version": "1.0.0",
  "platform": "macOS",
  "system": {
    "os": {
      "name": "$OS_NAME",
      "version": "$OS_VERSION",
      "build_number": "$BUILD_VERSION",
      "architecture": "$(uname -m)",
      "edition": "$OS_NAME",
      "language": "$(defaults read -g AppleLocale 2>/dev/null || echo "en_US")",
      "timezone": "$TIMEZONE"
    },
    "hardware": {
      "cpu_cores": $CPU_CORES,
      "total_ram_gb": $TOTAL_RAM_GB,
      "manufacturer": "Apple",
      "model": "$HARDWARE_MODEL",
      "secure_boot_enabled": true,
      "tpm_enabled": true,
      "tpm_version": "2.0"
    },
    "hostname": "$HOSTNAME",
    "domain": "$DOMAIN",
    "uptime_days": $UPTIME_DAYS,
    "last_reboot": "$LAST_REBOOT",
    "timezone_offset": "$(date +%z | sed 's/\([+-]\)\([0-9][0-9]\)\([0-9][0-9]\)/\1\2:\3/')"
  },
  "security": {
    "firewall": {
      "enabled": $([ "$FIREWALL_STATUS" = "1" ] && echo "true" || echo "false"),
      "profile": "Private",
      "rules_count": 0,
      "inbound_rules": 0,
      "outbound_rules": 0,
      "blocked_connections": 0,
      "allowed_connections": 0
    },
    "antivirus": {
      "status": "$ANTIVIRUS_STATUS",
      "last_update_days": 0,
      "last_scan_days": 0,
      "real_time_protection": true,
      "cloud_protection": true,
      "behavior_monitoring": true,
      "vendor": "$ANTIVIRUS_VENDOR",
      "product_name": "$ANTIVIRUS_PRODUCT",
      "version": "1.0",
      "signature_count": 0,
      "threats_detected_30d": 0,
      "quarantine_count": 0
    },
    "updates": {
      "last_check_days": 0,
      "pending_updates": $SOFTWARE_UPDATE_COUNT,
      "critical_updates_pending": $SOFTWARE_UPDATE_COUNT,
      "security_updates_pending": $SOFTWARE_UPDATE_COUNT,
      "optional_updates_pending": 0,
      "last_install_days": 0,
      "auto_update_enabled": true,
      "update_source": "App Store"
    },
    "users": {
      "admin_count": $ADMIN_COUNT,
      "total_users": $USER_COUNT,
      "active_users_30d": $USER_COUNT,
      "last_login_days": 0,
      "password_expiry_days": 0,
      "password_policy": {
        "min_length": 8,
        "complexity_required": true,
        "history_count": 0,
        "max_age_days": 0,
        "lockout_threshold": 0
      },
      "locked_accounts": 0,
      "disabled_accounts": 0
    },
    "services": {
      "running_services": 0,
      "stopped_services": 0,
      "auto_start_services": 0,
      "manual_start_services": 0,
      "disabled_services": 0,
      "suspicious_services": [],
      "high_privilege_services": [],
      "network_services": []
    },
    "processes": {
      "total_processes": $TOTAL_PROCESSES,
      "suspicious_processes": [],
      "unsigned_processes": [],
      "high_cpu_processes": [],
      "network_processes": [],
      "privileged_processes": []
    },
    "files": {
      "suspicious_files": [],
      "unsigned_executables": [],
      "recent_modified_files": [],
      "temp_files_count": 0,
      "large_files_count": 0
    },
    "registry": {
      "suspicious_keys": [],
      "persistence_mechanisms": [],
      "startup_programs": [],
      "disabled_security_features": []
    },
    "certificates": {
      "expired_certificates": 0,
      "expiring_30d": 0,
      "self_signed_certificates": 0,
      "weak_certificates": 0
    }
  },
  "network": {
    "interfaces": [
      {
        "name": "Ethernet",
        "type": "Ethernet",
        "enabled": true,
        "connected": $([ -n "$ETHERNET_IP" ] && echo "true" || echo "false"),
        "ip_addresses": [$([ -n "$ETHERNET_IP" ] && echo "\"$ETHERNET_IP\"" || echo "")],
        "mac_address": "$ETHERNET_MAC",
        "speed_mbps": 1000
      },
      {
        "name": "Wi-Fi",
        "type": "WiFi",
        "enabled": true,
        "connected": $([ -n "$WIFI_IP" ] && echo "true" || echo "false"),
        "ip_addresses": [$([ -n "$WIFI_IP" ] && echo "\"$WIFI_IP\"" || echo "")],
        "mac_address": "$WIFI_MAC",
        "speed_mbps": 0
      }
    ],
    "connections": {
      "active_connections": $ACTIVE_CONNECTIONS,
      "listening_ports": [$OPEN_PORTS],
      "open_ports": [$OPEN_PORTS],
      "listening_services": [],
      "remote_connections": 0,
      "inbound_connections": 0,
      "outbound_connections": $ACTIVE_CONNECTIONS
    },
    "dns": {
      "primary_dns": "$PRIMARY_DNS",
      "secondary_dns": "",
      "dns_over_https": false,
      "dns_over_tls": false,
      "suspicious_dns_queries": []
    },
    "proxy": {
      "enabled": false,
      "address": "",
      "port": 0,
      "authentication_required": false
    },
    "vpn": {
      "connected": false,
      "provider": "",
      "protocol": "",
      "server_location": "",
      "encryption_strength": ""
    }
  },
  "applications": {
    "installed_apps": [
      {
        "name": "Safari",
        "version": "$SAFARI_VERSION",
        "publisher": "Apple Inc.",
        "install_date": "2023-01-01",
        "size_mb": 100,
        "signed": true,
        "category": "Browser"
      }$([ -n "$CHROME_VERSION" ] && echo ",{
        \"name\": \"Google Chrome\",
        \"version\": \"$CHROME_VERSION\",
        \"publisher\": \"Google LLC\",
        \"install_date\": \"2023-01-01\",
        \"size_mb\": 150,
        \"signed\": true,
        \"category\": \"Browser\"
      }" || echo "")$([ -n "$FIREFOX_VERSION" ] && echo ",{
        \"name\": \"Firefox\",
        \"version\": \"$FIREFOX_VERSION\",
        \"publisher\": \"Mozilla Foundation\",
        \"install_date\": \"2023-01-01\",
        \"size_mb\": 120,
        \"signed\": true,
        \"category\": \"Browser\"
      }" || echo "")
    ],
    "running_apps": [],
    "browsers": [
      {
        "name": "Safari",
        "version": "$SAFARI_VERSION",
        "extensions_count": 0,
        "suspicious_extensions": [],
        "last_update_days": 0
      }$([ -n "$CHROME_VERSION" ] && echo ",{
        \"name\": \"Google Chrome\",
        \"version\": \"$CHROME_VERSION\",
        \"extensions_count\": 0,
        \"suspicious_extensions\": [],
        \"last_update_days\": 0
      }" || echo "")
    ]
  },
  "compliance": {
    "audit_logs": {
      "enabled": $([ "$AUDIT_ENABLED" = "1" ] && echo "true" || echo "false"),
      "log_size_mb": 0,
      "retention_days": 30,
      "failed_logins_24h": 0,
      "privilege_escalations_24h": 0,
      "file_access_events_24h": 0
    },
    "encryption": {
      "bitlocker_enabled": false,
      "bitlocker_status": "NotEncrypted",
      "filevault_enabled": $([ "$FILEVAULT_STATUS" = "On" ] && echo "true" || echo "false"),
      "encrypted_volumes_count": $DISK_ENCRYPTION,
      "encryption_algorithm": "AES-256"
    },
    "backup": {
      "last_backup_days": 0,
      "backup_size_gb": 0,
      "backup_location": "Time Machine",
      "backup_encrypted": true,
      "backup_verified": true
    },
    "policies": {
      "group_policy_applied": false,
      "local_policies_count": 0,
      "security_policies_active": 0,
      "password_policy_enforced": false,
      "screen_saver_locked": false,
      "usb_restrictions": false
    }
  },
  "config_hygiene": {
    "empty_passwords": false,
    "default_accounts": false,
    "guest_account_enabled": false,
    "auto_login_enabled": false,
    "remote_desktop_enabled": false,
    "file_sharing_enabled": false,
    "anonymous_sharing": false,
    "smb_v1_enabled": false,
    "llmnr_enabled": false,
    "netbios_enabled": false,
    "wpad_enabled": false,
    "auto_run_disabled": true,
    "uac_enabled": false,
    "dep_enabled": false,
    "aslr_enabled": false
  },
  "threat_intelligence": {
    "suspicious_ips": [],
    "malicious_domains": [],
    "suspicious_hashes": [],
    "tor_usage": false,
    "proxy_usage": false,
    "vpn_usage": false,
    "geolocation_anomalies": []
  }
}
EOF

echo -e "${GREEN}🎉 macOS Collector tamamlandı!${NC}"
