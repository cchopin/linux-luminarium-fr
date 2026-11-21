Vous savez donc vous passer de `cat` !
Et sans `ls` ?
Cette fois, `/challenge/check` restaurera le flag dans un fichier au nom _choisi au hasard_.
Il vous faudra le trouver sans utiliser votre commande `ls`.

Il existe de nombreuses solutions à ce défi.
`echo` est une primitive, et vous pouvez lui passer en argument un [globbing](https://pwn.college/linux-luminarium-fr/globbing) qui se développe en tous les fichiers !
Par exemple, `echo *` affiche le nom de tous les fichiers du répertoire courant.
De même, vous pouvez utiliser la complétion par tabulation (appuyez plusieurs fois sur la touche Tab) après une commande : le shell vous propose alors les fichiers possibles.

Quelle que soit la méthode, trouvez le fichier au nom aléatoire que `/challenge/check` crée dans `/` après votre `rm`, lisez-le, et obtenez le flag !
