"""Análisis descriptivo de un CSV: estadísticas por columna numérica.

Uso:
    python analysis.py data/datos.csv
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


def load(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("El archivo no contiene filas de datos")
    return df


def summary(df: pd.DataFrame) -> pd.DataFrame:
    """Media, mediana, desviación típica, mínimo y máximo de cada columna numérica."""
    numeric = df.select_dtypes("number")
    if numeric.empty:
        raise ValueError("No hay columnas numéricas para resumir")
    return numeric.agg(["mean", "median", "std", "min", "max"]).T.round(2)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    path = Path(args[0]) if args else Path("data/datos.csv")
    df = load(path)
    print(f"{len(df)} filas, {df.shape[1]} columnas\n")
    print(summary(df).to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
