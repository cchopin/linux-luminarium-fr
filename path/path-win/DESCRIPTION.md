D'accord, les choses cassent quand on vide `PATH`.
Mais que peut-on faire d'_utile_ avec `PATH` ?

Voyons comment ajouter un nouveau répertoire de programmes à notre répertoire de commandes.
Rappelons que `PATH` contient une liste de répertoires où chercher les commandes. Pour les commandes situées ailleurs, il faut en général les exécuter par leur chemin :

```console
hacker@dojo:~$ ls /home/hacker/scripts
goodscript	badscript	okayscript
hacker@dojo:~$ goodscript
bash: goodscript: command not found
hacker@dojo:~$ /home/hacker/scripts/goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

Si l'on garde des scripts utiles et qu'on veut les lancer par leur simple nom, c'est pénible.
Pourtant, en ajoutant des répertoires à cette liste, ou en en remplaçant, on rend ces programmes accessibles par leur simple nom !
Par exemple :

```console
hacker@dojo:~$ PATH=/home/hacker/scripts
hacker@dojo:~$ goodscript
YEAH! This is the best script!
hacker@dojo:~$
```

Passons à la pratique.
Le programme `/challenge/run` de ce défi lance la commande `win` par son simple nom, mais cette commande se trouve dans le répertoire `/challenge/more_commands/`, qui n'est pas dans `PATH` au départ.
La commande `win` est la _seule_ chose dont `/challenge/run` a besoin : il suffit donc de remplacer `PATH` par ce seul répertoire.
Bonne chance !
