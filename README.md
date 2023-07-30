Test for m1-advanced data structures, ECI36, 2023
====================================================

# Author
Karen Araceli Palacio Pastor

karen.palacio.1994@gmail.com

# Contents

## Ejercicio 6
in build_and_search_kd_tree.py you can find the code corresponding to the implementation in python of the pseudocode given as an answer to the point number 6 of the test.

> Number 6
> Give a high-level description (but detailed enough) of the algorithm to
> find all elements in a standard K-d tree that are at (Euclidean) distance of q not
> larger than a given radius R. In your algorithm, take into account that there is no
> need to store discriminants in the nodes of the standard K-d tree; they cycle along
> any path: 0, 1, 2, . . . , K − 1, 0, 1, . . .


It runs the algorithm for the following 2D KDtree

```python
Root: (51, 75)
    Left:  (25, 40)
        Left:  (10, 30)
            Left:  (1, 10)
        Right: (35, 90)
    Right: (70, 70)
        Left:  (55, 1)
        Right: (60, 80)



\********************/
searching elements within EUCL distance of: 25
[(25, 40)]
The corresponding distances are:
[25.0]

\********************/
searching elements within EUCL distance of: 30
[(51, 75), (25, 40), (35, 90)]

The corresponding distances are:
[27.85677655436824, 25.0, 26.92582403567252]

\********************/
searching elements within EUCL distance of: 40
[(51, 75), (25, 40), (10, 30), (35, 90), (60, 80)]

The corresponding distances are:
[27.85677655436824, 25.0, 38.07886552931954, 26.92582403567252, 38.07886552931954]

\********************/
searching elements within EUCL distance of: 50
[(51, 75), (25, 40), (10, 30), (35, 90), (70, 70), (60, 80)]

The corresponding distances are:
[27.85677655436824, 25.0, 38.07886552931954, 26.92582403567252, 45.27692569068709, 38.07886552931954]
```

## Ejercicio 7
in tst_prefix_search.py you can find the code corresponding to the implementation in python of the pseudocode given as an answer to the point number 7 of the test.

> Give a high-level description (but detailed enough) of an algorithm to
> list in ascending lexicographic order the subset of words in a TST (ternary search
> tree) that begin with a given prefix p. Assume that the given prefix and all words
> in the TST are strings built from 8-bit ASCII characters, with the usual ordering,
> furthermore, assume that the end-of-string symbol is \0, that is, the character which
> ASCII code is 0 (henceforth smaller than any other character).


the code outputs a drawing of an example TST and some prefix searches:

```python

['apple', 'apricot', 'banana', 'apartment', 'apex', 'ball', 'cat', 'dog', 'cataract']
|-- a
    |-- p
        |-- p
            |-- a
                |-- r
                    |-- t
                        |-- m
                            |-- e
                                |-- n
                                    |-- t
                                        |-- #
                |-- e
                    |-- x
                        |-- #
            |-- l
                |-- e
                    |-- #
            |-- r
                |-- i
                    |-- c
                        |-- o
                            |-- t
                                |-- #
    |-- b
        |-- a
            |-- n
                |-- l
                    |-- l
                        |-- #
                |-- a
                    |-- n
                        |-- a
                            |-- #
        |-- c
            |-- a
                |-- t
                    |-- #
                    |-- a
                        |-- r
                            |-- a
                                |-- c
                                    |-- t
                                        |-- #
            |-- d
                |-- o
                    |-- g
                        |-- #
Words with prefix 'ap': ['apartment', 'apex', 'apple', 'apricot']
Words with prefix 'ba': ['ball', 'banana']
Words with prefix 'cata': ['cataract']


```
