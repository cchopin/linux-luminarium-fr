En travaillant avec le shell, on veut souvent stocker la sortie d'une commande dans une variable.
Heureusement, le shell rend cela assez simple grâce à la [_substitution de commande_](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) (Command Substitution) !
Observons :

```console
hacker@dojo:~$ FLAG=$(cat /flag)
hacker@dojo:~$ echo "$FLAG"
pwn.college{blahblahblah}
hacker@dojo:~$
```

Élégant !
Passons à la pratique.
Il faut lire directement la sortie de la commande `/challenge/run` dans une variable nommée `PWN` : elle contiendra alors le flag !

----
**Anecdote :**
On peut aussi utiliser des guillemets inversés à la place de `$()` : `` FLAG=`cat /flag` `` au lieu de ``FLAG=$(cat /flag)`` dans l'exemple ci-dessus.
C'est un format plus ancien, qui présente quelques inconvénients.
Par exemple, imaginons qu'on veuille _imbriquer_ des substitutions de commandes.
Comment écrire `$(cat $(find / -name flag))` avec des guillemets inversés ?
La position officielle de pwn.college est d'utiliser `$(blah)` plutôt que `` `blah` ``.
