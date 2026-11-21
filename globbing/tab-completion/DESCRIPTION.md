Aussi tentant que soit l'usage de `*` pour raccourcir ce qu'on tape sur la ligne de commande, il peut conduire à des erreurs.
Le motif peut développer des fichiers non voulus, et l'on ne s'en rend compte que lorsque la commande `rm` est déjà en cours d'exécution !
Personne n'est à l'abri de ce genre d'erreur.

Une alternative plus sûre, lorsqu'on veut désigner une cible précise, est la _complétion par tabulation_.
Si l'on appuie sur la touche Tab dans le shell, celui-ci essaie de deviner ce qu'on va taper et complète automatiquement.
La complétion automatique est très utile, et ce défi en explore l'usage pour désigner des fichiers.

Ce défi a copié le flag dans `/challenge/pwncollege`, et l'on peut lire ce fichier librement avec `cat`.
Mais on ne peut pas taper le nom du fichier : nous avons employé une astuce pour qu'il faille _obligatoirement_ compléter le nom par tabulation.
Essayons !

```console
hacker@dojo:~$ ls /challenge
Dockerfile  pwncollege
hacker@dojo:~$ cat /challenge/pwncollege
cat: /challenge/pwncollege: No such file or directory
hacker@dojo:~$ cat /challenge/pwn<TAB>
pwn.college{HECK YEAH}
hacker@dojo:~$
```

Lorsqu'on appuie sur la touche Tab, le nom se complète et l'on peut lire le fichier.
Bonne chance !
