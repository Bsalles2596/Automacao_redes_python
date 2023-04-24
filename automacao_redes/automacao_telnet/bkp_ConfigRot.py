## Backup das configuracoes dos roteadores (_cisco_)
## salvar em um arquivo (file) C
## Contendo as informacoes e config dos roteadores

## Para ter certeza da conexaçao intelnet use o comando "debug telnet" no terminal da vm apos rodar o script
import getpass ## So roda ou compila via terminal
import telnetlib
import time
user = 'noc'
password = '6O7noNaoiMClIn7e'

'''Conexao telnet'''

user = input("Digite o seu Usuario: ")
password = getpass.getpass() ## Pega a senha do usuario e salva em uma variavel

lista_routers = open('routers-ip') ## Puxar o arquivo com o numero dos IPs que esta no diretorio

for ip in lista_routers:
    ip = ip.strip() ## retira o espaco
    print('Gerando backup do Roteador' + (ip)) ## Escreve que esta lendo
    HOST = ip
    tn = telnetlib.Telnet(HOST) ## Conexão telnet para o host indicado
    tn.read_until(b"Username: ") ## Faz a leitura ate o loguin
    tn.write(user.encode('ascii') + b"\n") ## transforma o user em ascii
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    ## Modo configuracao
    ## Comandos de escrita do terminal ou equipamento
    ## Mostre tudo e capture oque foi digitado do show running-config

    time.sleep(0.1)
    tn.write(b"terminal length 0\n") ## tamanho do terminal = 0 nao pede a barra de espaco vai ate o final.
    time.sleep(0.1)
    tn.write(b"show running-config\n") ## lista toda configuracao do roteador
    time.sleep(0.1)
    tn.write(b"quit\n")
    ler_config = tn.read_until(b'\r\nend\r').decode("ascii") ## pega o 'tn' e faz a leitura de tudo que esta como 'tn.write'
    tn.read_until(b"[yes/no]:")
    tn.write(b"yes\n")

    save_config = open('backup- ' + HOST, 'W') ## Cria um arquivo com nome 'backup-' e vai escrever o nome
    save_config.write(ler_config.decode('ascii')) ## escreve dentro do arquivo tudo que estiver no 'ler_config'
    ## decodifica para 'ascii' pegua como 'ascii' e entrega como 'ascii'
    save_config.write('\n') ## Pressiona o enter no final
    save_config.close()


print(f'Backup `{ip} Completo!')
