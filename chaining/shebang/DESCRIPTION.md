On est bien engagé sur la voie du script shell !
Mais jusqu'ici, les scripts ne peuvent être lancés que depuis le shell.
Tout fonctionnait au niveau précédent parce qu'on lançait le script depuis le shell `bash`, mais cela ne marchera plus si le script est lancé par un programme écrit en Python (ou dans un autre langage).

Quand un programme est lancé sous Linux, le noyau examine d'abord le fichier pour déterminer comment l'exécuter.
Il ne se fie *pas* à l'extension (c'est pourquoi on n'est pas obligé de nommer ses scripts shell avec `.sh`, ni ses scripts Python avec `.py`, etc.).
Linux regarde plutôt les premiers octets du fichier pour obtenir cette information.

Il existe plusieurs types de programmes, mais si le fichier commence par les caractères `#!` (appelés en anglais « [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) »), Linux traite le fichier comme un *programme interprété*, et le reste de la ligne comme le chemin de l'*interpréteur*.
Il lance alors l'interpréteur avec le chemin du fichier comme seul argument.

Prenons ce script shell :

```bash
#!/bin/bash

echo "Hello Hackers!"
```

On peut l'exécuter ainsi :

```console
hacker@dojo:~$ chmod a+x script.sh
hacker@dojo:~$ ./script.sh
Hello Hackers!
hacker@dojo:~$
```

Quand `./script.sh` est exécuté, Linux ouvre le fichier, lit la première ligne, extrait `/bin/bash` comme interpréteur, puis exécute `/bin/bash ./script.sh` pour lancer le script !

Attention : la ligne de shebang doit être la TOUTE PREMIÈRE ligne du fichier, sans ligne vide ni espace avant elle !

Pour ce défi, il faut créer un script `/home/hacker/solve.sh` avec un shebang correct, qui affiche « hack the planet ».
Ne pas oublier de le rendre exécutable, puis de lancer `/challenge/run` pour vérifier que le script fonctionne !

----
**ANECDOTE :**
Quelques shebangs courants :
- `#!/bin/bash` pour les scripts bash
- `#!/usr/bin/python3` pour les scripts Python
- `#!/bin/sh` pour les scripts shell POSIX : c'est un ancêtre plus primitif de `bash`, avec moins de fonctionnalités, mais une meilleure compatibilité avec les systèmes non Linux !
