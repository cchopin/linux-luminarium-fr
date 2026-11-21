On a vu que la substitution de processus peut faire paraître la sortie de commandes comme des fichiers à lire, avec `<(command)`.
On peut aussi l'utiliser pour _écrire_ vers des commandes !

On peut dupliquer des données vers deux fichiers avec `tee` :

```console
hacker@dojo:~$ echo HACK | tee THE > PLANET
hacker@dojo:~$ cat THE
HACK
hacker@dojo:~$ cat PLANET
HACK
hacker@dojo:~$
```

On a aussi utilisé `tee` pour dupliquer des données vers un fichier et une commande :

```console
hacker@dojo:~$ echo HACK | tee THE | cat
HACK
hacker@dojo:~$ cat THE
HACK
hacker@dojo:~$
```

Mais qu'en est-il de la duplication vers deux commandes ?
Comme le dit sa page de manuel, `tee` est conçu pour écrire vers des fichiers et vers la sortie standard :

```text
TEE(1)                           User Commands                          TEE(1)

NAME
       tee - read from standard input and write to standard output and files
```

Mais attendez ! On vient d'apprendre que bash peut faire paraître des commandes comme des fichiers, grâce à la substitution de processus !
Pour écrire vers une commande (substitution de processus en sortie), on utilise `>(command)`.
Si l'on écrit l'argument `>(rev)`, bash exécute la commande `rev` (qui lit des données sur l'entrée standard, les inverse et les écrit sur la sortie standard !), mais relie son entrée à un tube nommé temporaire.
Lorsque des commandes écrivent dans ce fichier, les données arrivent sur l'entrée standard de la commande :

```console
hacker@dojo:~$ echo HACK | rev
KCAH
hacker@dojo:~$ echo HACK | tee >(rev)
HACK
KCAH
```

Dans l'exemple ci-dessus, les événements suivants se sont produits :

1. `bash` a lancé la commande `rev`, en reliant un tube nommé (probablement `/dev/fd/63`) à son entrée standard
2. `bash` a lancé la commande `tee`, en reliant un tube à son entrée standard, et il a remplacé le premier argument de `tee` par `/dev/fd/63`. `tee` n'a jamais vu l'argument `>(rev)` : le shell l'a _substitué_ avant de lancer `tee`
3. `bash` a utilisé la commande interne `echo` pour écrire `HACK` dans l'entrée standard de `tee`
4. `tee` a lu `HACK`, l'a écrit sur la sortie standard, puis l'a écrit dans `/dev/fd/63` (relié à l'entrée standard de `rev`)
5. `rev` a lu `HACK` sur son entrée standard, l'a inversé et a écrit `KCAH` sur la sortie standard

Passons au défi !
Dans ce défi, on dispose de `/challenge/hack`, `/challenge/the` et `/challenge/planet`.
Lancer la commande `/challenge/hack`, et dupliquer sa sortie comme entrée des commandes `/challenge/the` et `/challenge/planet` !
Rappelons que `tee` peut recevoir plusieurs cibles de sortie, et que `>(command)` est l'une d'elles.
Revoir les défis précédents « Dupliquer des données avec tee » et « Substitution de processus en entrée » si l'on a besoin de rappels sur cette méthode.

----
**Anecdote !**

L'observateur attentif remarquera que les deux lignes suivantes sont équivalentes :

```console
hacker@dojo:~$ echo hi | rev
ih
hacker@dojo:~$ echo hi > >(rev)
ih
hacker@dojo:~$
```

Il existe plusieurs façons d'envoyer des données dans un tube !
La seconde est bien plus difficile à lire, et plus difficile à étendre.
Par exemple :

```console
hacker@dojo:~$ echo hi | rev | rev
hi
hacker@dojo:~$ echo hi > >(rev | rev)
hi
hacker@dojo:~$
```

C'est absurde !
Il faut retenir que la substitution de processus est un outil puissant, mais très _spécialisé_ : il ne faut pas l'utiliser pour tout.
