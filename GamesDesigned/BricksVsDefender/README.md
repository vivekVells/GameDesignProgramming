### View all of my Projectworks - click over here -> [Vivek Vellaiyappan Project Works](https://github.com/vivekVells/VivekVellaiyappanProjectWorks)
---
# Bricks vs Defender

### Title: 
- Bricks vs Defender
### Author: 
- Vivek Vellaiyappan Surulimuthu
### Proposal Submission Date: 
- 13th September 2018 
- [Game Proposal Link](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Design/Bricks%20vs%20Defender%20-%20Project%20Game%20Proposal%20.pdf) 
### Repo Location:
- https://github.com/vivekVells/GameDesignProgramming
### Version 1.0 - MVP-1 - Demo Files Location
- https://github.com/vivekVells/GameDesignProgramming/tree/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1
### Version 1.0 - MVP-1 - Application Preview
- [Click here](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/README.md#application-preview) to view all the screenshots of the working program application
- HOME PAGE
![Home Page](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Game%20Home%20Screen.png)

### Actual Project Scope: 
#### Description: 
- Combination of Brick Breaker and Pillball  Game but totally new concept that is not available anywhere in internet as of now. The game to be developed - titled “Bricks vs Defender” will be a multiplayer defending game which is based on Last Man Standing gaming concept. 
#### Planning: 
- This game will be designed from scratch and willing to complete as many MVP versions as possible. MVP versions for this game will be mentioned below.
#### Note: 
- Refer Game Design Components first for better understanding
#### Game play explanation: 
- First player (Single/Two) wins when more bricks being created using the Quaffle (ball) for opposite defending player such that the defending player will not be able to clear the bricks anymore. 

### What’s New: 
- The concept is fresh and I could not find it anywhere on the internet. It’s easy to play but harder to master depending upon the type of players playing against each other which creates more fun.

#### Game Design Components
1. Play rules and mechanics
    - Players can play against each other in Single or in team (Two players)
    - Paddle can move either left or right
    - Flipper can move in all directions (360°)
    - Player clears or bursts the brick by using the Quaffle (ball)
    - When a player misses to hit the Quaffle ball on his/her/bot’s paddle, the Quaffle ball will be passed to the opposite defending player
    - Player first should clear all assigned bricks, then try to reach the touchdown line which when reached leads to assigning more bricks for opposite defending player to clear.
    - Player wins when assigned bricks reach the paddle of opposite defending player
2. Level design
    - Objects involved: wall-like structure, paddle, flipper, bricks, touchdown line, points
    - The game play screen is enclosed inside wall-like structure 
    - Paddle positions: 1 Paddle on top & 1 Paddle on bottom assigned to players 
    - Flippers positions: 2 Flippers on left &  2 Flippers on right assigned to players
    - 3 Blocks positioned in Middle: (mentioned in order from top to bottom)
      - First block (Brick) - Top side Defender against Bottom side player 
      - Top side player aims to clear all assigned bricks first, then tries to reach the touchdown line which when reached assigns more bricks for defending Bottom side player to clear
      - Middle Block - touchdown line
    - Line when reached denotes that the player have cleared all required assigned bricks and such player would assign more bricks for opposite player to defend
    - Last block (Brick) - Bottom side Defender against Top side player
    - Bottom side player aims to clear all assigned bricks first, then tries to reach the touchdown line which when reached assigns more bricks for defending Top side player to clear
    - Points: a scoreboard will be used to keep track of player scores

3. Interaction design
    - Interaction:
      - Keyboard: 
          - Paddle direction: Left/Right using Left/Right Arrows
          - Flipper direction: 
            - For selecting left positioned flipper: Down Arrow
              - Up Arrow + ‘a’ to rotate flipper clockwise 
              - Up Arrow + ‘s’ to rotate flipper anti-clockwise 
            - For selecting right positioned flipper: Down Arrow 
              - Down Arrow + ‘a’ to rotate flipper clockwise
              - Down Arrow + ‘s’ to rotate flipper anti-clockwise
    - Feedback:
      - Score: displayed on scoreboard after each game play. 1 point per game win.
      - Powers hidden inside bricks:
        - Powers like expanding/shrinking paddle size, exploding more bricks when the Quaffle ball hits the bricks, etc. 
4. Audio-visual design
  - This is still in planning phase. But it’s self-applicable wherever required like whenever the Quaffle ball hits paddle or wall or brick or touchdown line sounds will be heard  accordingly. Visual would be very simple screen with Walls which contains paddles, flippers, player names, bricks, touchdown line and quaffle ball each with different colors and size.
5. Story
  - To motivate the players and make things more interesting, some powers can be hidden inside the bricks which when broken can reveal some cool powers to the player who broke it and even make the people to kind of have a bet (Say $5 for the one who wins) such that it is kept tracked in a bet-score board.
  
#### Describing what I am adding:
  - Fresh game concept (new)
  - Multiplayer feature (aiming to make players to play in 2 different screens)
  - Bet feature (Bet-scoreboard to keep track of who owes to who - to motivate players to play)
#### My proposal planning: (completing as much MVP versions as possible before semester ends)
  - MVP v1: Pinball game + score manipulate
    - Design the game UI that replicates pinball game
  - MVP v2: Flippers add + sound effects
    - Extend game by adding flippers and include the sound effects 
  - MVP v3: Single screen with two player with paddle alone
    - 2 players playing against each other using a paddle on their side in a single screen (may use 2 keyboards or single keyboard with different keys being assigned to the 2 player accordingly) with touchdown line as the wall and players playing in their side alone. (say player wins if the player clears all the bricks on his/her side)
  - MVP v4: Single screen with two player with flipper
    - Flipper include
  - MVP v5: two players against with touchdown line
    - Include touchdown line and give the functionality of creating cum assigning the bricks to opposite defending player if a player reaches touchdown line
  - MVP v6: I have never programmed a game in my life; so, first I will try to complete upto MVP v5 before this semester ends, then I will plan after that since I believe I will die and resurrect to complete MVPs from 1 to 5 itself.  

#### A Promise: 
- I have never coded a game and I struggled a lot to build a home using pygame itself; but I will give my best to complete as many MVPs as I can like I mentioned above in my proposal planning. 

##### Thank you for taking your time and reading this big proposal which is not in a single page.

#### Ref:
- Last Man Standing (LMS) - https://en.wikipedia.org/wiki/Last_man_standing_(gaming) 
- Minimum Viable Product (MVP) - https://en.wikipedia.org/wiki/Minimum_viable_product 
- Brick Breaker game - https://en.wikipedia.org/wiki/Brick_Breaker 
- Pinball game - https://en.wikipedia.org/wiki/Pinball (find info about flipper in this link)

###### P.S.: Thank you for taking your time and reading this big proposal which is not in a single page.

### Application Preview
- Welcome Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Welcome%20Screen.png)
- Game Home Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Game%20Home%20Screen.png)
- Game Won Status Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Game%20Won%20Status%20Screen.png)
- Game Over Status Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Game%20Over%20Screen.png)
- Power Up - Paddle Width Enlarged Status Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Power%20Up%20-%20Enlarged%20Paddle%20Width%20Screen.png)
- Power Up - Max Life Increased Status Screen
![](https://github.com/vivekVells/GameDesignProgramming/blob/master/GamesDesigned/BricksVsDefender/Demo/ver1.0%20-%20MVP1/Power%20Up%20-%20Max%20Life%20Increase%20Screen.png)
