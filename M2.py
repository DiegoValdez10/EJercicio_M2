def cargar_buffer(entrada, inicio, tamano_buffer):

    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(buffer, inicio_lexema, avance):
    lexema = ""
    while avance < len(buffer):
        char = buffer[avance]
        
        if char == "eof":

            if lexema:
                print(f"Lexema encontrado: {lexema}")
            return avance, True 
            
        elif char == " ":
            if lexema:
                print(f"Lexema encontrado: {lexema}")
                lexema = ""
            inicio_lexema = avance + 1
            
        else:
            lexema += char
        
        avance += 1
    

    if lexema:
        print(f"Lexema encontrado: {lexema}")
    
    return avance, False

def analizar_entrada(entrada, tamano_buffer):
    pos_entrada = 0  
    encontrado_eof = False
    
    while not encontrado_eof:

        buffer = cargar_buffer(entrada, pos_entrada, tamano_buffer)
        

        inicio_lexema = 0
        avance = 0
        

        avance, encontrado_eof = procesar_buffer(buffer, inicio_lexema, avance)
        

        pos_entrada += tamano_buffer


entrada = list("Esto es un ejemplo eof")
tamano_buffer = 10
analizar_entrada(entrada, tamano_buffer)