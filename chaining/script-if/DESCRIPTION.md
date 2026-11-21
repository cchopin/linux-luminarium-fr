Maintenant que les scripts peuvent recevoir des arguments, rendons-les plus intelligents grâce aux conditions !

En bash, on peut utiliser des instructions `if` pour prendre des décisions :

```bash
if [ "$1" == "ping" ]
then
    echo "pong"
fi
```

En anglais, cela se dit `if the first argument is "ping", print out "pong"`, soit en français : « si le premier argument vaut « ping », afficher « pong » ».
La syntaxe est assez stricte, pour plusieurs raisons.
D'abord, il *faut* des espaces après `if` (c'est différent dans un langage comme C), après `[` et avant `]`.
Ensuite, `if`, `then` et `fi` doivent être sur des lignes différentes (ou séparés par des points-virgules) : on ne peut pas les regrouper dans une seule instruction.
Il y a aussi une particularité : au lieu de `endif` ou `end`, l'instruction se termine par `fi` (`if` à l'envers).
C'est une chose à retenir.

Pour ce défi, il faut écrire un script `/home/hacker/solve.sh` qui :

- Prend un argument
- Si l'argument vaut « pwn », affiche « college »
- Pour toute autre entrée, n'affiche rien

Exemple :

```console
hacker@dojo:~$ bash /home/hacker/solve.sh pwn
college
hacker@dojo:~$ bash /home/hacker/solve.sh foo
hacker@dojo:~$
```
Une fois le script fonctionnel, il ne reste plus qu'à lancer `/challenge/run` pour obtenir le flag !

----
**NOTE :**
On peut savoir quoi d'autre vérifier dans une condition, en dehors de l'égalité de chaînes ?
Tout est expliqué dans `help test` !
