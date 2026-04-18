"""
this program is a loop that rins ten times so in that loop there's another loop if the index of the first loop rinning ten times is odd show "<" ten times else show ">" ten times then loops again ten times.
"""

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
