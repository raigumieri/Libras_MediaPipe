import cv2
import mediapipe as mp
import serial
import time
import math

# Inicializa comunicação com o Arduino
arduino = serial.Serial('COM5', 9600)  # Ajuste a porta conforme necessário
time.sleep(2)

# Inicializa o MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

ultima_letra = None

def enviar_para_arduino(letra):
    global ultima_letra
    if letra and letra != ultima_letra:
        arduino.write(letra.encode())
        print(f"Letra enviada para o Arduino: {letra}")
        ultima_letra = letra

def calcular_distancia(p1, p2):
    # Calcula a distância entre dois pontos (p1, p2)
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def identificar_vogal(landmarks):
    # Definindo os pontos de interesse: ponta do indicador (8), do meio (12) e polegar (4)
    polegar_ponta = landmarks[4]
    medio_ponta = landmarks[12]
    i_ponta = landmarks[8]
    anelar_ponta = landmarks[16]
    anelar_medio = landmarks[13]

    # Calculando a distância entre a ponta do indicador e a ponta do médio
    distancia = calcular_distancia(anelar_ponta, anelar_medio)
    print(f"Distância entre o indicador e o médio: {distancia}")


    # Pontos principais
    base = landmarks[3].y  # Base: polegar como referência

    dedo_polegar   = landmarks[4].y < base
    dedo_indicador = landmarks[8].y < base
    dedo_medio     = landmarks[12].y < base
    dedo_anelar    = landmarks[16].y < base
    dedo_minimo    = landmarks[20].y < base
    dedo_anelar_base    = landmarks[13].y < base

    dist_OM = abs(landmarks[8].x - landmarks[12].x)
    dist_OM2 = abs(landmarks[20].x - landmarks[4].x)
    dist_AB = abs(landmarks[16].x - landmarks[13].x)

    # A - Nenhum dedo levantado
    if not dedo_indicador and not dedo_medio and not dedo_anelar and not dedo_minimo:
        return "A"
    
    # E - Todos os dedos levantados
    elif dist_AB > 0.03 and dist_AB < 0.05:
        return "E"
    
    # I - Apenas o dedo mínimo levantado
    elif dedo_minimo and not dedo_indicador and not dedo_medio and not dedo_anelar:
        return "I"
    
    # O - Dedo minimo e polegar próximos
    elif dist_OM2 > 0.030 and dist_OM2 < 0.1:
        return "O"
    
    # U - Apenas indicador e médio levantados
    elif dedo_indicador and dedo_medio and not dedo_anelar and not dedo_minimo: 
        if dist_OM > 0.025:
            return "U"
    
    return None

# Carrega o vídeo
video_path = "video.mp4"
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 800)) # 1100 600
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            letra = identificar_vogal(hand_landmarks.landmark)
            if letra:
                cv2.putText(frame, f"Letra: {letra}", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)
                enviar_para_arduino(letra)

    cv2.imshow("Detector de Vogais em Libras", frame)

    if cv2.waitKey(25   ) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
