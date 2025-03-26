import os

def install_tool(option):
    tools = {
        "1": "git clone https://github.com/FultonF/HacksTools.git && cd HacksTools && chmod +x install.sh && ./install.sh",  # Custom hacking tools repository
        "2": "sudo apt install -y wireshark",  # Network traffic analysis
        "3": "sudo apt install -y nmap",  # Network scanning and open ports detection
        "4": "sudo apt install -y metasploit-framework",  # Exploitation framework
        "5": "sudo apt install -y john",  # Password cracking using dictionary and brute force attacks
        "6": "sudo apt install -y sqlmap",  # Automated SQL injection testing
        "7": "sudo apt install -y aircrack-ng",  # WiFi network security testing
        "8": "sudo apt install -y hydra",  # Brute-force attacks on network authentication
        "9": "sudo apt install -y gobuster",  # Directory and subdomain brute-forcing
        "10": "sudo apt install -y nikto",  # Web server vulnerability scanning
        "11": "sudo apt install -y hashcat",  # Advanced hash cracking using GPU
        "12": "git clone https://github.com/The-Art-of-Hacking/h4cker.git && cd h4cker",  # Collection of hacking resources
        "13": "git clone https://github.com/rebootuser/LinEnum.git && cd LinEnum",  # Privilege enumeration in Linux
        "14": "sudo apt install -y theharvester",  # OSINT email and data gathering
        "15": "pip install shodan",  # Shodan client for searching devices on the internet
        "16": "sudo apt install -y exploitdb",  # Database of exploits and vulnerabilities
        "17": "sudo apt install -y set",  # Social Engineering Toolkit for phishing and social engineering attacks
        "18": "sudo apt install -y ettercap-graphical",  # Sniffing and MITM network attacks
        "19": "sudo apt install -y bettercap",  # Advanced network security testing tool
        "20": "sudo apt install -y medusa",  # Brute-force attacks against multiple protocols
        "21": "sudo apt install -y crunch",  # Password dictionary generator for brute-force attacks
        "22": "git clone https://github.com/AlessandroZ/BeRoot.git && cd BeRoot",  # Privilege escalation tool for Linux
        "23": "wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 && chmod +x pspy64",  # Process monitoring tool for Linux
        "24": "git clone https://github.com/trustedsec/social-engineer-toolkit.git && cd social-engineer-toolkit",  # Social engineering toolkit
        "25": "git clone https://github.com/byt3bl33d3r/evilurl.git && cd evilurl",  # Phishing URL generator
        "26": "git clone https://github.com/Manoj-Kumar-01/Tbomb.git && cd Tbomb",  # SMS Bombing tool
        "27": "git clone https://github.com/Und3rf10w/kali-tools.git && cd kali-tools",  # Collection of useful Kali tools
        "28": "git clone https://github.com/3xploitX/trackip.git && cd trackip",  # IP tracking and geolocation
        "29": "git clone https://github.com/Pr0x10/FSociety.git && cd FSociety",  # Hacking tools collection
        "30": "git clone https://github.com/zd3d0x/MaskPhish.git && cd MaskPhish",  # Phishing tool with masking
        "31": "git clone https://github.com/AHacking/ALhacking.git && cd ALhacking",  # Linux post-exploitation tool
        "32": "git clone https://github.com/Pr0x10/SocialFish.git && cd SocialFish",  # Social engineering phishing tool
        "33": "git clone https://github.com/stealthcopter/steghide.git && cd steghide",  # Steganography tool for hiding data in images
    }

    if option in tools:
        print(f"Installing tool {option}...")
        os.system(tools[option])
    else:
        print("Invalid option.")

def main():
    while True:
        print("\nSelect a tool to install:")
        print("1 - HacksTools (Custom hacking tools repository)")
        print("2 - Wireshark (Network traffic analysis)")
        print("3 - Nmap (Network scanning and open ports detection)")
        print("4 - Metasploit Framework (Exploitation framework)")
        print("5 - John the Ripper (Password cracking tool)")
        print("6 - SQLmap (Automated SQL injection testing)")
        print("7 - Aircrack-ng (WiFi network security testing)")
        print("8 - Hydra (Brute-force attacks on network authentication)")
        print("9 - Gobuster (Brute-force directory and subdomain discovery)")
        print("10 - Nikto (Web server vulnerability scanning)")
        print("11 - Hashcat (Advanced hash cracking using GPU)")
        print("12 - H4cker Toolkit (Collection of hacking resources)")
        print("13 - LinEnum (Privilege enumeration
