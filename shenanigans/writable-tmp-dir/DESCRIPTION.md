Zardus est devenu prudent !
Fini le partage du répertoire personnel : malgré le confort moindre, Zardus partage désormais `/tmp/collab`.
Il a rendu ce répertoire accessible en écriture à tous et a commencé une liste de commandes malveillantes à retenir !

```console
zardus@dojo:~$ mkdir /tmp/collab
zardus@dojo:~$ chmod a+w /tmp/collab
zardus@dojo:~$ echo "rm -rf /" > /tmp/collab/evil-commands.txt
```

Dans ce défi, lorsque vous lancez `/challenge/victim`, Zardus ajoute `cat /flag` à cette liste de commandes :

```console
hacker@dojo:~$ /challenge/victim

Username: zardus
Password: **********
zardus@dojo:~$ echo "cat /flag" >> /tmp/collab/evil-commands.txt
zardus@dojo:~$ exit
logout

hacker@dojo:~$
```

Rappelez-vous le niveau précédent : puisque `hacker` a un accès en écriture à `/tmp/collab`, il peut remplacer le fichier `evil-commands.txt`.
Rappelez-vous aussi, dans [Comprendre les commandes](https://pwn.college/linux-luminarium-fr/commands), que les fichiers peuvent _pointer_ vers d'autres fichiers.
Que se passe-t-il si `hacker` remplace `evil-commands.txt` par un lien symbolique vers un fichier sensible dans lequel `zardus` peut écrire ?
Le chaos et les bêtises !

Vous _connaissez_ le fichier vers lequel pointer.
Réalisez l'attaque et obtenez `/flag` (que, pour ce niveau, Zardus peut de nouveau lire !).

----
**INDICE :**
Il faut lancer `/challenge/victim` deux fois : une fois pour faire écrire `cat /flag` là où vous le voulez, puis une fois pour le déclencher !

**`/tmp` est-il dangereux à utiliser ?**
Malgré l'attaque présentée ici, `/tmp` peut être utilisé sans risque.
Le répertoire _est accessible en écriture à tous_, mais il a un bit de permission spécial :

```console
hacker@dojo:~$ ls -ld /tmp
drwxrwxrwt 29 root root 1056768 Jun  6 14:06 /tmp
hacker@dojo:~$
```

Ce `t` à la fin est le _bit sticky_ (sticky bit).
Il signifie que, dans ce répertoire, seuls les propriétaires des fichiers peuvent les renommer ou les supprimer.
Il a été conçu précisément pour empêcher cette attaque !
Le problème de ce défi, bien sûr, était que Zardus n'avait pas activé le bit sticky sur `/tmp/collab`.
Cela aurait fermé la faille dans ce cas précis :

```console
zardus@dojo:~$ chmod +t /tmp/collab
```

Bien sûr, les ressources partagées comme les répertoires accessibles en écriture à tous restent dangereuses.
Beaucoup plus tard, dans les [conditions de concurrence](https://pwn.college/system-security/race-conditions) du contenu Green Belt, vous verrez de nombreuses façons dont ces ressources peuvent poser des problèmes de sécurité !
