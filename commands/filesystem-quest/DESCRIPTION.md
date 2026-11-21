Avec `cd`, `ls` et `cat`, nous sommes prêts pour un petit jeu !

On commence dans `/`.
Normalement :

```console
hacker@dojo:~$ cd /
hacker@dojo:/$ ls
bin   challenge  etc   home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  dev        flag  lib   lib64  media   opt  root  sbin  sys  usr
```

Le contenu est abondant !
Avec le temps, on le connaîtra très bien, mais on reconnaît déjà le fichier `flag` et le répertoire `challenge`.

Dans ce défi, le flag est caché !
Il faut suivre les indices avec `ls` et `cat` pour le trouver.
Voici le déroulement :

0. Le premier indice se trouve dans `/`. Aller y voir.
1. Regarder le contenu avec `ls`. Il y aura un fichier nommé HINT, CLUE ou quelque chose de semblable !
2. Lire ce fichier avec `cat` pour connaître l'indice !
3. Selon l'indice, aller dans le répertoire suivant (ou ne pas y aller !).
4. Suivre les indices jusqu'au flag !

Bonne chance !
