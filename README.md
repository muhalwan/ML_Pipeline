---

# Flask Prometheus Metrics Exporter

A simple Flask application showcasing the integration of the Prometheus metrics exporter. This application exposes basic performance metrics, which can be easily scraped by a Prometheus instance for monitoring purposes.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run the Application](#run-the-application)
- [Available Endpoints](#available-endpoints)
- [Integration with Prometheus](#integration-with-prometheus)
- [Contributing](#contributing)
- [License](#license)

## Features

- Expose Flask application metrics in Prometheus format.
- Simple `/` endpoint returning a "Hello, World!" message.

## Prerequisites

- Python 3.7+
- pip
- virtualenv (optional, but recommended)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/muhalwan/ML_Pipeline.git flask-prometheus-exporter
cd flask-prometheus-exporter
```

### Setting Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows, use: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app/main.py
```

The application should now be running at `http://0.0.0.0:5000/`.

## Available Endpoints

- `/` - Simple greeting endpoint.
- `/metrics` - Endpoint to retrieve the Prometheus metrics.

## Integration with Prometheus

To integrate with Prometheus:

1. Add the Flask application target in your Prometheus configuration (`prometheus.yml`):

```yaml
scrape_configs:
  - job_name: 'flask-application'
    static_configs:
    - targets: ['your-flask-app-domain-or-ip:5000']
```

2. Reload or restart Prometheus.

## Contributing

Contributions are welcome! Please read our [contribution guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---