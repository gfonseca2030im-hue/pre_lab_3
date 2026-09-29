opcion = input("Elige una opcion: ")

match opcion:
    case "A":
        print("Iniciando diagnóstico del sistema...")
    case "B":
        print("Activando enfriamiento de emergencia..." )
    case "C":
        print("Mostrando registro de errores...")
    case "D":
        print("Apagando el panel." )
    case _:
        print("Comando no reconocido. Intente de nuevo.")