# student-project

[![CI](https://github.com/Joseverav02/student-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Joseverav02/student-project/actions/workflows/ci.yml)

Herramienta de línea de comandos que lee un CSV y calcula estadísticas descriptivas (media, mediana, desviación típica, mínimo y máximo) de cada columna numérica.

## Uso

```bash
pip install -r requirements.txt
python analysis.py data/datos.csv
pytest -q
```

Ejemplo de salida:

```
3 filas, 4 columnas
```

## Estructura

```
analysis.py          # carga, resumen y CLI
data/datos.csv       # datos de ejemplo
tests/test_analysis.py
```

## Licencia
MIT
