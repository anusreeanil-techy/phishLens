# phishLens
Live Website:https://phishlens-1-gfro.onrender.com
🛡️ PhishLens – Phishing URL Detection System

PhishLens is a beginner-friendly web application designed to check website URLs for suspicious signs that may indicate phishing.

📌 About the Project

Phishing is a type of cyberattack in which attackers try to trick users into sharing sensitive information through deceptive websites.

PhishLens checks a submitted URL for basic suspicious indicators and displays a warning when certain rules are triggered.

This project was developed to learn the basics of cybersecurity, Python, Flask, and web application development.

🚀 Features

- Check a website URL for suspicious signs
- Detect URLs that do not use HTTPS
- Identify URLs containing the "@" symbol
- Detect internationalized domain names beginning with "xn--"
- Flag unusually long URLs
- Display warning messages for detected indicators
- Simple and user-friendly interface
- Web-based URL checking

🛠️ Technologies Used

- Python – Application logic
- Flask – Web framework
- HTML5 – Web page structure
- CSS3 – Website styling
- Gunicorn – Web application server
- Render – Deployment and hosting
- GitHub – Source code hosting

📂 Project Structure

PhishLens/
├── templates/
│   └── index.html
├── app.py
├── index.html
├── style.css
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How It Works

1. Open the PhishLens website.
2. Enter a website URL in the input box.
3. Click the Check URL button.
4. PhishLens checks the URL against predefined rules.
5. The website displays any suspicious indicators detected.

🌐 Live Demo

Live Website:
"Open PhishLens" https://phishlens-1-gfro.onrender.com

Replace the placeholder above with your actual Render website URL.

🧪 Example Result

Input: "http://example.com"

Possible warning: URL does not use HTTPS.

The result depends on the rules implemented in the application.

⚠️ Limitations

- This is a basic rule-based detection system.
- HTTPS does not guarantee that a website is safe.
- A suspicious indicator does not prove that a website is malicious.
- The application does not guarantee detection of every phishing website.

Always verify website addresses carefully before entering personal or financial information.

🔮 Future Improvements

- Integrate trusted phishing URL threat-intelligence sources
- Add more URL analysis rules
- Improve detection accuracy
- Add URL checking history with appropriate privacy controls
- Improve the user interface

👩‍💻 Author

Developed as a beginner cybersecurity project to explore phishing URL detection and web application development.

---

PhishLens – Learn, Detect, and Stay Aware.
