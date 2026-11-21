Dans ce niveau, on découvre les guillemets.
Les espaces ont une signification particulière dans le shell, et il existe des endroits où on ne peut pas les utiliser n'importe comment.
Rappelons notre affectation de variable :

```console
hacker@dojo:~$ VAR=1337
```

Elle affecte la valeur `1337` à la variable `VAR`, mais que faire pour lui affecter la valeur `1337 SAUCE` ?
On pourrait essayer :

```console
hacker@dojo:~$ VAR=1337 SAUCE
```

Cela semble correct, mais ça ne fonctionne pas, pour des raisons similaires à celles qui interdisent les espaces autour du `=`.
Quand le shell rencontre un espace, il termine l'affectation de variable et interprète le mot suivant (`SAUCE` dans ce cas) comme une commande.
Pour affecter `1337 SAUCE` à `VAR`, il faut *mettre entre guillemets* cette valeur :

```console
hacker@dojo:~$ VAR="1337 SAUCE"
```

Ici, le shell lit `1337 SAUCE` comme un seul mot, et affecte volontiers cette valeur à `VAR`.
Dans ce niveau, il faut affecter la valeur `COLLEGE YEAH` à la variable `PWN`.
Bonne chance !
