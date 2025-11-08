# servidor_tcp.py
# ----------------------------
# Ejemplo de servidor TCP básico
# Unidad 3 - Programación en Redes
# ----------------------------

import socket   # Importamos la librería estándar de sockets

# Dirección y puerto del servidor
HOST = "0.0.0.0"   # Escucha en todas las interfaces de red
PORT = 5000        # Puerto TCP (puedes cambiarlo si está ocupado)

# Crear el socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto
server.bind((HOST, PORT))

# Poner el servidor en modo escucha (máximo 1 cliente en cola)
server.listen(1)
print(f"✅ Servidor TCP escuchando en {HOST}:{PORT}")

# Esperar y aceptar conexión de un cliente
conn, addr = server.accept()
print(f"🔗 Conexión establecida con: {addr}")

# Comunicación con el cliente
while True:
    data = conn.recv(1024)  # Recibe hasta 1024 bytes
    if not data:
        print("❌ Cliente desconectado.")
        break
    print(f"📩 Cliente dice: {data.decode()}")
    conn.sendall("Mensaje recibido ✅".encode())

# Cerrar la conexión
conn.close()
server.close()
print("🔒 Servidor cerrado.")
