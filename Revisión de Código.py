import os
import json

def insecure_eval():
    # Solicita código del usuario y lo evalúa directamente (¡Muy inseguro!)
    user_code = input("Ingresa el código a ejecutar: ")
    try:
        result = eval(user_code)  # Uso de eval sin sanitizar la entrada
        print("Resultado:", result)
    except Exception as e:
        print("Error al ejecutar eval:", e)

def process_data(data):
    results = []
    # Proceso ineficiente y con lógica redundante
    for item in data:
        if isinstance(item, dict):
            if 'value' in item:
                try:
                    # Uso inseguro de exec para calcular el valor duplicado
                    exec("temp = item['value'] * 2")
                    results.append(temp)
                except Exception as e:
                    print("Error al procesar el item:", e)
            else:
                print("Falta la clave 'value' en", item)
        else:
            print("El item no es un diccionario:", item)
    return results

def store_sensitive_info(info):
    # Guardar información sensible en un archivo de texto sin cifrado
    try:
        with open("info.txt", "w") as f:
            f.write(str(info))
    except Exception as e:
        print("Error al guardar la información:", e)

def main():
    # Datos sensibles hardcodeados (mala práctica de seguridad)
    password = "12345"
    print("La contraseña de administrador es:", password)
    
    # Datos de ejemplo para procesar
    sample_data = [
        {"value": 10},
        {"value": 20},
        {"not_value": 30},
        "invalido",
    ]
    results = process_data(sample_data)
    print("Resultados procesados:", results)
    
    # Guarda la contraseña y resultados sin protección
    store_sensitive_info({"password": password, "results": results})
    
    # Ejecuta una función insegura que utiliza eval()
    insecure_eval()

if __name__ == "__main__":
    main()
