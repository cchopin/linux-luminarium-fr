On a peut-être remarqué que certaines commandes affichent des données dans le terminal quand on les lance.
Jusqu'ici, cela a surtout affiché des flags, mais la technique est bien plus profonde.
Les mécanismes qui gèrent l'entrée et la sortie en ligne de commande font une grande partie de la puissance du terminal.

Ce module explique la *redirection d'entrée et de sortie*.
En bref, chaque processus sous Linux dispose de trois canaux de communication standard :

- L'*entrée standard* est le canal par lequel le processus reçoit ses données. Par exemple, le shell utilise l'entrée standard pour lire les commandes que l'on tape.
- La *sortie standard* est le canal par lequel le processus envoie ses données normales, comme le flag affiché dans les défis précédents, ou la sortie de programmes comme `ls`.
- L'*erreur standard* est le canal par lequel le processus envoie les détails d'erreur. Par exemple, si l'on tape mal une commande, le shell indique sur l'erreur standard que cette commande n'existe pas.

Comme ces trois canaux sont très utilisés sous Linux, on les désigne par des noms plus courts : `stdin`, `stdout` et `stderr`.
Ce module apprend à rediriger, enchaîner, bloquer et manipuler ces canaux.
Bonne chance !
