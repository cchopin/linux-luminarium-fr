Essayons quelque chose d'un peu plus délicat !
On a déjà envoyé la sortie d'un programme vers un autre avec `|`, mais jusqu'ici, il s'agissait toujours de relier la sortie d'une commande à l'entrée d'une autre.
Et si l'on voulait envoyer la sortie de plusieurs programmes vers une seule commande ?
Il existe plusieurs façons de le faire ; on en explore une ici : rediriger la sortie du script lui-même !

Pour le shell, un script n'est qu'une commande de plus.
On peut donc rediriger son entrée et sa sortie, exactement comme pour les commandes du module [Tubes](https://pwn.college/linux-luminarium-fr/piping) !
Par exemple, on peut écrire sa sortie dans un fichier :

```console
hacker@dojo:~$ cat script.sh
echo PWN
echo COLLEGE
hacker@dojo:~$ bash script.sh > output
hacker@dojo:~$ cat output
PWN
COLLEGE
hacker@dojo:~$
```

Toutes les méthodes de redirection fonctionnent : `>` pour la sortie standard, `2>` pour l'erreur standard, `<` pour l'entrée standard, `>>` et `2>>` pour l'ajout en fin de fichier, `>&` pour rediriger vers d'autres descripteurs de fichiers, et `|` pour envoyer la sortie vers une autre commande.

Dans ce niveau, on s'entraîne à envoyer la sortie du script vers un autre programme avec `|`.
Comme les scripts exécutables arrivent plus tard, on lance le script avec `bash` lorsqu'on le redirige.
Comme précédemment, il faut créer un script `.sh` qui appelle la commande `/challenge/pwn` puis la commande `/challenge/college`, et envoyer la sortie du script vers une seule invocation de la commande `/challenge/solve`.
