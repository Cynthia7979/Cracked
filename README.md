**Cracked**, a game with imagination which players need to kill monsters in different floors.
 It's called Cracked because all monsters are *creepy and not understandable*.
[![Example of mob \'butterfly\'](https://s13.postimg.org/hlvyhh6fr/combine3.png)](https://postimg.org/image/9gdwjbi6r/)
Concepts in game:
---
1. ***Abstract position***.
    For every floor, (0,0) is at the bottom left.
    If every floor has an axb size, then `bottom right = (a,0), top left = (0,b), top right = (a,b)
2. ***Game status***.
    A `GameStatus` instance contains global data and variables in game.
    `GameStatus` instance will not store any local data for functions or other instances.
3. ***Screen position***.
    A screen position is the real position we use to `blit` surface objects.
    It's the pygame-kind position.[1]
4. ***Player status***.
    A `PlayerStatus` instance contains local variables for player (e.g. floor, blood)
    This instance will be deleted anytime the player quit \"playing\",
    which means the player died or just stopped to visit achievement house or store in game.
5. ***Scene functions***.
    Scenes will be defined as functions in this program. Scene functions take `GameStatus`
    instances and change it by calling `GameStatus.update()`.
    A scene function should look like this:

        def test_scene(game_status):
            # Load data from game_status
            while True:
                # Do something...
                game_status.update(changed_things)

---
#### Footnotes
[1]To calculate screen position, we must know where the origin(0,0) of the floor is.
This will be stored in the main GameStatus instance.