import os
import subprocess
from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)

def imprimir_herramientas():
    herramientas = [
        "1 - Metasploit Framework (Explotación y Pruebas de Penetración)",
        "2 - Nmap (Escaneo y Mapeo de Redes)",
        "3 - Burp Suite (Pruebas de Seguridad Web)",
        "4 - Sherlock (Identificación de Cuentas en Redes Sociales)",
        "5 - Hydra (Herramienta de Fuerza Bruta)",
        "6 - Sqlmap (Automatización de Inyección SQL)",
        "7 - John the Ripper (Crackeo de Contraseñas)",
        "8 - Wireshark (Analizador de Protocolo de Red)",
        "9 - Aircrack-ng (Crackeo de Wi-Fi)",
        "10 - Nikto (Escáner de Vulnerabilidades en Servidores Web)",
        "11 - Recon-ng (Framework de Reconocimiento Web)",
        "12 - LinEnum (Enumeración de Escalamiento de Privilegios)",
        "13 - Wifite (Crackeo Automático de Redes Inalámbricas)",
        "14 - Mimikatz (Volcado de Credenciales de Windows)",
        "15 - BloodHound (Enumeración de Active Directory)",
        "16 - OWASP ZAP (Pruebas de Seguridad en Aplicaciones Web)",
        "17 - BeEF (Framework de Explotación de Navegadores)",
        "18 - Social Engineering Toolkit (Phishing y Ingeniería Social)",
        "19 - Gobuster (Brute Force de DNS y Directorios)",
        "20 - Sublist3r (Enumeración de Subdominios)",
        "21 - Hashcat (Crackeo de Contraseñas)",
        "22 - TheHarvester (Recolección de Correos Electrónicos y Dominios)",
        "23 - SpiderFoot (Reconocimiento Automático)",
        "24 - Sn1per (Reconocimiento y Enumeración)",
        "25 - Netdiscover (Descubrimiento de Redes)",
        "26 - SSLscan (Escáner de Vulnerabilidades SSL/TLS)",
        "27 - Netcat (Utilidad de Red y Shell Inversa)",
        "28 - Responder (Movimiento Lateral y Suplantación de Red)",
        "29 - LinPEAS (Auditoría de Escalamiento de Privilegios en Linux)",
        "30 - TShark (Captura de Tráfico de Red)",
        "31 - Subjack (Toma de Subdominios)",
        "32 - Msfvenom (Generador de Payloads)",
        "33 - Fsociety (Toolkit Todo en Uno de Hacking)",
        "34 - Steghide (Herramienta de Esteganografía)",
        "35 - Track IP (Rastreador de Ubicación de IP)",
        "36 - Evilurl (Herramienta de Análisis de URLs)",
        "37 - Maskphish (Herramienta de Phishing)",
        "38 - Tbomb (Herramienta de Bombardeo SMS)",
        "39 - Hash-identifier (Identificador de Hashes)",
        "40 - Fuzzbunch (Framework de Explotación)",
        "41 - Dnsrecon (Reconocimiento DNS)",
        "42 - Packetstorm (Repositorio de Herramientas de Seguridad)",
        "43 - Scapy (Herramienta de Creación de Paquetes)",
        "44 - Slowloris (Herramienta de Denegación de Servicio)",
        "45 - Dmitry (Recolección de Información Deepmagic)",
        "46 - Dirbuster (Brute Force de Directorios)",
        "47 - Moxie0 (Ataque SSLStrip de Downgrade HTTPS)",
        "48 - PrivescCheck (Comprobador de Escalamiento de Privilegios)",
        "49 - Ghost Phisher (Phishing y Ataques Wi-Fi)",
        "50 - Snort (Detección y Prevención de Intrusiones)"
    ]
    print(Fore.YELLOW + Style.BRIGHT + "\n====================== Hackstools ======================")
    print(Fore.GREEN + Style.BRIGHT + "¡Bienvenido a la colección definitiva de herramientas de hacking!")
    print(Fore.CYAN + "Selecciona una herramienta para instalar ingresando el número correspondiente:")
    print(Fore.WHITE + "-"*60)
    for herramienta in herramientas:
        print(Fore.MAGENTA + herramienta)
    print(Fore.WHITE + "-"*60)

def instalar_herramienta(numero_herramienta):
    enlaces_herramientas = {
        1: "https://github.com/rapid7/metasploit-framework",
        2: "https://nmap.org",
        3: "https://portswigger.net/burp",
        4: "https://github.com/sherlock-project/sherlock.git",
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
        20: "https://github.com/aboul3la/Sublist3r.git",
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
        32: "https://github.com/g0tmi1k/msfpc.git",
        33: "https://github.com/Manisso/fsociety",
        34: "https://github.com/StefanoScherer/steghide",
        35: "https://github.com/htr-tech/track-ip.git",
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
        46: "https://github.com/maurosoria/dirsearch.git",
        47: "https://github.com/moxie0/sslstrip",
        48: "https://github.com/pentestmonkey/privesccheck",
        49: "https://github.com/evilsocket/ghost-phisher",
        50: "https://github.com/snort3/snort3"
    }

    # Comprobar si la entrada es válida
    if numero_herramienta < 1 or numero_herramienta > 50:
        print(Fore.RED + "Opción inválida. Por favor, selecciona un número válido entre 1 y 50.")
        return

    nombre_herramienta = list(enlaces_herramientas.keys())[numero_herramienta - 1]
    enlace_herramienta = enlaces_herramientas[nombre_herramienta]

    # Clonar o descargar el repositorio desde GitHub
    print(Fore.YELLOW + f"\nDescargando herramienta: {nombre_herramienta}")
    subprocess.run(["git", "clone", enlace_herramienta])

def principal():
    print(Fore.YELLOW + Style.BRIGHT + "\n=================== Hackstools ====================")
    print(Fore.RED + Style.BRIGHT + "¡Bienvenido a Hackstools - El Toolkit Definitivo de Hacking!\n")
    imprimir_herramientas()

    try:
        eleccion_herramienta = int(input(Fore.GREEN + "Ingresa tu elección (1-50): "))
        instalar_herramienta(eleccion_herramienta)
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un número válido.")

if __name__ == "__main__":
    principal()
