import cv2
import time
import os
import math

pasta = r"D:\Timelapse"

def capturar_fotos(duracao_horas=0, duracao_minutos=0, intervalo_segundos=10):
    duracao_segundos = duracao_horas * 3600 + duracao_minutos * 60

    if duracao_segundos > 3600:
        duracao_horas = math.ceil(duracao_segundos / 3600)
        duracao_minutos = 0
        duracao_segundos = duracao_horas * 3600
    num_fotos = duracao_segundos // intervalo_segundos

    os.makedirs(pasta, exist_ok=True)

    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    time.sleep(1)

    for i in range(num_fotos):
        ret, frame = cap.read()

        nome_arquivo = os.path.join(pasta, f"imagem_{i+1:04d}.jpg")
        cv2.imwrite(nome_arquivo, frame)

        time.sleep(intervalo_segundos)

    cap.release()

def gerar_timelapse(fps=29):
    arquivos = os.listdir(pasta)
    arquivos = [arquivo for arquivo in arquivos if arquivo.endswith(".jpg")]
    arquivos.sort()

    primeira_imagem = cv2.imread(os.path.join(pasta, arquivos[0]))
    altura, largura, _ = primeira_imagem.shape

    nome_arquivo = os.path.join(pasta, "timelapse.avi")
    video = cv2.VideoWriter(nome_arquivo, cv2.VideoWriter_fourcc(*"MJPG"), fps, (largura, altura))

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        imagem = cv2.imread(caminho_arquivo)

        video.write(imagem)

    video.release()


# capturar_fotos(2, 0, 15) # Habilite para tirar uma foto a cada 15 segundos num período de 2 horas
gerar_timelapse() # Gerar o timelapse