Essayons quelque chose de plus compliqué : une commande avec des _arguments_, c'est-à-dire des données supplémentaires transmises à la commande.
Lorsqu'on saisit une ligne de texte puis qu'on appuie sur Entrée, le shell découpe en réalité cette saisie en une commande et ses _arguments_.
Le premier mot est la commande, et les mots suivants sont les arguments.
Observons :

```console
hacker@dojo:~$ echo Hello
Hello
hacker@dojo:~$
```

Ici, la commande est `echo`, et l'argument est `Hello`.
`echo` est une commande simple qui « répète » tous ses arguments dans le terminal, comme on le voit dans la session ci-dessus.

Voyons `echo` avec plusieurs arguments :

```console
hacker@dojo:~$ echo Hello Hackers!
Hello Hackers!
hacker@dojo:~$
```

Ici, la commande est `echo`, et `Hello` ainsi que `Hackers!` sont les deux arguments transmis à `echo`.
C'est simple !

Dans ce défi, pour obtenir le flag, il faut exécuter la commande `hello` (et non la commande `echo`) avec un seul argument, `hackers`.
Essayons dès maintenant !
