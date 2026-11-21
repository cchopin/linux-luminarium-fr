Comme on redirige la _sortie_ des programmes, on peut aussi rediriger l'entrée _vers_ des programmes !
Cela se fait avec `<`, comme ceci :

```
hacker@dojo:~$ echo yo > message
hacker@dojo:~$ cat message
yo
hacker@dojo:~$ rev < message
oy
```

De nombreux programmes permettent de faire des choses intéressantes grâce à la redirection d'entrée.
Dans ce niveau, on utilise `/challenge/run`, qui exige qu'on redirige le fichier `PWN` vers lui, ce fichier devant contenir la valeur `COLLEGE` !
Pour écrire cette valeur dans le fichier `PWN`, il suffit de se rappeler le défi précédent sur la redirection de sortie avec `echo` !
