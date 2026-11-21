Nous savons désormais lister, lire et créer des fichiers.
Mais comment les retrouver ?
On utilise la commande `find` !

La commande `find` accepte des arguments facultatifs qui décrivent les critères de recherche et le lieu de recherche.
Si l'on ne précise aucun critère, `find` retient tous les fichiers.
Si l'on ne précise aucun lieu, `find` utilise le répertoire de travail courant (`.`).
Par exemple :

```console
hacker@dojo:~$ mkdir my_directory
hacker@dojo:~$ mkdir my_directory/my_subdirectory
hacker@dojo:~$ touch my_directory/my_file
hacker@dojo:~$ touch my_directory/my_subdirectory/my_subfile
hacker@dojo:~$ find
.
./my_directory
./my_directory/my_subdirectory
./my_directory/my_subdirectory/my_subfile
./my_directory/my_file
hacker@dojo:~$
```

Et en précisant le lieu de recherche :

```console
hacker@dojo:~$ find my_directory/my_subdirectory
my_directory/my_subdirectory
my_directory/my_subdirectory/my_subfile
hacker@dojo:~$
```

Bien sûr, on peut aussi préciser le critère !
Par exemple, ici, on filtre par nom :

```console
hacker@dojo:~$ find -name my_subfile
./my_directory/my_subdirectory/my_subfile
hacker@dojo:~$ find -name my_subdirectory
./my_directory/my_subdirectory
hacker@dojo:~$
```

On peut chercher dans tout le système de fichiers :

```console
hacker@dojo:~$ find / -name hacker
/home/hacker
hacker@dojo:~$
```

À notre tour.
Le flag est caché dans un répertoire quelconque du système de fichiers, toujours sous le nom `flag`.
Il faut le trouver !

Quelques remarques. D'abord, d'autres fichiers portent le nom `flag` sur le système de fichiers.
Ne pas s'inquiéter si le premier essayé ne contient pas le vrai flag.
Ensuite, beaucoup d'emplacements du système de fichiers sont inaccessibles à un utilisateur normal.
`find` produira alors des erreurs, qu'on peut ignorer : le flag n'est pas caché à cet endroit !
Enfin, `find` peut prendre du temps : un peu de patience !
