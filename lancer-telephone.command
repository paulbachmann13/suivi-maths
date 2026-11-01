#!/bin/bash
# Meme chose que lancer.command, mais l'appli est accessible depuis le telephone (meme Wi-Fi)
cd "$(dirname "$0")" || exit 1
export SUIVI_LAN=1
export SUIVI_PAGE=telephone
echo "  Au premier lancement, macOS peut demander d'autoriser Python a recevoir des connexions : Autoriser."
exec ./lancer.command
