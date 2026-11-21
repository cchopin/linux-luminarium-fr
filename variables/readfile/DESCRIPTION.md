Souvent, quand on veut lire un fichier dans une variable d'environnement, on écrit quelque chose comme :

```console
hacker@dojo:~$ echo "test" > some_file
hacker@dojo:~$ VAR=$(cat some_file)
hacker@dojo:~$ echo $VAR
test
```

Cela fonctionne, mais cela correspond à ce que les hackers grincheux appellent un ["Useless Use of Cat"](https://porkmail.org/era/unix/award#cat) (un usage inutile de cat).
Lancer un programme entier juste pour lire un fichier est un gaspillage.
On peut en fait se servir des capacités du shell lui-même !

On a déjà vu `read` pour lire une saisie dans une variable.
On a aussi déjà redirigé des fichiers vers l'entrée de commandes !
En combinant les deux, on peut lire des fichiers avec le shell.

```console
hacker@dojo:~$ echo "test" > some_file
hacker@dojo:~$ read VAR < some_file
hacker@dojo:~$ echo $VAR
test
```

Que s'est-il passé ?
L'exemple redirige `some_file` vers l'*entrée standard* de `read`, si bien que lorsque `read` lit dans `VAR`, il lit en fait le fichier !
Il faut maintenant utiliser cette technique pour lire `/challenge/read_me` dans la variable d'environnement `PWN`, et l'on obtiendra le flag !
Le contenu de `/challenge/read_me` change sans cesse : il faut donc le lire directement dans la variable `PWN`, en une seule commande !
