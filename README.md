# API Health Monitor

A production-ready API Health Monitoring System built with Python for DevOps, SRE, and Cloud Engineering use cases.

This project continuously monitors multiple APIs, measures response times, validates HTTP status codes, generates logs and reports, and can be integrated into CI/CD pipelines using GitHub Actions.

---

## Project Goals

The primary objective of this project is to:

- Monitor public and private APIs
- Track API availability
- Measure API response times
- Generate structured logs
- Create health reports
- Support CI/CD automation
- Demonstrate DevOps best practices

---

## Features

### Current Features

✅ Multi-API Monitoring

✅ Config-Driven Design

✅ Response Time Tracking

✅ HTTP Status Code Validation

✅ Structured Logging

✅ JSON Report Generation

✅ Error Handling

✅ GitHub Version Control

---

## Planned Features

### Monitoring

- API Availability Tracking
- Historical Monitoring Reports
- API SLA Tracking

### Alerting

- Slack Notifications
- Email Alerts
- Microsoft Teams Notifications

### Reporting

- HTML Dashboard
- Health Trend Analysis
- Daily Health Summary

### DevOps Integration

- GitHub Actions CI/CD
- Docker Support
- Kubernetes Deployment
- Prometheus Metrics
- Grafana Dashboard

---

## Project Structure

```text
api-health-monitor/
│
├── src/
│   ├── monitor.py
│   ├── logger.py
│   ├── config_loader.py
│   └── report_generator.py
│
├── config/
│   └── apis.json
│
├── logs/
│   └── app.log
│
├── reports/
│   └── report.json
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── monitor.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.11+
- Requests
- JSON
- Logging
- Git
- GitHub
- GitHub Actions

Future:

- Docker
- Kubernetes
- Prometheus
- Grafana
- Slack API

---

## Configuration

API endpoints are stored in:

```text
config/apis.json
```

Example:

```json
{
  "apis": [
    {
      "name": "GitHub",
      "url": "https://api.github.com"
    },
    {
      "name": "Google",
      "url": "https://www.google.com"
    }
  ]
}
```

This allows APIs to be added or removed without changing the application code.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Mahaboob3247/api-health-monitor.git

cd api-health-monitor
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Execute:

```bash
python src/monitor.py
```

Example Output:

```text
API HEALTH MONITOR

✅ GitHub 200 0.134s

✅ Google 200 0.221s

✅ JSONPlaceholder 200 0.113s
```

---

## Logging

The application automatically creates log files.

Location:

```text
logs/app.log
```

Example:

```log
2026-10-03 10:00:01 INFO GitHub Status=200 ResponseTime=0.134

2026-10-03 10:00:02 INFO Google Status=200 ResponseTime=0.211
```

Logs are useful for:

- Monitoring
- Troubleshooting
- Incident Analysis
- Audit Tracking

---

## Report Generation

After every execution a report is generated.

Location:

```text
reports/report.json
```

Example:

```json
[
  {
    "name": "GitHub",
    "status": 200,
    "response_time": 0.134
  }
]
```

Reports can later be integrated with:

- Grafana
- ELK Stack
- Splunk
- Prometheus

---

## CI/CD Integration

Planned GitHub Actions workflow:

```yaml
on:
  schedule:
    - cron: "0 * * * *"
```

This will automatically:

- Run API health checks
- Generate reports
- Store execution logs
- Alert on failures

---

## Potential Use Cases

- API Monitoring
- Application Monitoring
- Infrastructure Validation
- Deployment Verification
- Health Checks
- Site Reliability Engineering
- DevOps Automation

---

## Future Roadmap

### Version 1.0

- Multi API Health Checks
- Logging
- JSON Reports

### Version 2.0

- HTML Dashboard
- Report Visualization

### Version 3.0

- Slack Alerts
- Email Notifications

### Version 4.0

- Docker Support
- Containerized Deployment

### Version 5.0

- Kubernetes Deployment
- Helm Charts

### Version 6.0

- Prometheus Metrics
- Grafana Dashboards

---

## Sample DevOps Workflow

```text
Developer Pushes Code
         │
         ▼
GitHub Actions Runs
         │
         ▼
API Health Checks Execute
         │
         ▼
Logs Generated
         │
         ▼
Reports Generated
         │
         ▼
Alerts Sent (Future Feature)
```

---

## Why This Project?

This project demonstrates practical DevOps skills including:

- Python Automation
- Monitoring
- Logging
- CI/CD
- Configuration Management
- Reporting
- Observability
- Infrastructure Monitoring

---

## Author

Shaik Mahboob Basha
GitHub: https://github.com/Mahaboob3247

---

## License

MIT License