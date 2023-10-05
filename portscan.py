import socket, sys
for porta in range(1, 65535):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.04)
  
  if len(sys.argv) >= 3:
    if sys.argv[2] == "-v":
      print("Verificando porta: ", porta, "...")
  
  if s.connect_ex((sys.argv[1], porta)) == 0:
    print("=====Porta", porta, "[ABERTA]=====")
    s.close()