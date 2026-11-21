L'une des commandes Linux les plus importantes est `cat`.
`cat` sert surtout à lire le contenu de fichiers, comme ceci :

```console
hacker@dojo:~$ cat /path/to/file
Hello Hackers!
```

`cat` peut concaténer (d'où son nom) plusieurs fichiers lorsqu'on lui en donne plusieurs en arguments.
Par exemple :

```console
hacker@dojo:~$ cat myfile
This is my file!
hacker@dojo:~$ cat yourfile
This is your file!
hacker@dojo:~$ cat myfile yourfile
This is my file!
This is your file!
hacker@dojo:~$ cat myfile yourfile myfile
This is my file!
This is your file!
This is my file!
```

Enfin, si l'on ne donne aucun argument, `cat` lit l'entrée saisie dans le terminal et la renvoie.
On verra cela dans des défis ultérieurs...

Dans ce défi, le flag est copié dans le fichier `flag` du répertoire personnel (là où commence le shell).
Il faut le lire avec `cat` !
