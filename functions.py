
# ------ Función para registrar usuarios --------

array_usuarios = []

def registrarUsuario():
    
    while True:
        
        usuario_nombre_completo = input("\n" + "   Nombre completo del usuario: ")
        usuario_cedula = input("   Cedula del usuario: ")
        usuario_correo = input("   Correo del usuario: ")
        
        usuario = {
            "nombre_completo": usuario_nombre_completo,
            "cedula": usuario_cedula,
            "correo": usuario_correo
        }
        
        array_usuarios.append(usuario)
        
        print("\n" + "Registro exitoso.... \n")
        
        while True:
            respuesta = input("¿Desea registrar otro usuario? (s/n): ")
            if respuesta.lower() == "s" or respuesta.lower() == "n":
                break
            else:
                print("\n" + "Por favor, seleccione una opción válida (s/n). \n")
        if respuesta.lower() != "s":
            break

# ---------------- ------------- ----------------  
 
    
    
# ---- Función para consultar los usuarios ------

def consultarUsuarios():
    
    print("\n" + "Listado de usuarios registrados: \n")
    
    if len(array_usuarios) == 0:
        
        print("No hay usuarios registrados. \n")
        
    else:
        
        for usuario in array_usuarios:
            
            print("------------------------------------ -----")
            print(" Nombre completo: " + usuario["nombre_completo"])
            print(" Cedula: " + usuario["cedula"])
            print(" Correo: " + usuario["correo"])
            print("------------------------------------ ----- \n")

# ---------------- ------------- ----------------
    
    
    
# ------ Función para rentar bicicletas ---------

array_rentas = []

def registrarRenta():
    
    while True:
        
        cedula_usuario = input("\n" + "   Ingrese el número de cédula del usuario: ")
        cedula_encontrada = False
        
        for usuario in array_usuarios:
            if usuario["cedula"] == cedula_usuario:
                cedula_encontrada = True
                break
        if not cedula_encontrada:
            print("\n" + "   Cédula no existente. Por favor, ingrese un número de cédula válido.")
            continue
        
        origen_viaje = input("   Ingrese el origen del viaje: ")
        destino_viaje = input("   Ingrese el destino del viaje: ")
        
        renta = {
            "cedula_usuario": cedula_usuario,
            "origen_viaje": origen_viaje,
            "destino_viaje": destino_viaje
        }
        
        array_rentas.append(renta)
        
        print("\n" + "Renta exitosa.... \n")
        
        while True:
            respuesta = input("¿Desea rentar otra bicicleta? (s/n): ")
            if respuesta.lower() == "s" or respuesta.lower() == "n":
                break
            else:
                print("Por favor, seleccione una opción válida (s/n).")
        if respuesta.lower() != "s":
            break

# ---------------- ------------- ----------------    
    
    
    
# ----- Función para consultar las rentas -------

def consultarRentas():
    
    print("\n" + "Listado de rentas realizadas: \n")
    
    if len(array_rentas) == 0:
        
        print("No hay rentas registradas. \n")
        
    else:
        
        for renta in array_rentas:
            
            print("------------------------------------ -----")
            cedula = renta["cedula_usuario"]
            nombre = ""
            
            for usuario in array_usuarios:
                if usuario["cedula"] == cedula:
                    nombre = usuario["nombre_completo"]
                    break
                
            print(" Nombre del usuario: " + nombre)
            print(" Cedula del usuario: " + cedula)
            print(" Origen: " + renta["origen_viaje"])
            print(" Destino: " + renta["destino_viaje"])
            print("------------------------------------ ----- \n")

# ---------------- ------------- ----------------