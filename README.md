# 📰 Automated News Archival Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-GPLv3-green)

An automated ETL (Extract, Transform, Load) pipeline designed to aggregate digital publications from limited-access sources and archive them to Scribd for permanent preservation. 

This project demonstrates the use of containerization, continuous integration, and automated challenge-response handling (CAPTCHA) to build resilient data collection workflows.

## 🚀 Features

* **Automated Extraction:** Scrapes specific PDF publications on a daily schedule.
* **Resilient Logic:** Integrates **2Captcha** to handle anti-bot challenges and maintain session continuity.
* **Cloud-Native:** Fully containerized with **Docker** for consistent execution across environments.
* **CI/CD:** Orchestrated via **GitHub Actions** to run autonomously without local intervention.
* **Session Management:** Securely handles authentication cookies (`_scribd_session`) via environment secrets.

---

## 🛠️ Architecture & Problem Solved

**The Challenge:**
Researchers and archivists often face difficulties preserving digital news media due to:
1.  Temporary availability windows (content disappears after 24 hours).
2.  Daily download quotas on source platforms.
3.  The need for manual, repetitive retrieval processes.

**The Solution:**
This pipeline acts as a middleware that:
1.  **Extracts** the document from the source.
2.  **Processes** the file (handling authentication and verification).
3.  **Loads** (Archives) the document to a centralized Scribd repository for long-term access.

---

## ⚙️ Configuration & Secrets

To run this pipeline, you need two key secrets. Set these as **Environment Variables** (locally) or **Repository Secrets** (on GitHub).

| Variable | Description |
| :--- | :--- |
| `SCRIBD_SESSION` | Your valid `_scribd_session` cookie value. This allows the script to upload as your user. |
| `CAPTCHA_KEY` | Your API key from [2Captcha](https://2captcha.com/). Used to solve security challenges during scraping. |

---

## 💻 Installation & Usage

### Option 1: Running with Docker (Recommended)

The easiest way to run the application is via the pre-built container.

```bash
docker run \
  -e SCRIBD_SESSION="your_scribd_session_cookie" \
  -e CAPTCHA_KEY="your_2captcha_api_key" \
  ghcr.io/lsnnt/news-upload:latest
````

### Option 2: Running Locally (Python)

**1. Clone the repository**

```bash
git clone https://github.com/lsnnt/news-upload.git
cd news-upload
```

**2. Install dependencies**

```bash
pip3 install -r requirements.txt
```

**3. Set Environment Variables**

```bash
export SCRIBD_SESSION="your_long_session_string"
export CAPTCHA_KEY="your_captcha_key"
```

**4. Execute the pipeline**

```bash
python3 main.py
```

-----

## 🤝 Support & Contact

**Maintainer:** Nityanand Thakur

  * **Session:** `05501ebf09a0fe363d76046f0f2c027f3ce031bd649dbb94113622e6cb25563334`
  * **Email:** [tnityanand523@gmail.com](mailto:tnityanand523@gmail.com)
  * **Scribd Profile:** [View Archive](https://www.scribd.com/user/688308679/Nityanand-Thakur)

<details>
<summary><strong>🔐 Click to view PGP Public Key</strong></summary>

```text
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEaFvucBYJKwYBBAHaRw8BAQdAV1Was61jXtFiI12folbbWsQYKiWyfzMZwf8j
zC3fJxi0Kk5pdHlhbmFuZCBUaGFrdXIgPHRuaXR5YW5hbmQ1MjNAZ21haWwuY29t
PoiZBBMWCgBBFiEEdLmL82ejCEzIIC+vjf71D1ikMqYFAmhb7nACGwMFCQWjmoAF
CwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQjf71D1ikMqZfXAEAgETg8YN6
ABWqtQvevIWV4mcU8Whep/7sqq0SBQZWg/UA/0TNSUS/cHQB29JqElX4UgkRwH+C
gmXxKEN1uLdsdHAPuDgEaFvucBIKKwYBBAGXVQEFAQEHQEGOsxY0fyh9x9qB0OgL
QhlSv+ZSNXmo31713iL6ZWY+AwEIB4h+BBgWCgAmFiEEdLmL82ejCEzIIC+vjf71
D1ikMqYFAmhb7nACGwwFCQWjmoAACgkQjf71D1ikMqbgVwEAoDilntsraWSxGklf
BPpUhkYxbziUD9jXLyZoI+qUyRgA/i8MHCYkYBm8qYJXawR4GLxcM/OSEzfLgiCN
Jg9mg78E
=CX9H
-----END PGP PUBLIC KEY BLOCK-----
```

</details>

-----

## 📄 License

This project is licensed under the [GNU GPLv3 License](https://www.google.com/search?q=COPYING).

> **Disclaimer:** This tool is intended for educational purposes and personal archival use only. Users are responsible for ensuring their usage complies with the Terms of Service of the source platforms.

```
```