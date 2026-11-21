Autrefois, un système Linux typique avait un mot de passe `root`, que les administrateurs utilisaient avec `su` pour passer `root` (après s'être connectés avec le mot de passe de leur propre compte).
Mais les mots de passe `root` sont pénibles à entretenir, ils (ou plutôt leurs hachages !) peuvent fuiter, et ils se prêtent mal aux grands parcs de machines.
Pour répondre à ces problèmes, le monde est passé, au cours des dernières décennies, de l'administration avec `su` à l'administration avec `sudo`. *Anecdote* : `sudo` signifiait à l'origine **su**peruser **do** (« exécuter en superutilisateur »). Le nom s'est transformé en « su do », et comme `su` signifie « substitute user » (changer d'utilisateur), `sudo` veut aujourd'hui dire « changer d'utilisateur et agir ».

Contrairement à `su`, qui lance par défaut un shell pour l'utilisateur choisi, `sudo` exécute par défaut une commande en tant que `root` :

```console
hacker@dojo:~$ whoami
hacker
hacker@dojo:~$ sudo whoami
root
hacker@dojo:~$
```

Ou, plus utile pour récupérer des flags :

```console
hacker@dojo:~$ grep hacker /etc/shadow
grep: /etc/shadow: Permission denied
hacker@dojo:~$ sudo grep hacker /etc/shadow
hacker:$6$Xro.e7qB3Q2Jl2sA$j6xffIgWn9xIxWUeFzvwPf.nOH2NTWNJCU5XVkPuONjIC7jL467SR4bXjpVJx4b/bkbl7kyhNquWtkNlulFoy.:19921:0:99999:7:::
hacker@dojo:~$
```

Contrairement à `su`, qui repose sur un mot de passe, `sudo` vérifie des règles pour déterminer si l'utilisateur est autorisé à exécuter des commandes en tant que `root`.
Ces règles sont définies dans `/etc/sudoers`. Ce sujet dépasse en grande partie notre propos, mais de nombreuses [ressources](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file) permettent de l'approfondir.

Le monde est donc passé à `sudo`, et `su` a été laissé de côté pour l'administration système.
D'ailleurs, le mode privilégié de pwn.college fonctionne lui aussi en accordant un accès `sudo` pour élever les privilèges !

Dans ce niveau, on accorde un accès `sudo`, et il faut s'en servir pour lire le flag.
Simple et rapide !

----
**NOTE :**
Après ce niveau, on activera le mode privilégié !
Dans l'espace de travail, cliquer sur le cadenas fermé redémarre le défi en mode privilégié, et cliquer sur le cadenas ouvert revient au mode normal.
Pendant que le mode privilégié est actif, le nom d'hôte de l'invite se termine par `~practice`.
Le mode privilégié donne un accès `sudo` complet pour inspecter et déboguer, mais il fournit un flag factice qui ne peut pas être soumis.
