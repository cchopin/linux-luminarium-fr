Sans argument, `su` lance un shell `root` (après authentification avec le mot de passe de `root`).
On peut aussi donner un nom d'utilisateur en argument, pour basculer vers *cet* utilisateur plutôt que vers `root`.
Par exemple :

```console
hacker@dojo:~$ su some-user
Password:
some-user@dojo:~$
```

Parfait !
Dans ce niveau, il faut basculer vers l'utilisateur `zardus`, puis exécuter `/challenge/run`.
Le mot de passe de `zardus` est `dont-hack-me`.
Bonne chance !
