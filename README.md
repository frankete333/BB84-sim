# Simulador BB84 - Distribución Cuántica de Claves

Este proyecto implementa una simulación del protocolo BB84 (Bennett-Brassard 1984) para la distribución cuántica de claves utilizando Qiskit.

## Descripción

El protocolo BB84 es un algoritmo de criptografía cuántica que permite a dos partes (Alice y Bob) generar una clave secreta compartida a través de un canal cuántico, detectando la presencia de un espía (Eve) en el proceso.

## Características

- Simulación del protocolo BB84 con 1000 qubits
- Detección de interceptación en el canal cuántico
- Cálculo de la tasa de error para detectar espionaje
- Uso del simulador Qiskit Aer para computación cuántica

## Requisitos

- Python 3.10
- Qiskit
- Qiskit Aer

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd BB84-sim
```

2. Instala las dependencias usando pipenv:
```bash
pipenv install
```

3. Activa el entorno virtual:
```bash
pipenv shell
```

## Uso

Para ejecutar la simulación:

```bash
python src/simulator.py
```

## Configuración

Puedes modificar los siguientes parámetros en `src/simulator.py`:

- `number_of_qubits`: Número de qubits a utilizar (por defecto: 1000)
- `is_channel_compromised`: Si el canal está comprometido (por defecto: True)
- `e_read_probability`: Probabilidad de lectura por Eve (por defecto: 1)

## Resultados

El simulador mostrará:
- Número de resultados coincidentes
- Número de resultados incorrectos
- Porcentaje de errores en los qubits probados

## Estructura del Proyecto

```
BB84-sim/
├── src/
│   └── simulator.py    # Implementación principal del protocolo BB84
├── outputs/            # Directorio para resultados
├── Pipfile            # Dependencias del proyecto
└── README.md          # Este archivo
```

## Cómo Funciona

1. **Alice** genera bits aleatorios y decide si aplicar la puerta Hadamard
2. **Eve** (opcional) intercepta y mide los qubits en el canal
3. **Bob** recibe los qubits y decide si aplicar Hadamard
4. Se comparan las bases utilizadas y se calcula la tasa de error
5. Si la tasa de error es alta, se detecta la presencia de un espía

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.
