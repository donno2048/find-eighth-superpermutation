# find-eighth-superpermutation
this repository is used to find the eighth superpermutation

## What is that?

that scientific world still don't know what are the 7th, 8th, 9th, ... [superpermutations](https://en.wikipedia.org/wiki/Superpermutation).

this code can solve the problem, it may take a while, but after some (long) time you will get the answer.

just download the code from [the realeses section](https://github.com/donno2048/find-eighth-superpermutation/releases), open cmd in the folder where the code is and run `python find-8th.py`

## Why did you set the minimum `i` to be `8**46077`?

as proved [here](https://oeis.org/A180632/a180632.pdf) `46085` is is a lower bound of the digits, and since we're using octal base this is `8**46085`, but we automatically add `0` at the beginning because we're using `oct` and since the first digits better to be all the first 8 digits we add the digits `1-7` so we need just `46077` digits.
