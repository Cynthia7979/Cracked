<b>Cracked</b>, a game with imagination which players need to kill monsters in different floors.

It's called Cracked because all monsters are creepy and not understandable.

Concepts in game:
-------------------
1. Abstract position.
    For every floor, (0,0) is at the bottom left.
    If every floor has an axb size, then bottom right = (a,0), top left = (0,b), top right = (a,b)

2. Game status.
        A GameStatus instance contains global data and variables in game.
        GameStatus instance will not store any local data for functions or other instances.

3. Screen position.
        A screen position is the real position we use to blit surface objects.
        It's the pygame-kind position.
--------------------
To calculate screen position, we must know where the origin(0,0) of the floor is.
This will be stored in the main GameStatus instance.