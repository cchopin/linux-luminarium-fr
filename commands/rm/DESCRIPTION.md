Les fichiers sont partout autour de nous.
Comme les emballages de bonbons, il finit par y en avoir trop.
Dans ce niveau, on apprend à faire du ménage !

Sous Linux, on **supprime** des fichiers (**r**e**m**ove) avec la commande `rm`, comme ceci :

```console
hacker@dojo:~$ touch PWN
hacker@dojo:~$ touch COLLEGE
hacker@dojo:~$ ls
COLLEGE     PWN
hacker@dojo:~$ rm PWN
hacker@dojo:~$ ls
COLLEGE
hacker@dojo:~$
```

Pratiquons.
Ce défi crée un fichier `delete_me` dans le répertoire personnel.
Le supprimer, puis lancer `/challenge/check`, qui vérifie la suppression et donne le flag !
