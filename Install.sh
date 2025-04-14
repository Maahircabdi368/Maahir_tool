#!/bin/bash

echo "==== MAAHIR TOOL INSTALLER ===="

# Hubi in Python la rakibay
if ! command -v python3 &> /dev/null
then
    echo "Python3 lama helin. Fadlan ku rakib marka hore."
    exit
fi

# Abuurida virtual environment (ikhtiyaari)
# python3 -m venv venv
# source venv/bin/activate

# Rakiba dependencies
echo "[+] Installing required Python libraries..."
pip install colorama requests python-whois pyfiglet s 

echo "[+] Dhammaan libraries waa la rakibay."

# Run tool (ikhtiyaari)
echo "[*] Hadda waxaad bilaabi kartaa tool-ka:"
echo "python3 Maahir.py"
