Les instructions `if` vues jusqu'ici traitent des cas précis. Et tous les autres ?
C'est là qu'intervient `else` !

La clause `else` s'exécute lorsque la condition du `if` est fausse :

```bash
if [ "$1" == "hello" ]
then
    echo "Hi there!"
else
    echo "I don't understand"
fi
```

Le `else` n'a pas de condition : il attrape tout ce qui n'a pas été reconnu auparavant.
Il n'a pas non plus de `then`.
Enfin, le `fi` vient après le bloc `else` pour marquer la fin de l'ensemble de l'instruction !
Le `else` est facultatif : il n'était pas nécessaire au niveau précédent, et on ne l'utilise que si la logique à écrire l'exige.

Voici un exemple concret :

```bash
if [ "$1" == "start" ]
then
    echo "Starting the service..."
else
    echo "Unknown command. Use 'start' to begin."
fi
```

Pour ce défi, il faut écrire un script `/home/hacker/solve.sh` qui :

- Prend un argument
- Si l'argument vaut « pwn », affiche « college »
- Pour toute autre entrée, affiche « nope »

Exemple :

```console
hacker@dojo:~$ bash /home/hacker/solve.sh pwn
college
hacker@dojo:~$ bash /home/hacker/solve.sh hack
nope
hacker@dojo:~$ bash /home/hacker/solve.sh anything
nope
hacker@dojo:~$
```

Une fois le script fonctionnel, il ne reste plus qu'à lancer `/challenge/run` pour obtenir le flag !
