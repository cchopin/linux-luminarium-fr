Apprenons à naviguer entre les fenêtres de tmux !

Comme screen, tmux possède des fenêtres.
Les combinaisons de touches diffèrent, mais le principe est le même :

- `Ctrl-B c` : créer une nouvelle fenêtre
- `Ctrl-B n` : fenêtre suivante
- `Ctrl-B p` : fenêtre précédente
- `Ctrl-B 0` à `Ctrl-B 9` : aller à la fenêtre 0 à 9
- `Ctrl-B w` : afficher un sélecteur de fenêtres pratique

Tmux affiche les fenêtres en bas, dans une barre d'état qui ressemble à ceci :
```
[0] 0:bash* 1:bash
```

L'étoile `*` indique la fenêtre courante, et chaque entrée montre aussi le processus avec lequel la fenêtre a été créée.

Une session tmux a été préparée avec deux fenêtres :
- La fenêtre 0 contient le flag !
- La fenêtre 1 contient un message de bienvenue.

Il ne reste plus qu'à récupérer le flag !
