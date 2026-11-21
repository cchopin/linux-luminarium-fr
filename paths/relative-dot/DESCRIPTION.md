Jusqu'ici, nos chemins relatifs étaient « nus » : ils indiquaient directement le répertoire dans lequel descendre à partir du répertoire courant.
Dans ce niveau, on explore des chemins relatifs plus explicites.

Sous la plupart des systèmes d'exploitation, dont Linux, chaque répertoire possède deux entrées implicites qu'on peut utiliser dans les chemins : `.` et `..`.
La première, `.`, désigne le répertoire lui-même. Les chemins absolus suivants sont donc tous identiques :

- `/challenge`
- `/challenge/.`
- `/challenge/./././././././././`
- `/./././challenge/././`

Les chemins relatifs suivants sont également tous identiques :

- `challenge`
- `./challenge`
- `./././challenge`
- `challenge/.`

Bien sûr, si le répertoire de travail courant est `/`, les chemins relatifs ci-dessus sont équivalents aux chemins absolus ci-dessus.

Ce défi permet de s'entraîner à utiliser `.` dans les chemins relatifs.
Le répertoire de travail courant doit être `/`, et le chemin relatif utilisé pour lancer le défi doit commencer par `.`.
À nous de jouer !
