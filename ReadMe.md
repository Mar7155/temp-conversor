# Conversor de Temperaturas

Este es un programa simple en Python que convierte temperaturas entre Celsius y Fahrenheit. El proyecto incluye la creación de un ejecutable para facilitar su distribución.

## 📋 Contenido
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Creación del Ejecutable](#creación-del-ejecutable)
- [Problemas Encontrados y Soluciones](#problemas-encontrados-y-soluciones)
- [Estructura del Código](#estructura-del-código)

## ✨ Características
- Conversión de Celsius a Fahrenheit
- Conversión de Fahrenheit a Celsius
- Interfaz de línea de comandos simple
- Manejo de errores para entradas inválidas
- Ejecutable standalone

## 🔧 Requisitos
- Python 3.x
- PyInstaller (para crear el ejecutable)

## 💻 Instalación

1. Clona o descarga este repositorio
```bash
git clone [url-del-repositorio]
```

## 📦 Instalar dependencias

Instala las dependencias necesarias:

```bash
python -m pip install pyinstaller
```

## 🚀 Uso

El programa puede ejecutarse de dos formas:

**1. Directamente con Python:**

```bash
python main.py
```

**2. Usando el ejecutable generado (después de crear el `.exe`):**

- Navega a la carpeta `dist`
- Ejecuta `main.exe`

## 🛠️ Creación del Ejecutable

Para crear el ejecutable, se utilizó PyInstaller:

```bash
python -m PyInstaller --onefile main.py
```

## 📁 Archivos generados

- `dist/`: Contiene el ejecutable final  
- `build/`: Archivos temporales de construcción  
- `main.spec`: Archivo de especificación de PyInstaller

## ⚠️ Problemas Encontrados y Soluciones

### 1. PyInstaller no reconocido

**Problema:** El comando `pyinstaller` no era reconocido en la terminal.  
**Solución:** Usar la ruta completa con `python -m`:

```bash
python -m PyInstaller --onefile main.py
```

### 2. Manejo de errores de entrada

**Problema:** El programa crasheaba con entradas no numéricas.  
**Solución:** Implementación de manejo de excepciones:

```python
try:
    return float(input(f"Enter temperature in {unit}: "))
except ValueError:
    print("Please enter a valid number")
```

## 🔍 Estructura del Código

### Funciones Principales

#### `celsius_to_fahrenheit(celsius: float) -> float`

Convierte temperaturas de Celsius a Fahrenheit.

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32
```

#### `fahrenheit_to_celsius(fahrenheit: float) -> float`

Convierte temperaturas de Fahrenheit a Celsius.

```python
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9
```

#### `get_temperature_input(unit: str) -> float`

Maneja la entrada del usuario con validación.

```python
def get_temperature_input(unit: str) -> float:
    """Get and validate temperature input from user
    Args:
        unit (str): Temperature unit (Celsius/Fahrenheit)
    Returns:
        float: Valid temperature input
    """
    while True:
        try:
            return float(input(f"Enter temperature in {unit}: "))
        except ValueError:
            print("Please enter a valid number")
```

### Función Principal

```python
def main():
    MENU = """=== TEMPERATURE CONVERTER ===
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
"""
    print(MENU)
    
    conversion_map = {
        "1": ("Celsius", celsius_to_fahrenheit),
        "2": ("Fahrenheit", fahrenheit_to_celsius)
    }
    
    option = input("Select an option (1/2): ")
    
    if option in conversion_map:
        unit, converter = conversion_map[option]
        temperature = get_temperature_input(unit)
        result = converter(temperature)
        print(f"{temperature}°{unit[0]} equals {result:.2f}°{'F' if unit == 'Celsius' else 'C'}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
```

## ✅ Optimizaciones Implementadas

- Uso de *type hints* para mejor documentación
- Implementación de manejo de errores robusto
- Uso de diccionarios para mapeo de opciones
- Código modular y reutilizable
- Documentación completa con *docstrings*

## 📝 Notas Adicionales

- El ejecutable puede ser más grande que el script original debido a que incluye todas las dependencias necesarias.
- La primera ejecución del programa puede ser más lenta debido a la extracción de archivos.
- Se recomienda probar el ejecutable en un sistema limpio para verificar su funcionamiento.