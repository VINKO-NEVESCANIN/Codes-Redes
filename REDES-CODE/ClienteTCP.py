# cliente_tcp.py
# ----------------------------
# Ejemplo de cliente TCP básico
# Unidad 3 - Programación en Redes
# ----------------------------

import socket

# Dirección y puerto del servidor
HOST = "127.0.0.1"   # Localhost (misma PC)
PORT = 5000          # Mismo puerto que el servidor

# Crear socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar con el servidor
client.connect((HOST, PORT))
print(f"🔗 Conectado al servidor {HOST}:{PORT}")

# Bucle de comunicación
while True:
    msg = input("💬 Escribe un mensaje ('salir' para terminar): ")
    if msg.lower() == "salir":
        break

    # Enviar mensaje
    client.sendall(msg.encode())

    # Recibir respuesta del servidor
    data = client.recv(1024).decode()
    print(f"📬 Servidor respondió: {data}")

# Cerrar conexión
client.close()
print("🔒 Cliente desconectado.")
