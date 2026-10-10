
# PhishAware — Phishing Awareness Simulator

PhishAware is an educational cybersecurity web application built with
Python and Flask. It helps users learn how to recognize suspicious email
messages and improve their phishing-awareness skills.

## Features

- Professional cybersecurity-themed dashboard
- Fictional email training examples
- Explanations of common phishing warning signs
- Multiple-choice awareness assessment
- Automatic scoring and answer explanations
- Responsive layout for desktop and mobile
- Health-check endpoint
- Automated tests

## Technology Stack

- Python
- Flask
- HTML5
- CSS3
- unittest
- Gunicorn
- Render (deployment)

## Project Structure

```text
phishing-awareness-simulator/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── TESTING_REPORT.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

## Requirements

- Python 3.10 or later
- pip
- A web browser

## Run Locally

Create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

If PowerShell blocks activation, you can run the environment's
Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## Run Automated Tests

```powershell
python -m unittest discover -s tests -v
```

## Health Check

While the application is running, visit:

http://127.0.0.1:5000/health

Expected response:

```json
{"status": "ok"}
```

## Deployment

The application can be deployed as a Python web service on Render.

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
gunicorn app:app
```

## Project Links

- GitHub Repository: ADD_YOUR_REPOSITORY_URL
- Live Website: ADD_YOUR_LIVE_WEBSITE_URL
- Demo Video: ADD_YOUR_VIDEO_URL
- LinkedIn Post: ADD_YOUR_LINKEDIN_POST_URL

Replace these placeholders with your real links after publishing.

## Ethical Use and Limitations

PhishAware is intended for cybersecurity education and awareness.
Its examples are fictional and predefined. It is not a production
email-scanning service and does not determine whether arbitrary
real-world emails are safe.

The application does not send phishing messages or collect user
passwords. Users should verify unexpected requests through trusted
channels and follow their organization's reporting procedures.

## Future Improvements

- Additional training scenarios
- Accessibility improvements
- More detailed assessment reports
- Optional educational progress tracking

## Author

Student Cybersecurity Project
