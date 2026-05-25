# Temperature Monitoring System

A temperature monitoring system built with a **Raspberry Pi 4** and **Sense HAT** that:

- Reads ambient temperature in real time
- Displays status messages on the Sense HAT LED matrix
- Classifies temperature as **HOT**, **COLD**, or **FINE**
- Sends temperature data to the **Blynk IoT App**
- Allows remote monitoring through a mobile device

---

## Hardware Requirements

- Raspberry Pi 4
- Sense HAT
- MicroSD card with Raspberry Pi OS
- Power supply
- Internet connection (for Blynk)

---

## Software Requirements

- Raspberry Pi OS
- Python 3
- Sense HAT Python library
- Blynk library

---

## Installation

### 1. Update Raspberry Pi
sudo apt-get update

### 2. Install Sense HAT
sudo apt-get install sense-hat

### 3. Reboot
sudo reboot

## Running LED Temperature Monitor 
python temp-monitor.py

## Running Blynk App Temperature Monitor
