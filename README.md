# Linux Luminarium (français)

Traduction française du dojo **Linux Luminarium** de [pwn.college](https://pwn.college), une introduction en douceur à l'interface en ligne de commande de Linux.

Ce dépôt ne contient ni le code des défis, ni leurs vérifications. Ils sont importés depuis le dojo officiel `linux-luminarium`, avec les mêmes environnements, les mêmes vérifications et les mêmes flags. Seuls les textes sont traduits : noms et descriptions des dojos, modules et défis, ressources.

## Crédit et licence

- Contenu d'origine : © 2022 pwn.college, dépôt [`pwncollege/challenges`](https://github.com/pwncollege/challenges), dossier `challenges/linux-luminarium`, commit `0a4d91514c8077a5b77c25aff3ce2d6dc90c1181`.
- Le dossier source est sous licence BSD 2-Clause (fichier `LICENSE`, reproduit dans ce dépôt). Cette licence impose de conserver la notice de copyright et l'avertissement lors de toute copie ou modification : le fichier `LICENSE` doit donc rester avec les textes traduits.
- Ce dépôt ne reprend aucune vidéo ni diapositive. Les liens vers les ressources externes sont ceux de l'original.

Ce dépôt reste **privé**.

## Contenu

- `dojo.yml` : déclaration du dojo, de ses modules, et import de chacun depuis le dojo officiel `linux-luminarium`.
- `DESCRIPTION.md` : description du dojo.
- Un dossier par module, contenant `module.yml` (nom, ressources, défis) et `DESCRIPTION.md` (description du module).
- Un sous-dossier par défi, contenant `DESCRIPTION.md`.
- [GLOSSAIRE.md](GLOSSAIRE.md) : termes techniques et traductions retenues.
- `verifier.py` : contrôles automatiques (structure, code, liens, typographie).

## Installer le dojo sur pwn.college

1. Pousser ce dépôt sur GitHub (dépôt privé, branche `main`, dojo à la racine).
2. Sur pwn.college, ouvrir `/dojos/create`. Le formulaire fournit une clé de déploiement publique et privée.
3. Ajouter la clé publique dans le dépôt, à `https://github.com/<votre-compte>/linux-luminarium-fr/settings/keys` (lecture seule suffit).
4. Renseigner le dépôt au format `propriétaire/dépôt`, puis valider : la clé doit être ajoutée avant de valider, et la page ne doit pas être rechargée entre les deux étapes, car chaque rechargement génère une nouvelle clé.
5. Pour mettre à jour après un push, utiliser le bouton **Update** de la page d'administration du dojo.

Le dojo est déclaré `type: hidden` : il n'apparaît pas dans la liste publique, et seuls ses membres peuvent y accéder.

## Commit de référence

La traduction est basée sur `pwncollege/challenges`, dossier `challenges/linux-luminarium`, au commit `0a4d91514c8077a5b77c25aff3ce2d6dc90c1181`.
