# Python Subnet Calculator

A Python-based IPv4 subnet calculator that accepts IP addresses in CIDR notation and calculates important network details.

## Features

- Accepts IPv4 addresses with CIDR notation
- Calculates network address
- Calculates broadcast address
- Identifies subnet mask
- Displays CIDR prefix length
- Calculates total IP addresses
- Calculates usable host count
- Displays first and last usable IP addresses
- Handles invalid and empty input
- Includes automated unit tests

## Technologies Used

- Python
- `ipaddress` (Python standard library)
- `unittest`

## Project Structure

```text
python-subnet-calculator/
├── src/
│   └── subnet_calculator.py
├── tests/
│   ├── test_subnet_calculator.py
│   └── .gitkeep
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.8 or later
- No external dependencies

## How to Run

Clone the repository:

```powershell
git clone https://github.com/ManasaUmashankar/python-subnet-calculator.git
cd python-subnet-calculator
```

Run the calculator:

```powershell
python main.py
```

Enter an IPv4 address with CIDR notation when prompted.

Example:

```text
192.168.1.10/24
```

## Example Results

| Network Detail | Result |
|---|---|
| Network Address | 192.168.1.0 |
| Broadcast Address | 192.168.1.255 |
| Subnet Mask | 255.255.255.0 |
| CIDR Prefix | /24 |
| Total Addresses | 256 |
| Usable Hosts | 254 |
| First Usable IP | 192.168.1.1 |
| Last Usable IP | 192.168.1.254 |

## Run Automated Tests

```powershell
python -m unittest discover -s tests -v
```

## Concepts Practiced

- Python functions and dictionaries
- Exception handling
- Python standard library
- IPv4 addressing
- CIDR notation
- Subnet masks
- Network and broadcast addresses
- Host address calculations
- Unit testing

## Learning Goal

This project is part of my Python and networking foundations journey, focusing on practical networking concepts and their implementation using Python.

# Scope

This project currently supports IPv4 subnet calculations. It is intended for educational and networking practice purposes.