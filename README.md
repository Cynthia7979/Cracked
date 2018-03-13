**Cracked**, a game with imagination which players need to kill monsters in different floors.
 It's called Cracked because all monsters are *creepy and not understandable*.

 [![Example of mob 'butterfly'](https://s13.postimg.org/hlvyhh6fr/combine3.png)](https://postimg.org/image/9gdwjbi6r/)

Concepts in game:
---
1. ***Abstract position***.
    For every floor, (0,0) is at the bottom left.
    If every floor has an axb size, then `bottom right = (a,0), top left = (0,b), top right = (a,b)`
    I decided to give every floor a 50x30 size. Change if needed.
    ```
    (0, 30)                             (50, 30)
    ┌────────────────────────────────────┐
    │                                    │
    │                                    │
    │          abpos (x, y)              │
    │           ┌────────┐               │
    │           │ thing  │               │
    └────────────────────────────────────┘
    (0, 0)                             (0, 50）
    ```
2. ***Screen position***.
    A screen position is the real position we use to `blit` surface objects.
    It's the pygame-kind position.[1]
3. ***Game status***.
    A `GameStatus` instance contains global data and variables in program.
    `GameStatus` instance will not store any local data for any functions or other instances.

4. ***Play status***.
    A `PlayStatus` instance contains local variables for player (e.g. floor, blood)
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

6. ***MobStatus***.
    `MobStatus` will be a class which stores all Mob instances on the current floor.
    Its instance will be created by `play_scene()` function while the player start a new game.
    Its method will be "responsible" for calling the `make_policy()` method of every Mob instance on the floor.
---
#### Footnotes
[1]To calculate screen position, we must know where the origin(0,0) of the floor is.
This will be stored in the main GameStatus instance.

[2]I'm not sure if it's good to store a "mob status" in "player status"...
Maybe we can find a better solution to this problem.
Recent change: `PlayerStatus` --> `PlayStatus`
Current change: `PlayStatus` --> `PlayerStatus` and add `MobStatus`
I take the 'original mob instance' as the pre-defined Mob class instance inside another file. 
This file may also include defined Skill class instances, and so on.
