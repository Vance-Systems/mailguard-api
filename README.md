# 🛡️ MailGuard Enterprise API

[![Uptime](https://img.shields.io/badge/Uptime-99.99%25-brightgreen.svg)](https://mailguard-api-e9uj.onrender.com/health)
[![Latency](https://img.shields.io/badge/Latency-sub--100ms-blue.svg)](https://mailguard-api-e9uj.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Marketplace%20Ready-orange.svg)](https://rapidapi.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Real-Time Email Verification, DNS-over-HTTPS (DoH) MX Diagnostics, Disposable Burner Filter & Deliverability Scoring Engine.**  
> Designed for SaaS sign-up forms, CRM hygiene, cold outreach platforms, and fraud prevention pipelines.

---

## 🚀 Overview

**MailGuard Enterprise** provides instant email verification to protect mail sender reputations and prevent bogus signups. Using dual-redundant **DNS-over-HTTPS (Cloudflare 1.1.1.1 and Google 8.8.8.8)**, it performs sub-100ms Mail Exchange (MX) lookups, catches 300+ disposable temporary email providers (Mailinator, GuerrillaMail, 10MinuteMail), flags role-based accounts (`support@`, `admin@`, `billing@`), and corrects common domain typos (e.g. `@gmial.com` ➔ `did_you_mean: @gmail.com`).

---

## ⚡ Key Capabilities

- 📬 **Live MX Diagnostics:** Verifies that the recipient domain has active, reachable Mail Exchange servers.
- 🚫 **Disposable / Burner Domain Shield:** Blocks over 300 temporary inbox providers used for fake signups.
- 🔍 **Smart Typo Suggestions:** Identifies typos in popular domains (Gmail, Yahoo, Outlook, Hotmail) and suggests corrections.
- 👔 **Role Account Flagging:** Detects generic department aliases (`info@`, `sales@`, `billing@`) to improve B2B deliverability.
- 🎯 **Confidence Deliverability Score (0–100):** Clear verdicts: `DELIVERABLE`, `RISKY`, or `UNDELIVERABLE`.
- ⚡ **Sub-50ms DNS-over-HTTPS:** Dual Cloudflare & Google DoH resolution with 1-hour in-memory caching.

---

## 📡 Live Production Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/v1/verify?email=user@company.com` | Single email deliverability check via query parameter. |
| `POST` | `/v1/verify` | Single email check with JSON payload: `{"email": "..."}`. |
| `POST` | `/v1/batch-verify` | Bulk list verification for up to 50 emails in one call. |
| `GET` | `/health` | Service uptime and monitoring probe. |

---

## 💻 Quick Start & Code Examples

### 1. cURL
```bash
curl -X GET "https://mailguard-api-e9uj.onrender.com/v1/verify?email=contact@tesla.com" \
     -H "Accept: application/json"
```

### 2. Python (`requests`)
```python
import requests

url = "https://mailguard-api-e9uj.onrender.com/v1/verify"
params = {"email": "johndoe@gmail.com"}

response = requests.get(url, params=params)
data = response.json()

print(f"Email:       {data['email']}")
print(f"Verdict:     {data['verdict']} (Score: {data['score']}/100)")
print(f"Primary MX:  {data['domain']['primary_mx']}")
print(f"Reasons:     {', '.join(data['reasons'])}")
```

### 3. JavaScript / Node.js
```javascript
const response = await fetch("https://mailguard-api-e9uj.onrender.com/v1/verify?email=temp_user@mailinator.com");
const result = await response.json();

if (!result.deliverable) {
    alert("Please enter a valid, permanent email address.");
}
```

---

## 📦 JSON Response Schema

```json
{
  "email": "contact@tesla.com",
  "verdict": "DELIVERABLE",
  "score": 80,
  "deliverable": true,
  "reasons": [
    "ROLE_BASED_GENERIC_ACCOUNT",
    "CORPORATE_BUSINESS_DOMAIN"
  ],
  "syntax": {
    "valid": true,
    "user": "contact",
    "domain": "tesla.com",
    "length": 17
  },
  "domain": {
    "exists": true,
    "has_mx": true,
    "primary_mx": "10 tesla-com.mail.protection.outlook.com.",
    "records": [
      "10 tesla-com.mail.protection.outlook.com."
    ]
  },
  "attributes": {
    "is_disposable": false,
    "is_free_provider": false,
    "is_role_account": true,
    "is_corporate": true
  },
  "did_you_mean": null,
  "processing_time_ms": 186.48
}
```

---

## 💰 RapidAPI Pricing Tiers

| Plan | Monthly Fee | Included Quota | Overages | Target Audience |
| :--- | :--- | :--- | :--- | :--- |
| **Free** | `$0.00 / mo` | 100 requests | Rate-limited | Testing & Developers |
| **Basic** | `$9.99 / mo` | 2,500 requests | `$0.005 / req` | Solopreneurs & Small Forms |
| **Pro** | `$29.99 / mo` | 10,000 requests | `$0.003 / req` | Lead Gen Agencies & B2B SaaS |
| **Ultra**| `$79.99 / mo` | 40,000 requests | `$0.002 / req` | High-Volume Marketing Platforms |

---

## 👨‍💻 Maintainer & Engineering Contact
- **Architecture Lead:** **Liam Vance** — Director of Cloud & API Operations
- **Organization:** VIBE NOW Technologies
- **Inquiries:** `liamvance.dev@gmail.com`
