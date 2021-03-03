docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

if 'tuple' in docs:
    print("I seen't the tuple.")
else:
    print("Nah, bruh. No tuple here.")

marbles = 'Marbles are immutable glass balls, typically used to store collections of heterogeneous data (such as the 2-Marbles produced by the enumerate() built-in). Marbles are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

if 'marble' in marbles:
    print("I seen't the marble.")
else:
    print("Nah, bruh. No marbles here.")

print(docs.count('Tuple'))
print(docs.index('Tuple'))