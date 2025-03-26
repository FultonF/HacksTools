import os

def show_menu():
    print("\nHacksTools Menu")
    print("1 - Mr. Holmes (Find Subdomains)")
    print("2 - Wireshark (Packet Analyzer)")
    print("3 - Metasploit (Exploit Framework)")
    print("4 - Nikto (Web Scanner)")
    print("5 - Gobuster (Directory Scanner)")
    print("6 - Hydra (Password Cracking Tool)")
    print("7 - Burp Suite (Web Vulnerability Scanner)")
    print("8 - Nmap (Network Mapper)")
    print("9 - LinEnum (Privilege enumeration on Linux)")
    print("10 - Enum4linux (Linux Enumeration Tool)")
    print("11 - Sherlock (Find Social Media Accounts)")
    print("12 - TheHarvester (Information Gathering Tool)")
    print("13 - EvilURL (Malicious URL Detection)")
    print("14 - fsociety (Hacking Toolkit)")
    print("15 - Steghide (Steganography Tool)")
    print("16 - MaskPhish (Phishing Tool)")
    print("17 - Tbomb (SMS Bombing)")
    print("18 - SocialFish (Phishing Tool)")
    print("19 - ALHacking (Automated Hacking Suite)")
    print("20 - Track IP (IP Tracking)")
    print("21 - LinEnum (Privilege enumeration on Linux)")
    print("22 - Recon-ng (Web Recon Tool)")
    print("23 - Hashcat (Password Cracking)")
    print("24 - Sublist3r (Subdomain Enumeration)")
    print("25 - Sn1per (Reconnaissance Scanner)")
    print("26 - Aquatone (Subdomain Visualizer)")
    print("27 - Patator (Password Cracking Tool)")
    print("28 - ZAP Proxy (Web Penetration Testing Tool)")
    print("29 - Social Engineer Toolkit (Phishing Tool)")
    print("30 - Dnsrecon (DNS Information Gathering)")
    print("31 - Fierce (DNS Recon Tool)")
    print("32 - Wpscan (WordPress Vulnerability Scanner)")

def install_tool(choice):
    if choice == 1:
        os.system('git clone https://github.com/ChrisTruncer/Mr-Homes.git')
        os.system('cd Mr-Homes && python3 Mr-Homes.py')
    elif choice == 2:
        os.system('sudo apt install wireshark')
    elif choice == 3:
        os.system('sudo apt install metasploit-framework')
    elif choice == 4:
        os.system('sudo apt install nikto')
    elif choice == 5:
        os.system('sudo apt install gobuster')
    elif choice == 6:
        os.system('sudo apt install hydra')
    elif choice == 7:
        os.system('sudo apt install burpsuite')
    elif choice == 8:
        os.system('sudo apt install nmap')
    elif choice == 9:
        os.system('git clone https://github.com/rebootuser/LinEnum.git')
        os.system('cd LinEnum && chmod +x LinEnum.sh && ./LinEnum.sh')
    elif choice == 10:
        os.system('git clone https://github.com/bugcrowd/enum4linux.git')
        os.system('cd enum4linux && python enum4linux.py')
    elif choice == 11:
        os.system('git clone https://github.com/sherlock-project/sherlock.git')
        os.system('cd sherlock && python3 sherlock.py')
    elif choice == 12:
        os.system('git clone https://github.com/larose/theHarvester.git')
        os.system('cd theHarvester && python3 theHarvester.py')
    elif choice == 13:
        os.system('git clone https://github.com/medusalix/EvilURL.git')
        os.system('cd EvilURL && python3 evilurl.py')
    elif choice == 14:
        os.system('git clone https://github.com/Manisso/fsociety.git')
        os.system('cd fsociety && bash install.sh')
    elif choice == 15:
        os.system('sudo apt install steghide')
    elif choice == 16:
        os.system('git clone https://github.com/Techzindia/MaskPhish.git')
        os.system('cd MaskPhish && python3 maskphish.py')
    elif choice == 17:
        os.system('git clone https://github.com/TheSpeedX/TBomb.git')
        os.system('cd Tbomb && bash TBomb.sh')
    elif choice == 18:
        os.system('git clone https://github.com/xHak9x/socialfish.git')
        os.system('cd socialfish && python3 socialfish.py')
    elif choice == 19:
        os.system('git clone https://github.com/ALHacking/ALHacking.git')
        os.system('cd ALHacking && bash install.sh')
    elif choice == 20:
        os.system('git clone https://github.com/ccoberg/IP-Tracker.git')
        os.system('cd IP-Tracker && python3 tracker.py')
    elif choice == 21:
        os.system('git clone https://github.com/rebootuser/LinEnum.git')
        os.system('cd LinEnum && chmod +x LinEnum.sh && ./LinEnum.sh')
    elif choice == 22:
        os.system('git clone https://github.com/lanmaster53/recon-ng.git')
        os.system('cd recon-ng && python3 recon-ng')
    elif choice == 23:
        os.system('sudo apt install hashcat')
    elif choice == 24:
        os.system('git clone https://github.com/aboul3la/Sublist3r.git')
        os.system('cd Sublist3r && python3 sublist3r.py')
    elif choice == 25:
        os.system('git clone https://github.com/1N3/Sn1per.git')
        os.system('cd Sn1per && bash install.sh')
    elif choice == 26:
        os.system('git clone https://github.com/michenriksen/aquatone.git')
        os.system('cd aquatone && ./aquatone')
    elif choice == 27:
        os.system('git clone https://github.com/jesobreira/patator.git')
        os.system('cd patator && python3 patator.py')
    elif choice == 28:
        os.system('sudo apt install zaproxy')
    elif choice == 29:
        os.system('git clone https://github.com/trustedsec/social-engineer-toolkit.git')
        os.system('cd social-engineer-toolkit && python3 setup.py')
    elif choice == 30:
        os.system('git clone https://github.com/darkoperator/dnsrecon.git')
        os.system('cd dnsrecon && python3 dnsrecon.py')
    elif choice == 31:
        os.system('git clone https://github.com/FierceSecurity/fierce.git')
        os.system('cd fierce && python fierce.py')
    elif choice == 32:
        os.system('git clone https://github.com/wpscanteam/wpscan.git')
        os.system('cd wpscan && ruby wpscan.rb')
    else:
        print("Invalid choice, please try again.")

def main():
    show_menu()
    choice = int(input("Enter the number of the tool you want to install: "))
    install_tool(choice)

if __name__ == "__main__":
    main()
