def binario_para_decimal_ipv4(endereco_binario):
  
  octetos_binario= endereco_binario.split('.')
  octetos_decimal = []

  for octeto in octetos_binario:
    if len(octeto)!=8:
      raise ValueError("Uga buga, isto nao ser octeto")
    decimal = 0
    for enum,bit in enumerate(octeto):
      if bit == "1": 
        decimal += 2**enum
      elif bit != "0":    
        raise ValueError("Uga buga, isto nao ser da base 2")
    octetos_decimal.append(str(decimal))
  return ".".join(octetos_decimal)

def decimal_para_binario_ipv4(endereco_decimal):
  
  octetos_decimais = endereco_decimal.split('.')
  octetos_binarios = []

  for octeto in octetos_decimais:
    try: 
      int(octeto)
    except:
      raise ValueError("Uga buga, isto nao ser da base 10")
    if int(octeto) >255 or int(octeto) <0:
      raise ValueError("Uga buga, isto nao ser ip")
    binario = bin(int(octeto))[2:]
    while len(binario)<8:
      binario= "0" + binario
    octetos_binarios.append(binario)
  return ".".join(octetos_binarios)

print(binario_para_decimal_ipv4("00000000.00000000.00000000.00000000"))
print(decimal_para_binario_ipv4("0.0.0.0"))