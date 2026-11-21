Un type courant de caractères à supprimer est le séparateur de ligne.
Cela arrive quand on dispose d'un flux de données qu'on veut transformer en une seule ligne pour le traiter ensuite.
On peut indiquer un retour à la ligne presque comme n'importe quel autre caractère, en le _protégeant_ par une séquence d'échappement :

```console
hacker@dojo:~$ echo "hello_world!" | tr _ "\n"
hello
world!
hacker@dojo:~$
```

Ici, la barre oblique inversée (`\`) indique que le caractère qui la suit remplace un caractère difficile à saisir normalement dans le shell.
Le retour à la ligne est difficile à saisir, puisque la touche `Enter` lance la commande elle-même.
`\n` le représente, et il _doit_ être entre guillemets pour empêcher l'interpréteur du shell de le traiter lui-même et de le transmettre à `tr`.

Combinons maintenant avec la suppression.
Dans ce défi, on a injecté plein de retours à la ligne dans le flag.
Il faut les supprimer avec l'option `-d` de `tr` et la notation _échappée_ du retour à la ligne !

----
**Anecdote :**
Pour remplacer _vraiment_ un caractère barre oblique inversée (`\`) ?
Comme `\` est le caractère d'échappement, il faut l'échapper !
`\\` sera interprété par `tr` comme une barre oblique inversée.
Ce n'est pas utile pour ce défi, mais c'est une anecdote amusante.
