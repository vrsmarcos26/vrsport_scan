import socket
import sys

def scantcp(host, port, service="null", status="null", protocol="TCP/IP"):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP
        client.settimeout(0.5)  # Tempo de 0.5 s

        code = client.connect_ex((host, int(port)))  # Teste de conexão

        if code == 0:
            status = "open"
            # Caso queira que retorne somente resultado positivo
            # return print(f"{port:<12} {status:<12} {service:<70} {protocol}")
        else:
            status = "close"
        

        # Ajuste na formatação para alinhar as colunas
        # Caso queira que retorne resultado negativo
        '''print(f"{port:<12} {status:<12} {service:<70} {protocol}")
    except Exception as error:
        print(f"Erro {error} encontrado...")'''

    finally:
        client.close()

def scanudp(host, port, status="null", service="Not Identified", protocol="UDP"):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(1)

        client.sendto(b"", (host, int(port)))

        try:
            client.recvfrom(1024)
            status = "open"
        except socket.timeout:
            status = "closed"

        # Ajuste na formatação para alinhar as colunas
        print(f"{port:<12} {status:<12} {service:<70} {protocol}")

    except Exception as error:
        print(f"Erro encontrado {error}...")

    finally:
        client.close()

def obter_servico_por_porta(porta):
    switch = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH (Secure Shell)",
        23: "Telnet",
        25: "SMTP (Simple Mail Transfer Protocol)",
        53: "DNS (Domain Name System)",
        67: "DHCP (Dynamic Host Configuration Protocol - Server)",
        68: "DHCP (Dynamic Host Configuration Protocol - Client)",
        80: "HTTP (HyperText Transfer Protocol)",
        443: "HTTPS (HTTP Secure)",
        110: "POP3 (Post Office Protocol 3)",
        143: "IMAP (Internet Message Access Protocol)",
        220: "IMAP3 (Internet Message Access Protocol v3)",
        3389: "RDP (Remote Desktop Protocol)",
        3306: "MySQL",
        5432: "PostgreSQL",
        5900: "VNC (Virtual Network Computing)",
        8080: "HTTP Alternate (commonly used for proxies)",
        8443: "HTTPS Alternate",
        161: "SNMP (Simple Network Management Protocol)",
        162: "SNMP Trap",
        514: "Syslog",
        119: "NNTP (Network News Transfer Protocol)",
        1433: "MS SQL Server",
        1434: "MS SQL Server Resolution Protocol",
        389: "LDAP (Lightweight Directory Access Protocol)",
        636: "LDAPS (LDAP over SSL)",
        4444: "Blaster Worm (Remote Command Execution)",
        1521: "Oracle Database Listener",
        5000: "UPnP (Universal Plug and Play)",
        5222: "XMPP (Extensible Messaging and Presence Protocol)",
        5672: "AMQP (Advanced Message Queuing Protocol)",
        6379: "Redis",
        9200: "Elasticsearch",
        9300: "Elasticsearch Cluster",
        27017: "MongoDB",
        27018: "MongoDB Secondary",
        27019: "MongoDB Config Server",
        500: "ISAKMP (Internet Security Association and Key Management Protocol)",
        4500: "IPSec NAT-T (Network Address Translation Traversal)"
    }

    return switch.get(porta, "Not Identified")

def parse_ports(port_arg):
    ports = []
    if "-" in port_arg:
        start_port, end_port = port_arg.split("-")
        start_port, end_port = int(start_port), int(end_port)
        ports = list(range(start_port, end_port + 1))
    else:
        ports = [int(port) for port in port_arg.split(",")]
    return ports

def obter_ip_por_dominio(dom):
    try:
        ip = socket.gethostbyname(dom)
        return ip
    except socket.gaierror:
        return "IP não encontrado"

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].upper() == "-H":
        print("""
=============================================================
* Utilização:                                               *
*   python vrsport.py <domínio/IP> <porta(s)>               *
*                                                           *
* Exemplo 1 (varredura de portas TCP padrão):               *
*   python vrsport.py 192.168.0.1 80,443                    *
*                                                           *
* Exemplo 2 (varredura de portas UDP padrão):               *
*   python vrsport.py 192.168.0.1 80,443 -UDP               *
*                                                           *
* Exemplo 3 (varredura de intervalo de portas TCP):         *
*   python vrsport.py 192.168.0.1 20-25                     *
*                                                           *
* Exemplo 4 (varredura de um host em todas as portas TCP    *
* padrão):                                                  *
*   python vrsport.py 192.168.0.1                           *
=============================================================
""")

    elif len(sys.argv) >= 2:
        host_arg = sys.argv[1]
        ip_correspondente = obter_ip_por_dominio(host_arg)
        print(f"DOMAIN/IP: {host_arg} ({ip_correspondente})\n")
        # Ajuste no cabeçalho para alinhar as colunas
        print(f"{'PORT-':<12} {'-STATUS-':<12} {'-SERVICE-':<70} {'-PROTOCOL'}")

        if len(sys.argv) >= 3 and sys.argv[2].upper() == "-UDP":
            ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 443, 110, 143, 220, 3389, 3306, 5432, 5900, 8080, 8443, 161, 162, 514, 119, 1433, 1434, 389, 636, 4444, 1521, 
            5000, 5222, 5672, 6379, 9200, 9300, 27017, 27018, 27019, 500, 4500]

            for port in ports:
                scanudp(host_arg, port, status="null")

        elif len(sys.argv) >= 4 and sys.argv[3].upper() == "-UDP":
            port_arg = sys.argv[2]
            ports = parse_ports(port_arg)

            for port in ports:
                scanudp(host_arg, port, status="null")

        elif len(sys.argv) >= 3:
            port_arg = sys.argv[2]
            ports = parse_ports(port_arg)

            for port in ports:
                scantcp(host_arg, port, service=obter_servico_por_porta(port), status="null")
        else:
            ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 443, 110, 143, 220, 3389, 3306, 5432, 5900, 8080, 8443, 161, 162, 514, 119, 1433, 1434, 389, 636, 4444, 1521, 
            5000, 5222, 5672, 6379, 9200, 9300, 27017, 27018, 27019, 500, 4500]

            for port in ports:
                scantcp(host_arg, port, service=obter_servico_por_porta(port), status="null")

    else:
        print("""
***************************************************************
*           Bem-vindo ao Scanner de Portas TCP/UDP!         *
*                                                           *
* Este programa permite realizar uma varredura em portas    *
* de um determinado host ou IP para verificar o status      *
* das portas, identificando se estão abertas ou fechadas,   *
* além de informar qual serviço está associado a cada       *
* porta.                                                    *
*                                                           *
* Utilização:                                               *
*   python vrsport.py <domínio/IP> <porta(s)>               *
*                                                           *
* Exemplo 1 (varredura de portas TCP padrão):               *
*   python vrsport.py 192.168.0.1 80,443                    *
*                                                           *
* Exemplo 2 (varredura de portas UDP padrão):               *
*   python vrsport.py 192.168.0.1 80,443 -UDP               *
*                                                           *
* Exemplo 3 (varredura de intervalo de portas TCP):         *
*   python vrsport.py 192.168.0.1 20-25                     *
*                                                           *
* Exemplo 4 (varredura de um host em todas as portas TCP    *
* padrão):                                                  *
*   python vrsport.py 192.168.0.1                           *
*                                                           *
* Desenvolvido por: gh0st                                   *
* Version 1.0                                               *
***************************************************************
""")
