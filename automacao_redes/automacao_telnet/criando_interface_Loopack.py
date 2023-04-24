## Interface Loopack 0 script
## Para ter certeza da conexaçao intelnet use o comando "debug telnet" no terminal da vm apos rodar o script
import getpass ## So roda ou compila via terminal
import telnetlib

'''Conexao telnet'''
HOST = "localhost" # IP
user = input("Digite o seu Usuario: ")
password = getpass.getpass() ## Pega a senha do usuario cisco e salva em uma variavel

tn = telnetlib.Telnet(HOST) ## Conexão telnet para o host indicado

tn.read_until(b"login: ") ## Faz a leitura ate o loguin
tn.write(user.encode('ascii') + b"\n") ## transforma o user em ascii
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

## Comandos de escrita em um terminal ou equipamento

tn.write(b" config t\n")
tn.write(b" interface loopback 0\n")
tn.write(b" ip address 1.1.1.1 255.255.255.0\n")
tn.write(b" end t\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))