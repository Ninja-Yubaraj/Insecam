# [◉°] Insecam

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?logo=github)](#-contributing)

Access Insecure Security Cameras in 20+ countries.

> ⚠️ **Disclaimer**: This project is for **educational purposes only**. Accessing insecure devices without permission may be **illegal**. The author does not take responsibility for misuse.


## ✨ Features
- 🌍 Access **Realtime** Security Footage.
- 🛡️ **Random User-Agent rotation** to avoid blocking  
-  Error handling for network issues and invalid inputs  


##  Installation

```bash
git clone https://github.com/Ninja-Yubaraj/Insecam.git
cd Insecam
````

### Recommended: Virtual Environment Setup

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install requests
```

## 🚀 Usage

Run without arguments to list available countries:

```bash
python Insecam.py
```

Fetch cameras for a specific country (e.g., US):

```bash
python Insecam.py -C US
```

Quiet mode (only IPs, good for scripts and piping):

```bash
python Insecam.py -C US -q
```

Help menu:

```bash
python Insecam.py -h
```

## 📜 Output

Example output for `python Insecam.py -C US`:

```
 ___                                    
|_ _|_ __  ___  ___  ___ __ _ _ __ ___  
 | || '_ \/ __|/ _ \/ __/ _` | '_ ` _ \ 
 | || | | \__ \  __/ (_| (_| | | | | | |
|___|_| |_|___/\___|\___\__,_|_| |_| |_|

Access Insecure Security Cameras in 20+ countries.

    Author: Ninja-Yubaraj
    Github: https://github.com/Ninja-Yubaraj/Insecam

Found 42 cameras in United States:

http://123.45.67.89:8080
http://98.76.54.32:81
http://11.22.33.44:8081
...
```

Quiet mode output (`-q`):

```
http://123.45.67.89:8080
http://98.76.54.32:81
http://11.22.33.44:8081
...
```

---

## 🤝 Contributing

Pull requests & suggestions welcome! Feel free to fork and add: 💡

1. Location based Geographical map.
2. Comma separated multi countrycode support.
3. ``-C --all`` option for country codes.

## Author
Made with \:heart: by [Ninja-Yubaraj](https://github.com/Ninja-Yubaraj)


⭐ If you like this project, give it a star on GitHub!
