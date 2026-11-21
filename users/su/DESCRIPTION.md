Il n'y a pas que les pirates qui ont besoin de devenir `root`.
Très souvent, le propriétaire d'un ordinateur doit lui aussi utiliser les droits `root` pour l'administrer.
Devenir `root` est une action courante pour les utilisateurs de Linux, et deux utilitaires existent pour cela : `su` et `sudo`.

Ce défi présente le plus ancien des deux, `su` (pour **s**ubstitute **u**ser, « changer d'utilisateur »).
On ne s'en sert plus guère pour passer `root`, mais c'est un outil élégant, issu d'une époque plus civilisée, et on commence donc par lui.

`su` est un binaire setuid :

```console
hacker@dojo:~$ ls -l /usr/bin/su
-rwsr-xr-x 1 root root 232416 Dec 1 11:45 /usr/bin/su
hacker@dojo:~$
```

Parce que le bit SUID est positionné, `su` s'exécute avec les droits de `root`.
Ainsi exécuté, il peut lancer un shell `root` !
Bien sûr, `su` n'est pas sans contrôle : avant d'accorder les droits `root`, il vérifie que l'utilisateur connaît le mot de passe de `root` :

```console
hacker@dojo:~$ su
Password: 
su: Authentication failure
hacker@dojo:~$
```

C'est ce contrôle par mot de passe `root` qui rend `su` obsolète.
Les systèmes modernes ont très rarement un mot de passe `root`, et d'autres mécanismes, que nous verrons plus tard, accordent les droits d'administration.

Mais CE défi (et seulement lui) possède bien un mot de passe `root`.
Ce mot de passe est `hack-the-planet`. Il faut le fournir à `su` pour devenir `root` !
Il ne reste plus qu'à le faire, puis à lire le flag !
