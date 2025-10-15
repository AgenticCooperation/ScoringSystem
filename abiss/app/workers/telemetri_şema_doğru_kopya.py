{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Comprehensive Endpoint Security Telemetry Schema",
  "description": "Kapsamlı endpoint güvenlik telemetri verilerinin detaylı şeması",
  "type": "object",
  "required": ["endpoint_id", "timestamp", "system", "security", "network", "applications", "compliance"],
  "properties": {
    "endpoint_id": {
      "type": "string",
      "description": "Endpoint benzersiz kimliği"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Veri toplama zamanı"
    },
    "collector_version": {
      "type": "string",
      "description": "Collector agent versiyonu"
    },
    "platform": {
      "type": "string",
      "enum": ["Windows", "Linux", "macOS"],
      "description": "İşletim sistemi platformu"
    },
    "system": {
      "type": "object",
      "description": "Detaylı sistem bilgileri",
      "properties": {
        "os": {
          "type": "object",
          "properties": {
            "name": {"type": "string", "enum": ["Windows", "Linux", "macOS", "FreeBSD"]},
            "version": {"type": "string"},
            "build_number": {"type": "string"},
            "patch_level": {"type": "string"},
            "architecture": {"type": "string", "enum": ["x64", "x86", "arm64", "arm32"]},
            "edition": {"type": "string"},
            "language": {"type": "string"}
          }
        },
        "hardware": {
          "type": "object",
          "properties": {
            "bios_version": {"type": "string"},
            "secure_boot_enabled": {"type": "boolean"},
            "tpm_enabled": {"type": "boolean"},
            "tpm_version": {"type": "string"},
            "gatekeeper_enabled": {"type": "boolean"}
          }
        },
        "hostname": {"type": "string"},
        "domain": {"type": "string"},
        "workgroup": {"type": "string"},
        "uptime_days": {"type": "number", "minimum": 0},
        "last_reboot": {"type": "string", "format": "date-time"},
        "timezone_offset": {"type": "number"}
      }
    },
    "security": {
      "type": "object",
      "description": "Kapsamlı güvenlik durumu",
      "properties": {
        "firewall": {
          "type": "object",
          "properties": {
            "enabled": {"type": "boolean"},
            "profile": {"type": "string", "enum": ["Domain", "Private", "Public"]},
            "rules_count": {"type": "number", "minimum": 0},
            "inbound_rules": {"type": "number", "minimum": 0},
            "outbound_rules": {"type": "number", "minimum": 0},
            "blocked_connections": {"type": "number", "minimum": 0},
            "allowed_connections": {"type": "number", "minimum": 0},
            "last_log_entry": {"type": "string", "format": "date-time"}
          }
        },
        "antivirus": {
          "type": "object",
          "properties": {
            "status": {"type": "string", "enum": ["enabled", "disabled", "unknown", "error"]},
            "last_update_days": {"type": "number", "minimum": 0},
            "last_scan_days": {"type": "number", "minimum": 0},
            "real_time_protection": {"type": "boolean"},
            "cloud_protection": {"type": "boolean"},
            "behavior_monitoring": {"type": "boolean"},
            "vendor": {"type": "string"},
            "product_name": {"type": "string"},
            "version": {"type": "string"},
            "signature_count": {"type": "number", "minimum": 0},
            "threats_detected_30d": {"type": "number", "minimum": 0},
            "quarantine_count": {"type": "number", "minimum": 0}
          }
        },
        "updates": {
          "type": "object",
          "properties": {
            "last_check_days": {"type": "number", "minimum": 0},
            "pending_updates": {"type": "number", "minimum": 0},
            "critical_updates_pending": {"type": "number", "minimum": 0},
            "security_updates_pending": {"type": "number", "minimum": 0},
            "optional_updates_pending": {"type": "number", "minimum": 0},
            "last_install_days": {"type": "number", "minimum": 0},
            "auto_update_enabled": {"type": "boolean"},
            "update_source": {"type": "string", "enum": ["WSUS", "Windows Update", "Manual", "Third Party"]}
          }
        },
        "users": {
          "type": "object",
          "properties": {
            "admin_count": {"type": "number", "minimum": 0},
            "total_users": {"type": "number", "minimum": 0},
            "active_users_30d": {"type": "number", "minimum": 0},
            "last_login_days": {"type": "number", "minimum": 0},
            "password_expiry_days": {"type": "number"},
            "password_policy": {
              "type": "object",
              "properties": {
                "min_length": {"type": "number", "minimum": 0},
                "complexity_required": {"type": "boolean"},
                "history_count": {"type": "number", "minimum": 0},
                "max_age_days": {"type": "number", "minimum": 0},
                "lockout_threshold": {"type": "number", "minimum": 0}
              }
            },
            "disabled_accounts": {"type": "number", "minimum": 0}
          }
        },

        "vulnerabilities": {
          "type": "object",
          "properties": {
            "critical_vulns": {"type": "number", "minimum": 0},
            "high_vulns": {"type": "number", "minimum": 0},
            "medium_vulns": {"type": "number", "minimum": 0},
            "unpatched_critical": {"type": "number", "minimum": 0},
            "cve_count": {"type": "number", "minimum": 0},
            "exploit_available": {"type": "number", "minimum": 0},
            "last_scan_days": {"type": "number", "minimum": 0}
          }
        },
        "logging": {
          "type": "object",
          "properties": {
            "security_logs_enabled": {"type": "boolean"},
            "audit_logs_enabled": {"type": "boolean"},
            "log_retention_days": {"type": "number", "minimum": 0},
            "log_forwarding_enabled": {"type": "boolean"},
          }
        },

        "performance": {
          "type": "object",
          "properties": {
            "cpu_usage_percent": {"type": "number", "minimum": 0, "maximum": 100},
            "memory_usage_percent": {"type": "number", "minimum": 0, "maximum": 100},
            "disk_usage_percent": {"type": "number", "minimum": 0, "maximum": 100},
            "network_utilization_percent": {"type": "number", "minimum": 0, "maximum": 100},
            "system_load": {"type": "number", "minimum": 0}
          }
        },
        "health": {
          "type": "object",
          "properties": {
            "error_rate_24h": {"type": "number", "minimum": 0},
            "crash_count_7d": {"type": "number", "minimum": 0},
            "blue_screen_count_30d": {"type": "number", "minimum": 0},
            "hardware_failures": {"type": "number", "minimum": 0}
          }
        },
        "data_protection": {
          "type": "object",
          "properties": {
            "dlp_enabled": {"type": "boolean"},
            "data_classification": {"type": "string", "enum": ["Public", "Internal", "Confidential", "Restricted"]},
            "encryption_at_rest": {"type": "boolean"},
          }
        },
        "backup_recovery": {
          "type": "object",
          "properties": {
            "last_backup_days": {"type": "number", "minimum": 0},
            "backup_encrypted": {"type": "boolean"},
            "backup_verified": {"type": "boolean"},
            "recovery_time_objective": {"type": "number", "minimum": 0},
            "recovery_point_objective": {"type": "number", "minimum": 0},
            "disaster_recovery_plan": {"type": "boolean"}
          }
        },

        "services": {
          "type": "object",
          "properties": {
            "running_services": {"type": "number", "minimum": 0},
            "stopped_services": {"type": "number", "minimum": 0},
            "auto_start_services": {"type": "number", "minimum": 0},
            "manual_start_services": {"type": "number", "minimum": 0},
            "disabled_services": {"type": "number", "minimum": 0},
            "suspicious_services": {"type": "array", "items": {"type": "string"}},
            "high_privilege_services": {"type": "array", "items": {"type": "string"}},
            "network_services": {"type": "array", "items": {"type": "string"}}
          }
        },
        "processes": {
          "type": "object",
          "properties": {
            "total_processes": {"type": "number", "minimum": 0},
            "suspicious_processes": {"type": "array", "items": {"type": "string"}},
            "unsigned_processes": {"type": "array", "items": {"type": "string"}},
            "high_cpu_processes": {"type": "array", "items": {"type": "string"}},
            "network_processes": {"type": "array", "items": {"type": "string"}},
            "privileged_processes": {"type": "array", "items": {"type": "string"}}
          }
        },
        "files": {
          "type": "object",
          "properties": {
            "unsigned_executables": {"type": "array", "items": {"type": "string"}},
            "recent_modified_files": {"type": "array", "items": {"type": "string"}},
            "temp_files_count": {"type": "number", "minimum": 0},
            "large_files_count": {"type": "number", "minimum": 0}
          }
        },
        "registry": {
          "type": "object",
          "properties": {
            "persistence_mechanisms": {"type": "array", "items": {"type": "string"}},
            "startup_programs": {"type": "array", "items": {"type": "string"}},
          }
        },
        "certificates": {
          "type": "object",
          "properties": {
            "expired_certificates": {"type": "number", "minimum": 0},
            "expiring_30d": {"type": "number", "minimum": 0},
            "self_signed_certificates": {"type": "number", "minimum": 0},
            "weak_certificates": {"type": "number", "minimum": 0}
          }
        }
      }
    },
    "network": {
      "type": "object",
      "description": "Detaylı ağ güvenliği",
      "properties": {
        "interfaces": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "type": {"type": "string", "enum": ["Ethernet", "WiFi", "Bluetooth", "VPN", "Virtual"]},
              "enabled": {"type": "boolean"},
              "connected": {"type": "boolean"},
              "ip_addresses": {"type": "array", "items": {"type": "string"}},
              "mac_address": {"type": "string"},
              "speed_mbps": {"type": "number", "minimum": 0}
            }
          }
        },
        "connections": {
          "type": "object",
          "properties": {
            "active_connections": {"type": "number", "minimum": 0},
            "open_ports": {"type": "array", "items": {"type": "number"}},
            "listening_services": {"type": "array", "items": {"type": "string"}},
            "remote_connections": {"type": "number", "minimum": 0},
            "inbound_connections": {"type": "number", "minimum": 0},
            "outbound_connections": {"type": "number", "minimum": 0}
          }
        },
        "dns": {
          "type": "object",
          "properties": {
            "primary_dns": {"type": "string"},
            "secondary_dns": {"type": "string"},
            "dns_over_https": {"type": "boolean"},
            "dns_over_tls": {"type": "boolean"},
          }
        },
        "proxy": {
          "type": "object",
          "properties": {
            "enabled": {"type": "boolean"},
            "address": {"type": "string"},
            "port": {"type": "number", "minimum": 1, "maximum": 65535},
            "authentication_required": {"type": "boolean"}
          }
        },
        "vpn": {
          "type": "object",
          "properties": {
            "connected": {"type": "boolean"},
            "provider": {"type": "string"},
            "protocol": {"type": "string"},
            "server_location": {"type": "string"},
            "encryption_strength": {"type": "string"}
          }
        }
      }
    },
    "applications": {
      "type": "object",
      "description": "Uygulama güvenliği",
      "properties": {
        "installed_apps": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "version": {"type": "string"},
              "publisher": {"type": "string"},
              "install_date": {"type": "string", "format": "date"},
              "size_mb": {"type": "number", "minimum": 0},
              "signed": {"type": "boolean"},
              "category": {"type": "string"}
            }
          }
        },
        "running_apps": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "pid": {"type": "number"},
              "cpu_usage": {"type": "number", "minimum": 0, "maximum": 100},
              "memory_mb": {"type": "number", "minimum": 0},
              "network_connections": {"type": "number", "minimum": 0},
              "privileges": {"type": "string", "enum": ["User", "Admin", "System"]}
            }
          }
        },
        "browsers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "version": {"type": "string"},
              "extensions_count": {"type": "number", "minimum": 0},
              "last_update_days": {"type": "number", "minimum": 0}
            }
          }
        }
      }
    },
    "compliance": {
      "type": "object",
      "description": "Uyumluluk ve denetim",
      "properties": {
        "encryption": {
          "type": "object",
          "properties": {
            "encryption_enabled": {"type": "boolean"},
            "encryption_status": {"type": "string", "enum": ["FullyEncrypted", "PartiallyEncrypted", "NotEncrypted"]},
            "encryption_algorithm": {"type": "string"}
          }
        },
        "policies": {
          "type": "object",
          "properties": {
            "group_policy_applied": {"type": "boolean"},
            "local_policies_count": {"type": "number", "minimum": 0},
            "security_policies_active": {"type": "number", "minimum": 0},
            "screen_saver_locked": {"type": "boolean"},
            "usb_restrictions": {"type": "boolean"}
          }
        }
      }
    },
    "config_hygiene": {
      "type": "object",
      "description": "Konfigürasyon hijyeni",
      "properties": {
        "empty_passwords": {"type": "boolean"},
        "default_accounts": {"type": "boolean"},
        "guest_account_enabled": {"type": "boolean"},
        "auto_login_enabled": {"type": "boolean"},
        "remote_desktop_enabled": {"type": "boolean"},
        "file_sharing_enabled": {"type": "boolean"},
        "anonymous_sharing": {"type": "boolean"},
        "smb_v1_enabled": {"type": "boolean"},
        "telnet_enabled": {"type": "boolean"},
        "ftp_enabled": {"type": "boolean"},
        "llmnr_enabled": {"type": "boolean"},
        "netbios_enabled": {"type": "boolean"},
        "wpad_enabled": {"type": "boolean"},
        "auto_run_disabled": {"type": "boolean"},
        "uac_enabled": {"type": "boolean"},
        "dep_enabled": {"type": "boolean"},
        "aslr_enabled": {"type": "boolean"}
      }
    },
  }
}
