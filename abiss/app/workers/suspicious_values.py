{
  "account_security": {
    "type": "object",
    "properties": {
      "suspicious_login_detection": { "type": "boolean" }
    }
  },
  "services": {
    "type": "object",
    "properties": {
      "suspicious_services": { "type": "array", "items": { "type": "string" } }
    }
  },
  "processes": {
    "type": "object",
    "properties": {
      "suspicious_processes": { "type": "array", "items": { "type": "string" } }
    }
  },
  "files": {
    "type": "object",
    "properties": {
      "suspicious_files": { "type": "array", "items": { "type": "string" } }
    }
  },
  "registry": {
    "type": "object",
    "properties": {
      "suspicious_keys": { "type": "array", "items": { "type": "string" } }
    }
  },
  "dns": {
    "type": "object",
    "properties": {
      "suspicious_dns_queries": { "type": "array", "items": { "type": "string" } }
    }
  },
  "browsers": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "suspicious_extensions": { "type": "array", "items": { "type": "string" } }
      }
    }
  },
  "threat_intelligence": {
    "type": "object",
    "description": "Tehdit istihbaratı",
    "properties": {
      "suspicious_ips": { "type": "array", "items": { "type": "string" } },
      "malicious_domains": { "type": "array", "items": { "type": "string" } },
      "suspicious_hashes": { "type": "array", "items": { "type": "string" } },
      "tor_usage": { "type": "boolean" },
      "geolocation_anomalies": { "type": "array", "items": { "type": "string" } }
    }
  }
}
