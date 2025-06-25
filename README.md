<div align="center">
  <h1>
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" alt="Lupa" width="45" height="45" />
    VRS Port Scan
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Shield.png" alt="Escudo" width="45" height="45" />
  </h1>
</div>

<p align="center">
  <img alt="Linguagem Principal" src="https://img.shields.io/github/languages/top/vrsmarcos26/vrsport_scan?style=for-the-badge&color=3776AB">
  <img alt="Licença" src="https://img.shields.io/github/license/vrsmarcos26/vrsport_scan?style=for-the-badge&color=blue">
  <img alt="Último Commit" src="https://img.shields.io/github/last-commit/vrsmarcos26/vrsport_scan?style=for-the-badge&color=green">
</p>

<p align="center">
  Um scanner de portas TCP/UDP simples e de linha de comando, desenvolvido em Python para fins educacionais e de estudo em segurança de redes.
</p>

<p align="center">
  <a href="#-aviso-de-uso-ético">Aviso</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-usar">Como Usar</a> •
  <a href="#-exemplos-de-uso">Exemplos</a> •
  <a href="#-licença">Licença</a> •
  <a href="#-autor">Autor</a>
</p>

---

### ⚠️ Aviso de Uso Ético

**Este projeto foi criado para fins estritamente educacionais.** O objetivo é aprender sobre programação de sockets e protocolos de rede. A varredura de portas em redes ou sistemas sem autorização explícita é ilegal e antiética. Utilize esta ferramenta apenas em seus próprios sistemas ou em ambientes onde você tenha permissão para testar.

---

### 🚀 Funcionalidades

-   **Varredura TCP & UDP:** Testa a conectividade em portas TCP e, opcionalmente, em portas UDP.
-   **Identificação de Serviços:** Mapeia portas conhecidas para seus serviços correspondentes (ex: porta 80 para HTTP).
-   **Flexibilidade de Alvos:** Aceita uma lista de portas (`80,443,8080`) ou um intervalo (`20-1024`).
-   **Saída Clara:** Exibe uma tabela organizada com o status de cada porta, serviço e protocolo.
-   **Varredura Padrão:** Se nenhuma porta for especificada, realiza a varredura em uma lista de portas comuns.

---

### 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
</p>

-   A biblioteca nativa `socket` do Python foi utilizada para toda a comunicação de rede.

---

### ⚙️ Como Usar

Você precisará ter o **Python 3** instalado em sua máquina.

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/vrsmarcos26/vrsport_scan.git](https://github.com/vrsmarcos26/vrsport_scan.git)
    cd vrsport_scan
    ```

2.  **Sintaxe de Execução**
    Execute o script diretamente do seu terminal, seguindo a sintaxe abaixo:

    ```bash
    python vrsport.py <domínio/IP> [porta(s)] [opções]
    ```

    **Parâmetros:**
    -   `domínio/IP`: **(Obrigatório)** O host alvo que você deseja escanear.
    -   `porta(s)`: **(Opcional)** Portas específicas. Pode ser:
        -   Uma lista separada por vírgulas: `80,443,8080`
        -   Um intervalo: `20-25`
        -   Se omitido, portas padrão serão usadas.
    -   `opções`:
        -   `-UDP`: Realiza a varredura usando o protocolo UDP em vez de TCP.

---

### 👨‍💻 Exemplos de Uso

**1. Varredura de portas TCP específicas**
```bash
python vrsport.py scanme.nmap.org 80,443
```

**2. Varredura de um intervalo de portas TCP**
```bash
python vrsport.py scanme.nmap.org 20-25
```

3. Varredura de portas UDP
```bash
python vrsport.py scanme.nmap.org 53,161,162 -UDP
```

4. Varredura nas portas TCP padrão (se nenhuma for especificada)
```bash
python vrsport.py scanme.nmap.org
```

## 💡 Exemplo de Saída
A saída será formatada em uma tabela clara no terminal:
```
PORT-   -STATUS-     -SERVICE-                         -PROTOCOL
20      closed       FTP Data Transfer                 TCP/IP
21      closed       FTP Control                       TCP/IP
22      open         SSH (Secure Shell)                TCP/IP
80      open         HTTP (HyperText Transfer Protocol)TCP/IP
443     open         HTTPS (HTTP Secure)               TCP/IP
```
---

### 🤝 Como Contribuir
Contribuições são bem-vindas! Se você tiver ideias para novas funcionalidades, melhorias ou correções de bugs, sinta-se à vontade para abrir uma Issue para discussão ou enviar um Pull Request.

---

### 📝 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

<hr>

<p align="center">
  Desenvolvido por <b>vrsmarcos26</b>
</p>
