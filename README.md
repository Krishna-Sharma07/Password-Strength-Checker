---

<div align="center">
  <h1 align="center">🔐 Password Utility – Strength Checker & Generator</h1>
  <p align="center">
    A simple yet powerful <strong>web application</strong> built with Flask to <strong>test password strength</strong> and <strong>generate secure passwords</strong> instantly.<br />
    Improve your online security by learning what makes a password strong — and create one in seconds!
  </p>
  <br />
  <img src="https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Web-App-orange?style=for-the-badge" />
</div>

---

## 📋 Table of Contents

* [🌟 Features](#features)
* [🛠 Tech Stack](#tech-stack)
* [🚀 Getting Started](#getting-started)
* [📁 Project Structure](#project-structure)
* [🧠 Core Functionalities](#core-functionalities)
* [💡 Security Awareness](#security-awareness)
* [🤝 Contributing](#contributing)

---

## 🌟 Features

* ✅ **Real-time password strength checker** — evaluates complexity and gives live feedback
* 🔢 **Custom password generator** — create strong, random passwords of desired length
* 🧩 **Interactive UI** — instant updates for rules like uppercase, digits, and symbols
* 🔒 **Local-only testing** — no passwords are stored, sent, or logged anywhere
* 🧠 **Educational insights** on password hygiene and security importance
* 📱 **Responsive design** — clean and simple interface for all screen sizes

---

## 🛠 Tech Stack

| Layer         | Technology             |
| ------------- | ---------------------- |
| Language      | Python 3.10+           |
| Framework     | Flask (Jinja2, JSON)   |
| Frontend      | HTML, CSS, JavaScript  |
| Logic Module  | `checker_generator.py` |
| Communication | Fetch API (AJAX)       |

---

## 🚀 Getting Started

### 🧰 Prerequisites

* Python 3.10+
* Flask library

Install dependencies:

```bash
pip install flask
```

### 📦 Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

> 💡 Use the **Password Checker** link in the header to test a password, or the **Generator** link to create strong passwords.

---

## 📁 Project Structure

```
password-utility/
│
├── app.py                       # Flask app routes and backend logic
├── checker_generator.py          # Core logic for checking & generating passwords
│
├── templates/
│   ├── base.html                 # Main layout and homepage content
│   ├── checker.html              # Password strength checker page
│   └── generator.html            # Password generator page
│
├── static/
│   ├── css/
│   │   └── style.css             # Styles and layout for the web app
│   └── js/
│       └── checker.js            # Frontend logic for real-time checking
│
└── README.md                     # Project documentation
```

---

## 🧠 Core Functionalities

### 🔍 Password Strength Checker

* Evaluates a password based on:

  * Length (≥ 8 characters)
  * Uppercase and lowercase letters
  * Numbers and special symbols
* Displays **color-coded feedback** in real-time as you type.
* Classifies password as **Weak**, **Medium**, **Strong**, or **Very Strong**.

### ⚙️ Password Generator

* Create random, secure passwords instantly.
* Customize:

  * Length (6–32 characters)
  * Include/exclude uppercase, lowercase, digits, symbols
* Copy your generated password with a single click.

---

## 💡 Security Awareness

Strong passwords are your **first line of defense** online.
Avoid using:

* Common passwords like “123456”, “password”, or “admin”
* Reusing passwords across multiple sites
* Short or guessable words from personal information

A strong password should be:

> 🧩 Long • Complex • Unique • Hard to Guess

---

### ⚠️ Privacy Notice

We respect your privacy and security. ❤️
This tool **does not store, log, or transmit** your passwords.
All checks and generations happen **locally in your browser** using real-time processing.

🛡️ *Your passwords are yours alone — this app is made purely for awareness, education, and safety.*

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork this repository
2. Create your feature branch

   ```bash
   git checkout -b feature/improvement
   ```
3. Commit and push your changes
4. Open a Pull Request 🚀

---

<div align="center">
  🛡️ Built with Flask & ❤️ by <a href="https://github.com/Krishna-Sharma07" target="_blank">Krishna Sharma</a>
</div>

---

mplete for GitHub presentation?
