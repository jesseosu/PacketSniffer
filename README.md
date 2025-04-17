# Packet Sniffer & Logger

## Overview
This project is a Python-based network packet sniffer and logger built using the `scapy` library. It captures and logs network traffic, specifically HTTP, HTTPS, and DNS packets. The tool provides detailed information about the domains and IPs visited, and it supports advanced features like reverse DNS resolution, verbose output, and logging to text or CSV files.

## Features
- Capture HTTP, HTTPS, and DNS packets
- Protocol breakdown (HTTP, HTTPS, DNS, etc.)
- Command-line interface with multiple configuration options
- Log results to terminal and optional output file (text/CSV)
- Filter HTTP/HTTPS traffic by ports (80, 443)
- Capture only DNS requests
- Reverse DNS lookup for IP addresses
- Verbose mode for raw packet content display
- Match specific domain names with filters
- Prevent duplicate domain logging

## Requirements
Before running the project, you need to install the required dependencies. The main dependency is `scapy`.

```bash
pip install -r requirements.txt
