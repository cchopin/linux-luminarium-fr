Nous savons créer des fichiers.
Et des répertoires ?
On crée des **r**épertoires avec la commande `mkdir` (pour **m**a**k**e **dir**ectory), puis on peut y ranger des fichiers !

Regardons :

```console
hacker@dojo:~$ cd /tmp
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ ls
hacker@dojo:/tmp$ mkdir my_directory
hacker@dojo:/tmp$ ls
my_directory
hacker@dojo:/tmp$ cd my_directory
hacker@dojo:/tmp/my_directory$ touch my_file
hacker@dojo:/tmp/my_directory$ ls
my_file
hacker@dojo:/tmp/my_directory$ ls /tmp/my_directory/my_file
/tmp/my_directory/my_file
hacker@dojo:/tmp/my_directory$
```

Maintenant, il faut créer un répertoire `/tmp/pwn` et y créer un fichier `college` !
Puis lancer `/challenge/run`, qui vérifie la solution et donne le flag.
