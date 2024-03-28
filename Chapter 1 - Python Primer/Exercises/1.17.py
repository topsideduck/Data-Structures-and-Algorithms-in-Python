"""
Had we implemented the scale function (page 25) as follows, does it work
properly?

def scale(data, factor):
    for val in data:
        val *= factor

Explain why or why not.
"""

# no, it doesn't work properly. the values in data do not get reassigned as val is an
# immutable variable and does not have any relation to values in data.
