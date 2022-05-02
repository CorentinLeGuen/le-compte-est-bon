# _Le Compte est Bon_ algorithm with Python


## What is _Le Compte est Bon_ ?

The goal of the game is to obtain a number (between 101 and 999 included) with basic operators (Add "+", Substract "-", Multiply "*", Divide "/") on natural integers with 6 randomly taken (on this list : 1 to 10, 25, 50, 75 and 100).\
We can have multiple times the same number (for example, 6 two times).\
If we can't find the exact result, we should find the closest.

Example :
> Numbers : 3, 100, 8, 8, 10, 6\
> Target : 683
> 
> Solution :\
> 6 * 100 = 600\
> 8 * 10 = 80\
> 600 + 80 = 680\
> 680 + 3 = 683

Another example :
> Numbers : 3, 75, 2, 4, 1, 1\
> Target : 888
>
> Solution :\
> 75 - 1 = 74\
> 3 * 4 = 12\
> 74 * 12 = 888

Here is a link with game description (in french) : [wikipedia article](https://fr.wikipedia.org/wiki/Des_chiffres_et_des_lettres#Le_Compte_est_Bon).

## Algorithms

There is 3 main algorithms :

1. **Recursive solution** : we take two by two the numbers, make the 4 operations on them and reiterate the process.
2. **Search with cache** : same as _Recursive solution_ but we store in cache all the calculs made. It's fast but high memory consumption.
3. **Random search** : can be effective, it's just the same af _Recursive solution_ but we make everythink randomly.

## Application

To launch the program: 
```shell
python3 main.py
```

You should have a result like this :

```
{'numbers': [50, 3, 7, 100, 75, 6], 'target': 592}
{'operations': ['75 - 7 = 68', '50 * 3 = 150', '150 - 68 = 82', '82 * 6 = 492', '492 + 100 = 592'], 'best': 592}
```