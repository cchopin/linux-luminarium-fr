On a repris des processus au _premier plan_ avec la commande `fg`.
On peut aussi reprendre des processus en _arrière-plan_ avec la commande `bg` !
Le processus peut ainsi continuer à tourner, tout en rendant le shell disponible pour lancer d'autres commandes.

Le `run` de ce niveau veut voir une autre copie de lui-même, _non suspendue_, qui utilise le même terminal.
Comment faire ?
Lancer le programme depuis le terminal, puis le suspendre, puis le passer en arrière-plan avec `bg`, et lancer une autre copie pendant que la première tourne en arrière-plan !

---

**Pour aller plus loin :**
Pour les détails, on peut observer les différences entre les propriétés des processus suspendus et des processus en arrière-plan !
Voici une démonstration.
D'abord, suspendons un `sleep` :

```console
hacker@dojo:~$ sleep 1337
^Z
[1]+  Stopped                 sleep 1337
hacker@dojo:~$
```

Le processus `sleep` est maintenant _suspendu_ en arrière-plan.
On peut le voir avec `ps`, en affichant la colonne `stat` grâce à l'option `-o` :

```console
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 T    sleep 1337
hacker       782 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$ 
```

Repérons ce `T` !
Il signifie que le processus est suspendu à cause de notre `Ctrl-Z`.
Le `S` dans la colonne `STAT` de `bash` signifie que `bash` est en sommeil, en attente d'une saisie.
Le `R` de la commande `ps` signifie qu'elle est en cours d'exécution, et le `+` qu'elle est au premier plan !

Observons ce qui se passe quand on reprend `sleep` en arrière-plan :

```console
hacker@dojo:~$ bg
[1]+ sleep 1337 &
hacker@dojo:~$ ps -o user,pid,stat,cmd
USER         PID STAT CMD
hacker       702 Ss   bash
hacker       762 S    sleep 1337
hacker      1224 R+   ps -o user,pid,stat,cmd
hacker@dojo:~$
```

Voilà !
Le `sleep` affiche maintenant un `S`.
Il est en sommeil, puisqu'il attend, mais il n'est pas suspendu !
Il est aussi en _arrière-plan_, et n'a donc pas de `+`.
