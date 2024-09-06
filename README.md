# Enhanced Port Scanner

## Description

This Python script is an enhanced port scanner with reporting functionality. It performs network port scanning and generates a report detailing the open ports found on the target system.

## Features

- **Multi-threaded Scanning**: Efficiently scans ports using multiple threads to speed up the process.
- **Report Generation**: Creates a detailed report in CSV format listing the open ports.

## Requirements

- Python 3.x
- `argparse` module (included with Python)
- `socket` module (included with Python)
- `threading` module (included with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Enhanced_port_scanner.git
    ```

2. Navigate into the project directory:

    ```bash
    cd Enhanced_port_scanner
    ```

3. Install any necessary packages (if applicable):

    ```bash
    # No additional packages are required for this script
    ```

## Usage

Run the script with the following command:

```bash
python Enhanced_port_scanner.py --start 1 --end 1024 --report scan_report.csv target_ip
