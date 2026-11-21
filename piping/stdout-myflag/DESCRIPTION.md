En plus de rediriger la sortie de `echo`, on peut bien sûr rediriger la sortie de n'importe quelle commande.
Dans ce niveau, `/challenge/run` donne encore un flag, mais _seulement_ si l'on redirige sa sortie vers le fichier `myflag`.
Le flag se retrouve, bien entendu, dans le fichier `myflag` !

On remarque que `/challenge/run` continue d'afficher du texte dans le terminal, malgré la redirection de la sortie standard.
C'est parce qu'il communique ses instructions et ses retours par l'erreur standard, et qu'il n'affiche le flag que sur la sortie standard !

----
**Attention :** si une expérience précédente a laissé un fichier, un répertoire ou un lien symbolique nommé `myflag` dans le répertoire courant, il faut d'abord le supprimer, pour que le shell puisse y créer un fichier normal accessible en écriture.
