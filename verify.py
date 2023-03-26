import json
import subprocess


with open('interfaces.json', 'r') as f:
    data = json.load(f)

bloco = len(data)
lista = data[0]


ciclo = 0
while ciclo < bloco:
  b0 = data[ciclo]
  iface = b0["ifname"]
  rx = subprocess.run(['iwlist',iface,'scanning'], capture_output=True)
  if(rx.returncode == 0):
     saida = rx.stdout.decode('utf-8')
     print('INTERFACE DE REDE SEM FIO ENCONTRADA ->',iface)
     break
  ciclo = ciclo + 1


jsl = saida.split()
redes = jsl.count('Cell')
interface = jsl[0]
print(redes,'REDES ENCONTRADAS')

del jsl[0]
del jsl[0]
del jsl[0]
del jsl[0]

####################################--[ TRATAMENTO DE ARRAY ]--########################################

print('\n\n')

bloco = []
drs = []
cnx = 0

while redes > 0:
  array_interno = []
  while True:
    if 'Extra:fm' in jsl[cnx]:
      array_interno.append(jsl[cnx])
      cnx = cnx + 1
      break
    else:
      array_interno.append(jsl[cnx])
      cnx = cnx + 1
  redes = redes - 1
  drs.append(array_interno)

print(drs)





redex = jsl.count('Cell')
paramex = len(jsl)
div = paramex / redex
print('\n\nParâmetros:',paramex)
print(div,'Por rede')   