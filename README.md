# SECR3253-17-Neteam-Hybrid-Network-Automation

A Python-based hybrid network automation tool combining Cisco NETCONF
device configuration with Linux host monitoring, run through a single
interactive menu and packaged with Docker.

## Project Overview

This project was built by a team of 5 for SECR3253. It automates common
network engineering and system administration tasks:

- Configuring Cisco IOS-XE devices over NETCONF (IP addressing, interface
  descriptions, local users, MOTD banners, static routes)
- Retrieving live device configuration/state over NETCONF
- Monitoring the health of the Linux host running the tool
- Generating a session report summarizing actions taken

## Project Structure
├── main.py                  # Entry point / main menu (Member 5)
├── netconf_config.py        # Shared NETCONF device connection settings
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── member1/                 # NETCONF: IP Configuration, Interface Description
│   └── member1_netconf.py
├── member2/                 # NETCONF: User Creation, Banner Configuration
│   └── user_banner.py
├── member3/                 # NETCONF: Static Routes, Device Info Retrieval
│   └── routing_info.py
├── member4/                 # Linux Monitoring: hostname, date/time, CPU,
│   └── linux_monitor.py     # memory, disk, users, processes
└── member5/                 # Integration, Docker, Report Generator
└── report_generator.py

## Requirements

- Python 3.11+
- Access to a NETCONF-capable device (tested against a CSR1000v in the
  devasc-labvm environment, port 830)
- Docker (optional, for containerized usage)

Python dependencies are listed in `requirements.txt`:
ncclient
xmltodict

## Installation

```bash
git clone https://github.com/<your-org>/SECR3253-17-Neteam-Hybrid-Network-Automation.git
cd SECR3253-17-Neteam-Hybrid-Network-Automation
pip install -r requirements.txt
```

Update the device credentials in `netconf_config.py` to match your lab
environment before running.

## How to Run

```bash
python3 main.py
```

Then choose an option from the menu:

NETCONF Configuration (IP / Interface Description)
User & Banner Configuration
Routing & Device Information
Linux Monitoring
Generate Report
Exit


## Docker Usage

Build and run the whole tool inside a container:

```bash
docker compose build
docker compose run --rm app
```

`docker-compose.yml` mounts the app with an interactive TTY so the menu's
`input()` prompts work as expected inside the container.

## Features

- Interactive, menu-driven CLI covering NETCONF config, retrieval, and
  Linux host monitoring
- Session report generation summarizing all actions taken in a run
- Dockerized for consistent setup across machines
- Modular structure — each member's work lives in its own folder

## Team Members

| Member | Name | Module |
|---|---|---|
| 1 | NIK DANISH ADAM BIN FAIRUS | NETCONF Configuration (IP Configuration, Interface Description) |
| 2 | MUHAMMAD FIRDAUS ALIF BIN ROSLAN | User & Banner Module (User Creation, Banner Configuration) |
| 3 | AHMAD ARIFF AZAHARI BIN MOHD AZHAR | Routing & Information Retrieval (Static Route, Device Information Retrieval) |
| 4 | LUQMAN HAKIMI BIN MHD ABDUL ADZIM | Linux Monitoring (Hostname, Date & Time, CPU, Memory, Disk, Users, Processes) |
| 5 | MUHAMMAD ALIF BIN AZMAN | Integration & Docker (Main Menu, Docker, Report Generator, GitHub Management, README) |
