def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key")
listarTerminos(Nombre="Leonel Messi")