Plongeons maintenant dans la magie du _détachement_ !

Imaginons qu'on travaille sur quelque chose d'important à distance, et que la connexion tombe.
Dans un terminal ordinaire (en dehors de cet excellent environnement de dojo), tout est perdu.
Avec screen, le travail continue de tourner, et on peut le _rattacher_ plus tard !

On peut aussi se _détacher_ volontairement, ce que fait ce défi.
Pour se détacher, on appuie sur `Ctrl-A`, puis sur `d` (pour **d**etach, « détacher »).
La session continue alors de tourner en arrière-plan, pendant qu'on retrouve son terminal habituel.

```console
hacker@dojo:~$ screen
[doing some work...]
[Press Ctrl-A, then d]
[detached from 12345.pts-0.hostname]
hacker@dojo:~$ 
```

Pour se **r**attacher, on utilise l'argument `-r` de `screen` :

```console
hacker@dojo:~$ screen -r
```

Pour ce défi, il faut :

1. Lancer screen.
2. S'en détacher.
3. Exécuter `/challenge/run` (cela envoie discrètement le flag dans la session détachée !).
4. Se rattacher pour récupérer sa récompense.

----
**ANECDOTE :**
`Ctrl-A` est la touche d'activation de `screen` pour tous ses raccourcis, dans la configuration par défaut.
Toutes les fonctionnalités de `screen` s'activent avec une combinaison commençant par `Ctrl-A`.

**INDICE :**
Rappel : on maintient Ctrl et on appuie sur A, puis on relâche les deux et on appuie sur d.

**INDICE :**
Si l'on voit `[detached from...]`, c'est gagné !
