On a vu comment utiliser un seul `if` pour vérifier une condition.
Mais que faire si l'on doit vérifier plusieurs conditions ?
On peut utiliser `elif` (contraction de `else if`) :

```bash
if [ "$1" == "one" ]
then
    echo "1"
elif [ "$1" == "two" ]
then
    echo "2"
elif [ "$1" == "three" ]
then
    echo "3"
else
    echo "unknown"
fi
```

Il faut bien un `then` après le `elif`, comme après le `if`.
Comme précédemment, le `else` final attrape tout ce qui n'a pas été reconnu.

Pour ce défi, il faut écrire un script `/home/hacker/solve.sh` qui :

- Prend un argument
- Si l'argument vaut « hack », affiche « the planet »
- Si l'argument vaut « pwn », affiche « college »
- Si l'argument vaut « learn », affiche « linux »
- Pour toute autre entrée, affiche « unknown »

Exemple :

```console
hacker@dojo:~$ bash /home/hacker/solve.sh hack
the planet
hacker@dojo:~$ bash /home/hacker/solve.sh pwn
college
hacker@dojo:~$ bash /home/hacker/solve.sh learn
linux
hacker@dojo:~$ bash /home/hacker/solve.sh foo
unknown
hacker@dojo:~$
```

Une fois le script fonctionnel, il ne reste plus qu'à lancer `/challenge/run` pour obtenir le flag !

----
**NOTE :**
En écrivant le script, il faut bien respecter les espaces des exemples.
Contrairement à beaucoup d'autres langages, bash exige que `[` et `]` soient séparés des autres caractères par des espaces, sinon il ne peut pas analyser la condition.
