from pathlib import Path

import pandas as pd
import pytest

from analysis import load, main, summary

DATA = Path(__file__).resolve().parents[1] / "data" / "datos.csv"


def test_summary_computes_expected_values(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 10, 10], "texto": ["x", "y", "z"]})
    s = summary(df)
    assert list(s.index) == ["a", "b"]
    assert s.loc["a", "mean"] == 2.0
    assert s.loc["a", "median"] == 2.0
    assert s.loc["b", "std"] == 0.0


def test_summary_rejects_non_numeric_only():
    with pytest.raises(ValueError):
        summary(pd.DataFrame({"texto": ["x", "y"]}))


def test_load_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load(tmp_path / "no.csv")


def test_load_empty_file_raises(tmp_path):
    p = tmp_path / "vacio.csv"
    p.write_text("a,b\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load(p)


def test_main_runs_on_bundled_data(capsys):
    assert main([str(DATA)]) == 0
    assert "filas" in capsys.readouterr().out
