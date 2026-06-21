## tcp-port-scanner

A simple TCP connect port scanner written in Python.
This was built as a test project while was learning network security fundamentals.

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only. 
Scanning systems you do not own or have explicit written permission to test may 
violate computer misuse laws in your jurisdiction. The author assumes no liability 
for misuse.

## Features

- TCP connect scan across ports 1-999
- Hostname-to-IP resolution
- Reports open ports with scan start time

## Requirements

- Python 3.x
- No external dependencies (standard library only)

## Installation

```bash
git clone https://github.com/Emoytech/tcp-port-scanner.git
cd tcp-port-scanner
```

## Usage

```bash
python3 scanner.py <target>
```

Example (using Nmap's official test host, which explicitly permits scanning):
```bash
python3 scanner.py scanme.nmap.org
```

## How It Works

Uses Python's `socket.connect_ex()` to attempt a TCP handshake on each port. 
A return value of 0 indicates the port accepted the connection (open). 
1-second timeout per port to avoid long hangs on filtered ports.

## Known Limitations

- Sequential scanning — slow on larger port ranges (no threading)
- Fixed port range (1-999), not yet configurable via arguments
- No stealth/SYN scanning, only full TCP connect scans

## Status

Complete / not actively maintained. Built as a learning exercise.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

I learnt this from TCM Security- <a href="https://www.youtube.com/watch?v=3FNYvj2U0HM"> Course Video </a>
