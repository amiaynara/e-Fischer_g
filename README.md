# e-Fischer
1. What is your Project?
My Project is a robotic arm that play chess against Human and I have named it e-Fischer, after the greatest player of all Time Bobby Fischer.
The project has four components: 
    1. A robotic arm: Moves the pieces on the chess board
    2. A Microcontroller: Controls the movement of the arm and decides the the next best move
    3. A Pulley-belt mechanism that enables 2-D motion of the arm, order to reach a particular piece, say Rook on A1
    4. A camera that moniters and captures the move made by human.

2. Why did you choose this project? 
I had always been fascinated by stepper motors and electronics. I saw this independent project to apply my knowledge and further expand it. 
I have always wanted to some that was inter-discplinary, although this was not a large scale project, but I think this was a nice place for me to start and try out different things, fail in the process and learn new things and finally get something unique out of this. 
Besides I also saw opportunity to use various other tools and techniques that were available to us at the campus: 3D printing, moulding, cnc-milling and laser cutting.

3. How did you start?
4. What was your design procedure?  
We started out by first making a proper idea for design on paper and with documentation. By laying out what were the major challenges involved in the project and what milestones we had to achieve in order to complete the project on time. We divided it into phases. 
    1. creating a parts required for the chess board(like chess board, chess pieces)
    2. Making a pulley-belt mechanisms. 
    3. Implementing the image processing algorithm to capture the move made on the board
    4. Piece picking algorithm
    5. Assembly
    6. Testing

5. What are the things that you required in your project?
There were two types of requirement: 
1. Compononents and Equipments(Tools): Stepper motors, drivers, Microcontrollers(Arduino Mega) , Raspberry pi, Camera, Jumpers, Servo motors, acrylic sheets, 3-D printer, Laser Cutter, CNC milling for Acrylic, Wood, pulley, belt, Powersupply.
2. Skill: Like designing the belt pulley mechanism, Coming up with an image processing algorithm.

6. Mathematical calculation?

7. What challenges did you face?How did you overcome them?
There were quite a few challenges, but I would like to mention a few of them that I found really interesting and their solutions had to be cost efficient.

    1. Tracking the pieces on the board: One solution was to place a 'reed sensor' beneath every square on the board these would say what piece is there on above it. however cost of each such sensor was Rs. 160, => (64x160), way over the budget could allow. 
    Solution: We placed a camera (Rs. 1300) right above the board, that captured the board state after each move was made. Since the initial state has to be the same for any chess game, this state can be cleverly assumed to be constant and hence the position of each of piece(say rook) is deterministic at the start of the game(position is always 

    2. Picking up the chess piece: Shapes and heights of the chess pieces are different. This made it difficult for 
        us to come up with a general clipping mechanism, and what should be the depth to which the clipping mechanisms
        should drop in order to pick the piece. 
    Solution: 3D printer saved the day! Thanks to our instructor(Dr. Surya IIT Hyd.), we had access to 3D printers. So we decided to print our own chess pieces. Normally, the chess pieces do not have uniform cross sectional arear. We designed the pieces to have uniform cross section area (by extruding the 2d picture of the piece) and then mounting it on flat cirular disk. This allowed us to make the width of every piece exactly the same. Hence it was muc easier for the clipping mechanism to get hold of the pieces. 
    
    below is not a technical challenge. you may not count it if you want. 
    3. The worst happened. The laser cutting machine caught fire due mishandling by some students.
    solution: we used acrylic cnc and milling machines to get our work done. 

    4. Chess pieces are black and white & the board is also black-and white. This made the task of image processing a lot difficult. 
    Solution: We colored our pieces red and green instead, this helped the tracking of the moves much easier. The color of the pieces don't matter(if you know chess you can beat some one even with pink pieces!). 





8. Governing Equation?
The calulation involved number of spins taken in order to cover the length of one square on the board. Conversion of rotational motion to linear. 
        No slipping condition, 
            => Length of on square on chess = radius_of_stepper_shaft * angle_to_be_rotated(theta)
            => theta = L/r
            Therefore, to cover n squares on the board, number of rotations required  = n*L/(2*pi*r)

Steppers operate on microstepping, single step covers 0.8 degree of rotations. Therefore, total number of rotations required to cover n squares is : 
            steps for each rotation = 360/0.8 = 200 steps 
            => steps to cover n squares on the board = [n*L/(2*pi*r)] * 200   steps
            


9. Fundamental principle?
The 2D motion of the arm was based on the contrained motion principle. The belt tooth were meshed with geared pulley(7 in total, including two on the stepper motor shaft). The length of the belt is fixed, which ensured the movement of the arm when the steppers spinned. 

The Capturing of the moves on the board was based on the Image processing using python. 

10. How much power will it consume? What about efficiency?
    Each Stepper required 15V of Voltage and around 1.2 A of current. There were two such steppers.[These steppers were 'overkill', one could use smaller wattage steppers]
        => P1 = V * I = 15 * 1.2 W = 18 W

    For microcontroller, P2 = 5V * 0.04 A = 0.2 W
    For servo, P3 = 5 * 0.1  = 0.5 W

    Therefore total, 
            P = P1*2 + P2*4 + P3*2          [There were 2 steppers, 4 microcontrollers and 2 servos]
              = 36 + 0.8 + 1
              ~ 40 W

    Note: All Voltage requirements are DC

11. Is it practically feasible to operate in the real world?
Yes, it is. Given the precision of the manufacturing of the arm's component, and proper assembly of the components the realisation of the project, I am confident to say this project is completely feasible. However, I would like to add that the processes required for the manufacture of the components required more precision and room for error must taken care of.  


