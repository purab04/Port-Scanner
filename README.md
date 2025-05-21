# 🔍 Port Scanner Project

A Python-based **Port Scanner** that scans a target host for open ports, identifies services, grabs banners, and displays results in a color-coded table with real-time progress updates.

---

## 📌 Features

- ✅ Scans a target host within a specified port range
- 🚀 Multithreaded for fast scanning using `ThreadPoolExecutor`
- 📡 Retrieves banners from open ports (when available)
- 🎨 Formatted and colorized output using ANSI codes
- 🔁 Live progress display using `sys.stdout`

---

## 🧠 Prerequisites

- Basic knowledge of networking (ports, IPs, services)
- Python 3 installed
- Run from a terminal that supports ANSI color codes (Linux/macOS or Git Bash on Windows)

---

## 📦 Dependencies

Only uses Python standard libraries:
- `socket`
- `sys`
- `concurrent.futures`

---

## 🚀 Usage

1. Clone the repo or download the script:
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
