import pickle

import socket


def encode(a):
  result = {}
  for i, j in a:
    if i != "tout":
      result.update({i:j})

  return result

def send(a):
  response = pickle.dumps([""])
  data = pickle.dumps(a)
  sock = socket.socket()
  if True:#try:
    sock.connect(("172.16.5.4", 1111))
    sock.send(data)
    response = sock.recv(8192)
    return pickle.loads(response)
  #except Exception:
    return pickle.loads(response)
    