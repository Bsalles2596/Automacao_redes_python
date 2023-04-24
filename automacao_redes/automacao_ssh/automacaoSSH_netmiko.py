from netmiko import ConnectHandler


user = 'noc'
password = '6O7noNaoiMClIn7e'
model = 'C300-SE77E-OLT-ZTE-CAP'

C300 = {
    'device_type':'C300-SE77E-OLT-ZTE-CAP',
    'host':'noc',
    'username': 'noc',
    'password': '6O7noNaoiMClIn7e',
}

connect = ConnectHandler(**C300)

bkp_OLTs = ['terminal length 0\n', 'show running-config\n'] ## Posso executar mais de um comando 

configurar = connect.send_command(bkp_OLTs)

output = connect.send_command("show running-config")
print(output)