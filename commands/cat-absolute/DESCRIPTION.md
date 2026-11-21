Dans le niveau précédent, on a utilisé `cat flag` pour lire le flag dans le répertoire personnel !
On peut bien sûr donner à `cat` des arguments sous forme de chemins absolus :

```console
hacker@dojo:~$ cat /path/to/file
Hello Hackers!
```

Dans ce défi, le flag n'est pas copié dans le répertoire personnel, mais il est rendu lisible.
On peut le lire avec `cat` à son chemin absolu : `/flag`.

----
**FUN FACT:**
`/flag` est l'emplacement où le flag se trouve _toujours_ dans pwn.college. Mais, contrairement à ce défi, on ne peut en général pas accéder directement à ce fichier.
