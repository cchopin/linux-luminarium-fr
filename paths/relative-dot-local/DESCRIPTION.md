Dans ce niveau, on s'entraîne encore à désigner des chemins avec `.`.
Ce défi demande de lancer le programme depuis le répertoire `/challenge`.
La difficulté vient de ce qui suit.

Linux évite volontairement de chercher automatiquement dans le répertoire courant lorsqu'on saisit un chemin « nu ».
Observons :

```console
hacker@dojo:~$ cd /challenge
hacker@dojo:/challenge$ run
```

Cela n'exécutera *pas* /challenge/run.
C'est une mesure de sécurité : si Linux cherchait dans le répertoire courant à chaque fois qu'on saisit un chemin nu, on pourrait exécuter par erreur des programmes du répertoire courant qui portent le même nom que des utilitaires système essentiels !
Par conséquent, les commandes ci-dessus affichent l'erreur suivante :

```
bash: run: command not found
```

On étudiera plus tard les mécanismes qui sous-tendent ce comportement. Dans ce défi, on apprend à utiliser des chemins relatifs explicites pour lancer `run` dans cette situation.
La méthode consiste à *dire* à Linux qu'on veut explicitement exécuter un programme du répertoire courant, en utilisant `.` comme dans les niveaux précédents.
Essayons !
