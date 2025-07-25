# 🛡️ Phishing Awareness Demo (Educational Only)

This project simulates a phishing login page to help raise awareness of phishing attacks. **It is intended for educational and security training purposes only.**

## 🚀 Features

- ✅ Fake login form (HTML/CSS)
- 🌙 Dark mode toggle
- 📱 Responsive design
- 🧠 Phishing awareness tips in a modal
- ✉️ Email alerts when credentials are captured
- 📂 Instructor-only log viewer (with authentication)
- 🔁 Real-time log updates (via AJAX)
- 🐳 Dockerized for easy deployment

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/phishing-awareness-demo.git
cd phishing-awareness-demo
```

### 2. Create `.env` for sensitive config

```env
EMAIL_ADDRESS=youremail@example.com
EMAIL_PASSWORD=your-app-password
TO_EMAIL=receiver@example.com
LOG_VIEW_PASSWORD=letmein123
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Docker Deployment

```bash
docker build -t phishing-awareness .
docker run -p 5000:5000 phishing-awareness
```

---

## 🧪 Usage

- Visit `http://localhost:5000/` to view the phishing demo
- Enter any test credentials (⚠️ not real ones)
- Check `captured_log.txt` or visit `/view-logs` (requires password)
- Email alert will be sent to configured address

---

## 📜 Disclaimer

This project is for **ethical hacking education and cybersecurity awareness only**. Do **NOT** use it for real-world credential harvesting.

---

## 📄 License

MIT License