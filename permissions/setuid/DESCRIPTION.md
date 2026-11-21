Comme on l'a vu dans le module précédent, il existe de nombreux cas où des utilisateurs qui ne sont pas `root` ont besoin d'un accès élevé pour effectuer certaines tâches système.
L'administrateur du système ne peut pas être là pour donner le mot de passe chaque fois qu'un utilisateur veut accomplir une tâche réservée à `root` ou aux utilisateurs de `sudo`.
Le bit de permission « Set User ID » (SUID) permet donc à l'utilisateur d'exécuter un programme avec les droits du propriétaire de son fichier.

C'est précisément le mécanisme qui permet aux programmes de défi de lire le flag, et, en dehors de pwn.college, aux outils d'administration système comme `su`, `sudo` et autres.
Les permissions d'un fichier avec SUID ressemblent à ceci :

```console
hacker@dojo:~$ ls -l /usr/bin/sudo
-rwsr-xr-x 1 root root 232416 Dec 1 11:45 /usr/bin/sudo
hacker@dojo:~$
```

La lettre `s` à la place du bit d'exécution signifie que le programme est exécutable *avec SUID*.
Cela veut dire que, quel que soit l'utilisateur qui lance le programme (du moment qu'il en a le droit d'exécution), le programme s'exécute avec les droits de son propriétaire (ici, l'utilisateur `root`).

En tant que propriétaire d'un fichier, on peut positionner son bit SUID avec chmod :

```
chmod u+s [program]
```

Attention, cependant !
Donner le bit SUID à un exécutable appartenant à `root` peut offrir à un attaquant un moyen de devenir `root`.
On en apprendra davantage [dans le module sur le mauvais usage des programmes](https://pwn.college/fundamentals/program-misuse/).

Dans ce niveau, on va ajouter le bit SUID au programme `/challenge/getroot`, afin de lancer un shell `root` et de lire soi-même le flag avec `cat` !
