Commençons par afficher des variables.
Le programme `/challenge/run` ne peut pas, et ne pourra pas, donner le flag, mais ce n'est pas grave : le flag a été placé dans la variable nommée « FLAG » !
Il suffit de demander au shell de l'afficher !

On peut procéder de plusieurs façons, mais commençons par `echo`.
Cette commande se contente d'afficher du texte.
Par exemple :

```console
hacker@dojo:~$ echo Hello Hackers!
Hello Hackers!
```

On peut aussi afficher des variables avec `echo`, en faisant précéder le nom de la variable d'un `$`.
Par exemple, la variable `PWD` contient toujours le répertoire de travail courant du shell.
On l'affiche ainsi :

```console
hacker@dojo:~$ echo $PWD
/home/hacker
```

Il est maintenant temps de s'y mettre.
Il faut faire afficher la variable `FLAG` par le shell pour résoudre ce défi !
