git bisect demo
===============

for run tests you should clone repo and run this commands:

    git bisect start
    git bisect bad
    git bisect good d8e32db15267e857dda146d6a131a1289e91da74
    git bisect run python test.py

for friday(18+) test run:

    git bisect start
    git bisect bad
    git bisect good d8e32db15267e857dda146d6a131a1289e91da74
    git bisect run python friday_18+/test.py

