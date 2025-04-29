def celsius_to_fahrenheit(celsius: float) -> float:
    """convierte Celsius a Fahrenheit
    
    Params:
        celsius (float): Temperatura en celsius
        
    Retorna:
        float: TTemperatura en Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convierte Fahrenheit a Celsius
    
    Params:
        fahrenheit (float): Temperatura en Fahrenheit
        
    Retorna:
        float: Temperatura en Celsius
    """
    return (fahrenheit - 32) * 5/9

def get_temperature_input(unit: str) -> float:
    """Solicita al usuario una temperatura válida en la unidad especificada
    
    Params:
        Unidad (str): Temperatura en (Celsius/Fahrenheit)
        
    Retorna:
        float: Temperatura valida en la unidad especificada
    """
    while True:
        try:
            return float(input(f"Ingresa una temperatura valida {unit}: "))
        except ValueError:
            print("Input no valido. Por favor, ingresa un numero.")

def main():
    MENU = """=== Convertidor de Temperatura ===
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
"""
    print(MENU)
    
    conversion_map = {
        "1": ("Celsius", celsius_to_fahrenheit),
        "2": ("Fahrenheit", fahrenheit_to_celsius)
    }
    
    option = input("Selecciona una opcion (1/2): ")
    
    if option in conversion_map:
        unit, converter = conversion_map[option]
        temperature = get_temperature_input(unit)
        result = converter(temperature)
        print(f"{temperature}°{unit[0]} equals {result:.2f}°{'F' if unit == 'Celsius' else 'C'}")
    else:
        print("Opcion no valida. Por favor, selecciona 1 o 2.")

main()