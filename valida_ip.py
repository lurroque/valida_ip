def ip_ok(ip):
    ip = ip.split(".")
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
arquivo = open("IPS.txt")
validos = open("validos.txt", "w")
invalidos = open("invalidos.txt", "w")
for linha in arquivo.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arquivo.close()
validos.close()
invalidos.close()
