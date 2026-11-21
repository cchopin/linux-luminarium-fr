Même sans commettre d'erreur, les utilisateurs peuvent s'exposer sans le vouloir.
Par exemple, de nombreux fichiers du répertoire personnel d'un utilisateur ordinaire sont _lisibles par tous par défaut_, alors qu'ils servent souvent à stocker des informations sensibles.
Vous ne le croirez peut-être pas, mais votre `.bashrc` est lisible par tous, sauf si vous le modifiez explicitement !

```console
hacker@dojo:~$ ls -l ~/.bashrc
-rw-r--r-- 1 hacker hacker 148 Jun  7 05:56 /home/hacker/.bashrc
hacker@dojo:~$
```

On pourrait se dire : « Au moins, il n'est pas accessible en écriture à tous par défaut ! »
Mais même lisible par tous, il peut faire des dégâts.
Comme le `.bashrc` est lu par le shell au démarrage, c'est là que l'on place d'ordinaire l'initialisation des variables d'environnement qu'on veut personnaliser.
La plupart du temps, il s'agit de choses sans danger, comme `PATH`, mais il arrive qu'on y stocke des clés d'API pour y accéder facilement.
Par exemple, dans ce défi :

```
zardus@dojo:~$ echo "FLAG_GETTER_API_KEY=sk-XXXYYYZZZ" > ~/.bashrc
```

Ensuite, Zardus peut facilement se servir de la clé d'API.
Dans ce niveau, il suffit d'utiliser une clé d'API valide pour obtenir le flag :

```
zardus@dojo:~$ flag_getter --key $FLAG_GETTER_API_KEY
Correct API key! Do you want me to print the key (y/n)? y
pwn.college{HACKED}
zardus@dojo:~$
```

Naturellement, Zardus a stocké sa clé dans `.bashrc`.
Pouvez-vous voler la clé et obtenir le flag ?

----
**NOTE :**
Une fois la clé obtenue, il suffit d'exécuter `flag_getter` en tant qu'utilisateur `hacker`.
Le `/challenge/victim` de ce défi n'est là que pour l'ambiance : vous n'avez pas besoin de l'utiliser.
