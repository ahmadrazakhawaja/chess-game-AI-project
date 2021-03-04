# Chess Game
## Technologies used:
Python with pygame module




## Project Description:
This is a Chess game built using python with pygame module for GUI. It has 2 playing mode either you can play against another human player or against AI. The AI was implemented using Minimax algorithm with alpha beta pruning and with the depth search of 3.

Inorder to model a chessboard within a data structure a 2D array was used with the dimensions of 8x8. The chessboard array could store 64 gametiles objects and each gametile object stored a tile number and a chess piece object.

## Files Description:

1. **Board Directory:**: 
      - Board.py: In this file we create a class of chessBoard and initialize and declare a 2D array of gametiles with null pieces and then place all the chess pieces of the board on their respective starting positions. 
      - move.py: In this file we define some of the special cases in chess for example castling, enpassant rule, check. functions are used to check whether the the player is in check, return moves available in case the player is in check, return moves in case of castling and return moves available in case of enpassant rule.
      - Tile.py: It creates a Tile class which is placed on chessboard array. It can store a position number on the board and a chess piece object. 

2. **chess Art directory:**: Contains all the images of the chess pieces.

3. **pieces directory:**: Contains files in which every chess piece class is defined. Every chess piece class has alliance (indicating whether the piece is white or black) and position ( coordinates on the chessboard ) attributes. It also has legalmove method which is used to calculate the legal moves for that chess piece on the chessboard. 

4. **Player directory:**:
      - AI.py: Contains the logic for AI algorithm. The AI was implemented using recursive Minimax algorithm with alpha beta pruning and with the depth search of 3. The evaluation function assigned each chess piece a value, White pieces were assigned a positive value based on their rank and black pieces were assigned negative value based on their rank as well. So the total value becomes 0 in the start of the game where each side has all the pieces. The algorithm tried to search all possible moves up to the depth of 3 and calculate which next move could allow it to have best evaluation value.

5.  **Playchess.py:**: Main file of the program which merges all the functionality from the other files and itself as well to implement all this on pygame GUI.
      
5. **Screen**:
Game Screen

    1. Main Screen: 
    (https://raw.githubusercontent.com/ahmadrazakhawaja/chess-game-AI-project/master/project_images/Screenshot%202021-03-04%20at%206.16.22%20PM.png)<br/><br/>
    2. group.html:
    This is the group_chat page where user can see all the group chat and send text to group<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Group_chat_page1.png?raw=true)<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Group_chat_page2.png?raw=true)<br/><br/>
    4. login.html:
    This is the login page<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Login_page.png?raw=true)<br/><br/>
    5. register.html:
    This is the register page<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Register_page.png?raw=true)<br/><br/>
    6. room.html:
    One to One chat page<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Chatting_page.png?raw=true)<br/><br/>
    7. setting.html:
    Group Settings page<br/><br/>
    ![index page](https://github.com/ahmadrazakhawaja/chat-application/blob/master/cs50-web-screenshots/Group_settings_page.png?raw=true)<br/><br/>

6. **static/chat folder**:
This folder contains the styles.css stylesheet for the entire site and the **very important chat.js** javascript file which contains the code to initiate the websockets and use fetch api at the client side and handle all client side interactivity. Bootstrap is also used to style the frontend and make it mobile responsive although not which focus is given to styling and asthetics as more focus was on backend services and on handling all the data in real time.

A channel layer is used in this app which allows multiple consumer instances to talk with each other, and with other parts of Django. We will use a channel layer that uses Redis as its backing store. Each client that connects to the application is assigned a unique channel name through which he is communicated all the receiving messages.

## How to Run the Application
`git clone https://github.com/ESWZY/cs50web-final-project.git`

`cd cs50web-final-project`

`pip install -r requirements.txt`

In order to run this app locally we need to start a redis server. I start the redis server inside docker container using the command:

`docker run -p 6379:6379 -d redis:5`

After redis server has started then you can normally start the app using the command:

`Python3 manage.py runserver`

Run these following commands to migrate database.

`python manage.py makemigrations`

`python manage.py migrate`


## Deployment

The application is deployable to Heroku. But we have to change the Database from SQL Lite to Heroku Post gre SQL. We also need redis store for channel layer for that we can use the Heroku Redis addon. Since redis addon requires a verified account on Heroku using the credit card details I was not able to use the addon and hence The Websocket Functionality is currently not active hence messages cant be delivered.

Here is the link to deployed website: https://cs50wchat.herokuapp.com/

Please note that currently messaging service is not active because I can’t use the Heroku Redis addon.
