import cv2
import numpy as np
from datetime import datetime

# Carrega o haarcascade da face
face_cascade = cv2.CascadeClassifier('trabalhoG2\haarcascade_frontalface_default.xml')

# Joga um erro se o arquivo xml não for lido corretamente
if face_cascade.empty():
  raise IOError('Não foi possível carregar o classifier xml file.')

# Configurações iniciais necessárias
clown = False

cap = cv2.VideoCapture(0)
ds_factor = 0.5

# Início do algoritmo
while True:

    # Captura da imagem
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # CONFIGURAÇÃO PARA DETECÇÃO DAS CORES VERMELHA E AZUL
    lower_red = np.array([0, 118, 224])
    lower_blue = np.array([61, 161, 46])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red,upper)
    mask2 = cv2.inRange(hsv, lower_blue,upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    result2 = cv2.bitwise_and(frame, frame, mask=mask2)
    gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    gray_result2 = cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)
    _, border = cv2.threshold(gray_result, 3, 255, cv2.THRESH_BINARY)
    _2, border2 = cv2.threshold(gray_result2, 3, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(border,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _2 = cv2.findContours(border2,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    frame2 = frame.copy()

    # DETECÇÃO DA COR VERMELHA
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
            print('Modo palhaço ativado!')

            # GERAÇÃO DO LOG
            log_text = datetime.now().strftime('[%Y-%m-%d] Modo palhaço ativado às %H:%M:%S')
            file = open('log.txt', 'r', encoding='utf-8')
            logs = file.readlines()
            logs.append(log_text)
            logs.append('\n')
            file = open('log.txt', 'w', encoding='utf-8')
            file.writelines(logs)
            file.close()

            # TRANSFORMA O ALGORITMO EM MODIFICAÇÃO DE PALHAÇO
            clown = True
            face_cascade = cv2.CascadeClassifier('trabalhoG2\haarcascade_mcs_nose.xml')

    # DETECÇÃO DA COR AZUL
    for contour2 in contours2:
        area = cv2.contourArea(contour2)
        if area > 500:
            (x,y,w,h) = cv2.boundingRect(contour2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
            print('Modo blur ativado!')
            clown = False
            face_cascade = cv2.CascadeClassifier('trabalhoG2\haarcascade_frontalface_default.xml')

    # Rects da face detectada
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Se não for detectada uma face, então aplica o blur no frame todo
    if type(face_rects) == tuple and clown == False:
        frame = cv2.blur(frame, (20,20))

    for (x,y,w,h) in face_rects:
        
        # Se o modo palhaço estiver ativo
        if clown == True:
            # Criação do círculo na área detectada
            cv2.circle(frame, (round(x+(w/2)), round((y+(h/2)))), round(h/2), (0,0,255), -1)

            # Criação do retângulo na área do nariz
            cv2.rectangle(frame2, (x,y), (x+w,y+h), (0,255,0), 2)

        # Se o modo blur estiver ativo
        else:
            # Criação do retângulo na área da face
            cv2.rectangle(frame2, (x,y), (x+w,y+h), (0,255,0), 2)
        
            # Aplica blur na área da face detectada
            sub_img = frame[y:y+h, x:x+w]
            img = cv2.blur(sub_img, (20,20))
            frame[y:y+h, x:x+w] = img

        break

    # MOSTRA A FACE BORRADA
    cv2.imshow('Face Blur', frame)

    # MOSTRA A MASK DA COR VERMELHA
    cv2.imshow('Face Mask', result)

    # MOSTRA A ÁREA DA DETECÇÃO FACIAL
    cv2.imshow('Face Detected', frame2)
    
    # Apertar ESC para fechar
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()