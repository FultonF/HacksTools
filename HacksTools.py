import os
import subprocess

def print_tools():
    tools = [
        "1 - Metasploit Framework (Exploitation & Penetration Testing)",
        "2 - Nmap (Network Scanning & Mapping)",
        "3 - Burp Suite (Web Security Testing)",
        "4 - Gobuster (Directory & Subdomain Bruteforce)",
        "5 - Hydra (Brute Force Attack Tool)",
        "6 - Sqlmap (SQL Injection Automation)",
        "7 - John the Ripper (Password Cracking)",
        "8 - Wireshark (Network Protocol Analyzer)",
        "9 - Aircrack-ng (Wi-Fi Cracking)",
        "10 - Nikto (Web Server Vulnerability Scanner)",
        "11 - Recon-ng (Web Reconnaissance Framework)",
        "12 - LinEnum (Privilege Escalation Enumeration)",
        "13 - Wifite (Automated Wireless Cracking)",
        "14 - Mimikatz (Windows Credentials Dumping)",
        "15 - BloodHound (Active Directory Enumeration)",
        "16 - OWASP ZAP (Web Application Security Testing)",
        "17 - BeEF (Browser Exploitation Framework)",
        "18 - Social Engineering Toolkit (Phishing & Social Engineering)",
        "19 - Gobuster (DNS & Directory Bruteforce)",
        "20 - Sublist3r (Subdomain Enumeration)",
        "21 - Hashcat (Password Cracking)",
        "22 - TheHarvester (Email & Domain Harvesting)",
        "23 - SpiderFoot (Automated Reconnaissance)",
        "24 - Sn1per (Reconnaissance & Enumeration)",
        "25 - Netdiscover (Network Discovery)",
        "26 - SSLscan (SSL/TLS Vulnerability Scanner)",
        "27 - Netcat (Network Utility & Reverse Shell)",
        "28 - Responder (Lateral Movement & Network Spoofing)",
        "29 - LinPEAS (Linux Privilege Escalation Audit)",
        "30 - TShark (Network Traffic Capture)",
        "31 - Subjack (Subdomain Takeover)",
        "32 - Msfvenom (Payload Generator)",
        "33 - Fsociety (All-in-one Hacking Toolkit)",
        "34 - Steghide (Steganography Tool)",
        "35 - Track IP (IP Location Tracker)",
        "36 - Evilurl (URL Analysis Tool)",
        "37 - Maskphish (Phishing Tool)",
        "38 - Tbomb (SMS Bombing Tool)",
        "39 - Hash-identifier (Identify Hashes)",
        "40 - Fuzzbunch (Exploitation Framework)",
        "41 - Dnsrecon (DNS Reconnaissance)",
        "42 - Packetstorm (Security Tools Repository)",
        "43 - Scapy (Packet Crafting Tool)",
        "44 - Slowloris (Denial of Service Tool)",
        "45 - Dmitry (Deepmagic Information Gathering)",
        "46 - Dirbuster (Directory Brute Force)",
        "47 - Moxie0 (SSLStrip HTTPS Downgrade Attack)",
        "48 - PrivescCheck (Privilege Escalation Checker)",
        "49 - Ghost Phisher (Wi-Fi Phishing & Attacks)",
        "50 - Snort (Intrusion Detection & Prevention)"
    ]
    for tool in tools:
        print(tool)

def install_tool(tool_number):
    tool_links = {
        1: "https://github.com/rapid7/metasploit-framework",
        2: "https://nmap.org",
        3: "https://portswigger.net/burp",
        4: "https://github.com/OJ/gobuster",
        5: "https://github.com/vanhauser-thc/thc-hydra",
        6: "https://github.com/sqlmapproject/sqlmap",
        7: "https://github.com/magnumripper/JohnTheRipper",
        8: "https://www.wireshark.org",
        9: "https://github.com/aircrack-ng/aircrack-ng",
        10: "https://github.com/sullo/nikto",
        11: "https://github.com/lanmaster53/recon-ng",
        12: "https://github.com/rebootuser/LinEnum",
        13: "https://github.com/derv82/wifite",
        14: "https://github.com/gentilkiwi/mimikatz",
        15: "https://github.com/BloodHoundAD/BloodHound",
        16: "https://github.com/zaproxy/zaproxy",
        17: "https://github.com/BeEF-Project/beef",
        18: "https://github.com/trustedsec/social-engineer-toolkit",
        19: "https://github.com/OJ/gobuster",
        20: "https://github.com/aboul3la/Sublist3r",
        21: "https://github.com/hashcat/hashcat",
        22: "https://github.com/larose/theHarvester",
        23: "https://github.com/smicallef/spiderfoot",
        24: "https://github.com/1N3/Sn1per",
        25: "https://github.com/MattyBaker/netdiscover",
        26: "https://github.com/rbsec/sslscan",
        27: "https://github.com/diegocr/Netcat",
        28: "https://github.com/SpiderLabs/Responder",
        29: "https://github.com/carlospolop/PEASS-ng",
        30: "https://github.com/mjkvaak/tshark",
        31: "https://github.com/AdamBorder/Subjack",
        32: "https://github.com/rapid7/metasploit-framework",
        33: "https://github.com/Manisso/fsociety",
        34: "https://github.com/StefanoScherer/steghide",
        35: "https://github.com/cyberboysumanjay/Track-IP",
        36: "https://github.com/JohnHammond/EVILURL",
        37: "https://github.com/Techzindia/MaskPhish",
        38: "https://github.com/TheSpeedX/TBomb",
        39: "https://github.com/blackploit/hash-identifier",
        40: "https://github.com/mattermost/fuzzbunch",
        41: "https://github.com/darkoperator/dnsrecon",
        42: "https://packetstormsecurity.com",
        43: "https://github.com/secdev/scapy",
        44: "https://github.com/gkbrk/slowloris",
        45: "https://github.com/jaymoulin/dmitry",
        46: "https://github.com/digitarald/dirbuster",
        47: "https://github.com/moxie0/sslstrip",
        48: "https://github.com/pentestmonkey/privesccheck",
        49: "https://github.com/evilsocket/ghost-phisher",
        50: "https://github.com/snort3/snort3"
    }

    # Check if the input is valid
    if tool_number < 1 or tool_number > 50:
        print("Invalid option.")
        return

    tool_name = list(tool_links.keys())[tool_number - 1]
    tool_url = tool_links[tool_name]

    # Clone or download the repository from GitHub
    print(f"Downloading tool: {tool_name}")
    subprocess.run(["git", "clone", tool_url])

def main():
    print("Welcome to HacksTools!")
    print("Select a tool to install by entering the corresponding number:")
    print_tools()
    
    # Get the user's choice
    tool_choice = int(input("Enter your choice: "))
    
    install_tool(tool_choice)

if __name__ == "__main__":
    main()
