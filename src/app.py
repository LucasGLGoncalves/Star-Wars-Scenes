import os
from os import uname

from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


def get_scene() -> str:
    """Retorna o tema da cena.

    Valores aceitos: batalha | tranquilo
    """
    scene = (os.getenv("SCENE") or "tranquilo").strip().lower()
    if scene not in {"batalha", "tranquilo"}:
        scene = "tranquilo"
    return scene


def get_header_text(scene: str) -> str:
    header = (os.getenv("HEADER_TEXT") or scene).strip()
    if not header:
        header = scene
    return header


@app.get("/")
def index():
    scene = get_scene()
    header_text = get_header_text(scene)
    return render_template(
        "index.html",
        maquina=uname().nodename,
        scene=scene,
        header_text=header_text,
    )


@app.get("/healthz")
def healthz():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # Debug local (em container, quem serve é o gunicorn)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "80")))
