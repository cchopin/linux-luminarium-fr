Essayons la même chose avec `tmux` !

`tmux` (multiplexeur de terminal) est le cousin plus jeune et plus moderne de screen.
Il fait exactement les mêmes choses, avec d'autres combinaisons de touches.
La plus grande différence ?
Au lieu de `Ctrl-A`, tmux utilise `Ctrl-B` comme préfixe de commande.

Pour se détacher de tmux, on appuie donc sur `Ctrl-B`, puis sur `d`.

```console
hacker@dojo:~$ tmux
[doing some work...]
[Press Ctrl-B, then d]
[detached (from session 0)]
hacker@dojo:~$ 
```

Les commandes diffèrent aussi :
- `tmux ls` : lister les sessions
- `tmux attach` ou `tmux a` : se rattacher à une session

Pour ce défi :
1. Lancer tmux.
2. S'en détacher.
3. Exécuter `/challenge/run` (cela envoie le flag dans la session détachée !).
4. Se rattacher pour récupérer sa récompense.
