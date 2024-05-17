import socket

#import cv2
import streamlit as st

import page
import module


def enregistrer_video(nom_fichier="video_enregistree.avi", largeur=640, hauteur=480, duree=10):
  # Configuration de la capture vidéo
  capture = cv2.VideoCapture(0)
  capture.set(cv2.CAP_PROP_FRAME_WIDTH, largeur)
  capture.set(cv2.CAP_PROP_FRAME_HEIGHT, hauteur)

  # Configuration du codec et de la vidéo Writer
  codec = cv2.VideoWriter_fourcc(*'XVID')
  sortie_video = cv2.VideoWriter(nom_fichier, codec, 20.0, (largeur, hauteur))

  # Enregistrement de la vidéo
  debut_enregistrement = cv2.getTickCount()
  while True:
    ret, frame = capture.read()
    if not ret:
      break

    sortie_video.write(frame)
    cv2.imshow('Enregistrement', frame)

    if (cv2.getTickCount() - debut_enregistrement) / cv2.getTickFrequency() >= duree:
      break

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Libération des ressources
  capture.release()
  sortie_video.release()
  cv2.destroyAllWindows()

# Exemple d'utilisation de la fonction pour enregistrer une vidéo de 10 secondes
#enregistrer_video("video.mp4", 640, 480, 10)


# Exécuter la fonction
def send(a):
  video = open(a, 'rb').read()
  sock = socket.socket()
  sock.connect(('172.31.196.49', 8080))
  sock.send(video)
  response = sock.recv(8192)
  return response.decode()

try:
  #x = send("video.mp4")
  x = int(x)if x.isdigit()else 0
  if x > 0:
    st.write("ok")
except Exception:
  pass

w = page.page()
if w == 1:
  st.title("Home")

  st.write("Bonjours, adolescents !")
  st.write("Bienvenue sur notre site web !")
  st.write("il est fait pour vous permetre de rencontrer des personnes qui vous intéressent.")

if w == 2:
  st.title("Recherche")
  st.write("vous pouvez rechercher des personnes en fonction de leur age, de leur genre etc...")

  number = st.number_input("Entrez un age minimum : ", min_value=0, max_value=25, step=1)
  
  number2 = st.number_input("Entrez un age maximum : ", min_value=0, max_value=25, step=1)

  genre = st.selectbox("Choisissez un genre : ", ("homme", "femme", "home transgenre", "femme transgenre", "non-binaire", "inter-sexs", "tout"))
  orientation = st.selectbox("Choisissez une orientation sexuelle : ",["Hétérosexuel(le)", "Homosexuel(le)", "Bisexuel(le)", "Pansexuel(le)", "Asexuel(le)", "Aromantique", "Autre", "tout"])

  dico = {"age":[number, number2], "genre":genre, "orientation":orientation}
  if st.button("Rechercher"):
    st.write(module.send(dico))

if w == 3:
  st.title("Proposition")
  st.write("nous alons vous proposer des personnes suseptibles de vous plaire")

if w == 4:
  st.title("Message")
  st.text_input("votre correspondant")
  st.chat_input("votre message")

if w == 5:
  st.title("Messages recu")
  for i in ["message recu"]:
    st.write(i)