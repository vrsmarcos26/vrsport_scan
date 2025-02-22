# vrsport_scan

Este é um simples scanner de portas desenvolvido em Python para testar a conectividade de portas TCP/UDP em um determinado host ou IP. O programa permite verificar se uma porta está aberta ou fechada, além de identificar o serviço associado a algumas portas padrão.

## Funcionalidades

- **Varredura de portas TCP**: Identifica se as portas estão abertas ou fechadas.
- **Varredura de portas UDP**: Testa a conectividade em portas UDP.
- **Identificação de serviços**: Exibe o serviço relacionado à porta (exemplo: HTTP para a porta 80).
- **Entrada flexível de portas**: Permite varredura de uma lista de portas específicas ou intervalos de portas.
- **Exibição detalhada**: Mostra o status de cada porta, o serviço e o protocolo.

## Como Usar

### Requisitos
- Python 3.x instalado.

### Sintaxe
```python vrsport.py <domínio/IP> <porta(s)> [opções]```


#### Exemplos

1. **Varredura de portas TCP padrão**:
```python vrsport.py 192.168.0.1 80,443```
Isso fará uma varredura nas portas 80 e 443 no host `192.168.0.1` utilizando o protocolo TCP.

2. **Varredura de portas UDP**:
```python vrsport.py 192.168.0.1 80,443 -UDP```
Isso realizará uma varredura nas portas 80 e 443 no host `192.168.0.1` utilizando o protocolo UDP.

3. **Varredura de intervalo de portas TCP**:
```python vrsport.py 192.168.0.1 20-25```
Realiza uma varredura nas portas 20 a 25 do host `192.168.0.1` utilizando o protocolo TCP.

4. **Varredura em todas as portas TCP padrão**:
```python vrsport.py 192.168.0.1```
Isso realizará uma varredura nas portas padrão (20, 21, 22, 23, 25, 53, 67, 68, 80, 443) no host `192.168.0.1` utilizando o protocolo TCP.

### Parâmetros

- **<domínio/IP>**: O endereço de IP ou domínio do host a ser escaneado.
- **<porta(s)>**: A(s) porta(s) a ser(em) escaneada(s), que pode(m) ser especificada(s) como uma lista separada por vírgulas ou um intervalo de portas (ex: `20,21,22` ou `20-25`).
- **-UDP** (opcional): Indica que a varredura será realizada usando o protocolo UDP.

### Exemplo de Saída

PORT-   -STATUS-     -SERVICE-                            -PROTOCOL\n
20       open         FTP Data Transfer                    TCP/IP\n 
21       open         FTP Control                          TCP/IP\n 
22       closed       SSH (Secure Shell)                   TCP/IP 
80       open         HTTP (HyperText Transfer Protocol)   TCP/IP 
443      open         HTTPS (HTTP Secure)                  TCP/IP


## Como Contribuir

Se você quiser contribuir para o projeto, fique à vontade para abrir issues ou pull requests. Certifique-se de seguir as boas práticas de desenvolvimento e testes.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo para mais detalhes.

## Autor

Desenvolvido por: **Marcos Vinícius - gh0st**

