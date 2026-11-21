Pauvre Zardus ; vous l'avez bien malmené.
Mais il s'est rendu compte du danger et a sécurisé son répertoire personnel !
Partie terminée ?

Pas tout à fait !
Lorsque plusieurs comptes existent sur une même machine, on pense souvent peu aux données que _les invocations de commandes_ laissent fuiter.
Rappelez-vous que la commande `ps aux` affiche :

```
hacker@dojo:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
hacker         1  0.0  0.0   1128     4 ?        Ss   05:34   0:00 /sbin/docker-init -- /bin/sleep 6h
hacker         7  0.0  0.0   2736   580 ?        S    05:34   0:00 /bin/sleep 6h
hacker       102  0.4  0.0 723944 64660 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       138  3.3  0.0 968792 106272 ?       Sl   05:34   0:07 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       287  0.0  0.0 717648 53136 ?        Sl   05:34   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       318  3.3  0.0 977472 98256 ?        Sl   05:34   0:06 /usr/lib/code-server/lib/node --dns-result-order=
hacker       554  0.4  0.0 650560 55360 ?        Rl   05:35   0:00 /usr/lib/code-server/lib/node /usr/lib/code-serve
hacker       571  0.0  0.0   4600  4032 pts/0    Ss   05:35   0:00 /usr/bin/bash --init-file /usr/lib/code-server/li
hacker      1172  0.0  0.0   5892  2924 pts/0    R+   05:38   0:00 ps aux
hacker@dojo:~$
```

Mais que se passerait-il si l'un des arguments de l'une de ces commandes était une donnée sensible, comme le flag ou un mot de passe ?
Cela arrive, et des utilisateurs malveillants partageant la même machine (ou pouvant lister les processus d'une manière ou d'une autre) peuvent voler ces données et s'en servir !

C'est ce que ce défi explore.
Zardus utilise un script d'automatisation, auquel il passe le mot de passe de son compte en argument.
Zardus est aussi autorisé à utiliser `sudo` (et donc à faire `sudo cat /flag` !).
Volez le mot de passe, connectez-vous au compte de Zardus (rappelez-vous la commande `su` du module [Démêler les utilisateurs](https://pwn.college/linux-luminarium-fr/users)), et obtenez ce flag !
