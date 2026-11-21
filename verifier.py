#!/usr/bin/env python3
"""Contrôles avant chaque commit de la traduction de Computing 101.

Compare le dépôt français au dojo d'origine cloné dans sources/challenges-upstream.
Ne dépend que de la bibliothèque standard ; le YAML est lu avec Ruby (présent sur macOS).
Code de sortie 0 si aucune erreur, 1 sinon.
"""

import collections
import json
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent
ORIGINE = RACINE / "sources" / "challenges-upstream" / "challenges" / "linux-luminarium"
MARQUEUR_FICHE = "## Fiche de cours (ajout, hors traduction)"
TIRETS_INTERDITS = ("—", "–")
PONCTUATION_FRANCAISE = re.compile(r"[^\s ] [;:?!»]|« [^\s ]")

erreurs = []
avertissements = []


def erreur(message):
    erreurs.append(message)


def lire_yaml(chemin):
    script = "require 'yaml'; require 'json'; puts JSON.generate(YAML.load_file(ARGV[0]))"
    resultat = subprocess.run(
        ["ruby", "-ryaml", "-rjson", "-e", script, str(chemin)],
        capture_output=True, text=True, check=True,
    )
    return json.loads(resultat.stdout)


def decouper_code(texte):
    """Retourne (blocs de code délimités, code en ligne) hors section fiche."""
    blocs = re.findall(r"^[ \t]*```[^\n]*\n(.*?)^[ \t]*```", texte, flags=re.S | re.M)
    sans_blocs = re.sub(r"^[ \t]*```[^\n]*\n.*?^[ \t]*```", "", texte, flags=re.S | re.M)
    en_ligne = [a or b for a, b in re.findall(r"``(.+?)``|`([^`]+)`", sans_blocs)]
    return blocs, en_ligne


def partie_avant_fiche(texte):
    return texte.split(MARQUEUR_FICHE, 1)[0]


def normaliser_lien(url):
    if url.startswith("https://pwn.college/linux-luminarium/"):
        return "https://pwn.college/linux-luminarium-fr/" + url[len("https://pwn.college/linux-luminarium/"):]
    if url.startswith("/linux-luminarium/"):
        return "https://pwn.college/linux-luminarium-fr/" + url[len("/linux-luminarium/"):]
    if url.startswith("/") and not url.startswith("//"):
        return "https://pwn.college" + url
    return url


def liens(texte, normaliser=False):
    urls = re.findall(r"\]\(([^)\s]+)\)", texte)
    if normaliser:
        urls = [normaliser_lien(u) for u in urls]
    return sorted(set(urls) | set(re.findall(r"<(https?://[^>]+)>", texte)))


def sans_code(texte):
    texte = re.sub(r"^[ \t]*```[^\n]*\n.*?^[ \t]*```", "", texte, flags=re.S | re.M)
    return re.sub(r"`[^`]+`", "", texte)


def verifier_typographie(chemin, texte):
    prose = sans_code(texte)
    for numero, ligne in enumerate(prose.split("\n"), 1):
        if ligne.lstrip().startswith(">"):
            continue
        if PONCTUATION_FRANCAISE.search(ligne):
            erreur(f"{chemin}:{numero}: espace ordinaire avant ; : ? ! ou » (utiliser une espace insécable)")


def verifier_tirets(chemin, texte):
    for tiret in TIRETS_INTERDITS:
        if tiret in texte:
            erreur(f"{chemin}: tiret long ou demi-cadratin interdit")


def verifier_texte(chemin_original, chemin_traduit):
    original = chemin_original.read_text(encoding="utf-8")
    traduit = chemin_traduit.read_text(encoding="utf-8")
    if not traduit.strip():
        erreur(f"{chemin_traduit}: traduction vide")
        return
    if traduit.strip() == original.strip():
        erreur(f"{chemin_traduit}: texte identique à l'original (non traduit)")

    verifier_tirets(chemin_traduit, traduit)
    verifier_typographie(chemin_traduit, traduit)

    avant_o = partie_avant_fiche(original)
    avant_t = partie_avant_fiche(traduit)
    blocs_o, en_ligne_o = decouper_code(avant_o)
    blocs_t, en_ligne_t = decouper_code(avant_t)
    if blocs_o != blocs_t:
        erreur(f"{chemin_traduit}: blocs de code différents de l'original ({len(blocs_t)} au lieu de {len(blocs_o)})")
    ensemble_o = set(en_ligne_o)
    ensemble_t = set(en_ligne_t)
    if ensemble_o != ensemble_t:
        manquants = sorted(ensemble_o - ensemble_t)
        ajoutes = sorted(ensemble_t - ensemble_o)
        erreur(f"{chemin_traduit}: code en ligne absent de l'original ou manquant (manquants: {manquants}, ajoutés: {ajoutes})")
    if liens(avant_o, normaliser=True) != liens(avant_t):
        erreur(f"{chemin_traduit}: liens ou images différents de l'original")


def charger_defis_originaux(module):
    fichier = ORIGINE / module / "module.yml"
    if not fichier.exists():
        return []
    donnees = lire_yaml(fichier)
    ids = [c["id"] for c in donnees.get("challenges", []) or []]
    ids += [r["id"] for r in donnees.get("resources", []) or [] if r.get("type") == "challenge"]
    return ids


def verifier_structure():
    dojo_origine = lire_yaml(ORIGINE / "dojo.yml")
    dojo_fr = lire_yaml(RACINE / "dojo.yml")

    if dojo_fr.get("id") != "linux-luminarium-fr":
        erreur("dojo.yml: id attendu linux-luminarium-fr")
    if dojo_fr.get("type") != "hidden":
        erreur("dojo.yml: type attendu hidden")
    if not dojo_fr.get("name"):
        erreur("dojo.yml: nom manquant")
    if dojo_fr.get("import", {}).get("dojo") != "linux-luminarium":
        erreur("dojo.yml: import de niveau dojo absent ou différent de linux-luminarium")

    ids_origine = [m["id"] for m in dojo_origine["modules"]]
    ids_fr = [m["id"] for m in dojo_fr["modules"]]
    if ids_origine != ids_fr:
        erreur(f"dojo.yml: modules différents ou dans un autre ordre (attendu {ids_origine}, obtenu {ids_fr})")

    for module in dojo_fr["modules"]:
        identifiant = module["id"]
        if module.get("import", {}).get("module") != identifiant:
            erreur(f"dojo.yml: le module {identifiant} n'importe pas le module d'origine du même identifiant")

        dossier = RACINE / identifiant
        if not (dossier / "module.yml").exists():
            continue

        donnees = lire_yaml(dossier / "module.yml")
        defis_fr = [r for r in donnees.get("resources", []) if r.get("type") == "challenge"]
        ids_defis_fr = [r["id"] for r in defis_fr]
        ids_defis_origine = charger_defis_originaux(identifiant)
        if ids_defis_fr != ids_defis_origine:
            erreur(f"{identifiant}/module.yml: défis différents de l'original (attendu {ids_defis_origine}, obtenu {ids_defis_fr})")

        for defi in defis_fr:
            imp = defi.get("import", {})
            if imp != {"dojo": "linux-luminarium", "module": identifiant, "challenge": defi["id"]}:
                erreur(f"{identifiant}/module.yml: import du défi {defi['id']} incorrect : {imp}")
            if not defi.get("name"):
                erreur(f"{identifiant}/module.yml: nom manquant pour le défi {defi['id']}")

        origine_module = lire_yaml(ORIGINE / identifiant / "module.yml")
        lectures_o = [r for r in origine_module.get("resources", []) if r.get("type") == "lecture"]
        lectures_t = [r for r in donnees.get("resources", []) if r.get("type") == "lecture"]
        if [(r.get("video"), r.get("playlist"), r.get("slides")) for r in lectures_o] != \
           [(r.get("video"), r.get("playlist"), r.get("slides")) for r in lectures_t]:
            erreur(f"{identifiant}/module.yml: vidéos, playlists ou diapositives différentes de l'original")

        if not donnees.get("name"):
            erreur(f"{identifiant}/module.yml: nom de module manquant")


def verifier_textes():
    for module in lire_yaml(RACINE / "dojo.yml")["modules"]:
        identifiant = module["id"]
        dossier = RACINE / identifiant
        if not (dossier / "DESCRIPTION.md").exists():
            continue

        origine_module = ORIGINE / identifiant
        verifier_texte(origine_module / "DESCRIPTION.md", dossier / "DESCRIPTION.md")
        if MARQUEUR_FICHE not in (dossier / "DESCRIPTION.md").read_text(encoding="utf-8"):
            avertissements.append(f"{identifiant}/DESCRIPTION.md: pas de fiche de cours (ajout facultatif)")

        for defi in charger_defis_originaux(identifiant):
            fichier_fr = dossier / defi / "DESCRIPTION.md"
            fichier_origine = origine_module / defi / "DESCRIPTION.md"
            if not fichier_fr.exists():
                erreur(f"{identifiant}/{defi}/DESCRIPTION.md: fichier de traduction absent")
                continue
            if fichier_origine.exists():
                verifier_texte(fichier_origine, fichier_fr)
            else:
                erreur(f"{identifiant}/{defi}: pas de DESCRIPTION.md dans l'original")

    for fichier in ["README.md", "GLOSSAIRE.md", "DESCRIPTION.md", "LICENSE"]:
        if not (RACINE / fichier).exists():
            erreur(f"{fichier}: absent")
    for fichier in ["DESCRIPTION.md", "README.md", "GLOSSAIRE.md"]:
        if (RACINE / fichier).exists():
            verifier_tirets(fichier, (RACINE / fichier).read_text(encoding="utf-8"))
    for fichier in RACINE.rglob("*.yml"):
        if "sources" in fichier.parts:
            continue
        verifier_tirets(fichier.relative_to(RACINE), fichier.read_text(encoding="utf-8"))

    gitignore = (RACINE / ".gitignore")
    if not gitignore.exists() or "sources/" not in gitignore.read_text(encoding="utf-8").split():
        erreur(".gitignore: la ligne sources/ est absente")


def main():
    if not ORIGINE.exists():
        print(f"Dojo d'origine absent : {ORIGINE}")
        return 1
    verifier_structure()
    verifier_textes()

    for message in avertissements:
        print(f"AVERTISSEMENT  {message}")
    for message in erreurs:
        print(f"ERREUR         {message}")
    print(f"{len(erreurs)} erreur(s), {len(avertissements)} avertissement(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
