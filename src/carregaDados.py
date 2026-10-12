import json
from pathlib import Path

def carregar_disciplinas():
    caminho = Path(__file__).parent.parent / "data" / "disciplinas.json"
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)
