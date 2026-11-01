#!/bin/bash
cd "$(dirname "$0")" || exit 1
export PATH="/opt/homebrew/bin:$PATH"

# Premiere utilisation : cree l'environnement Python et installe Flask
if [ ! -x ".venv/bin/python" ]; then
    echo "Premiere installation, patiente quelques secondes..."
    python3.12 -m venv .venv || python3 -m venv .venv
    .venv/bin/python -m pip install -q -r requirements.txt
fi

# Cree la base et charge le programme si besoin (ne touche pas aux donnees)
.venv/bin/python seed.py >/dev/null

# Si une ancienne version de l'appli tourne encore, on l'arrete pour repartir sur la derniere version
lsof -ti tcp:5000 -sTCP:LISTEN | xargs kill 2>/dev/null
sleep 1

[ -z "$SUIVI_NO_BROWSER" ] && (sleep 2; open "http://127.0.0.1:5000/${SUIVI_PAGE:-}") &
echo
echo "  Suivi maths tourne sur http://127.0.0.1:5000"
echo "  Ferme cette fenetre pour arreter l'appli."
echo
exec .venv/bin/python app.py
