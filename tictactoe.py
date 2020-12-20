import random, copy, sys

def new_game(): 
    #show player the numbering of the board 

    board = [' ',' ',' ','_','_','_','_','_','_']
    availablespots = ['1','2','3','4','5','6','7','8','9']
    winner = '' 

    #choose players
    players = choose_players()

    #start game
    display_gameboard(board)
    while winner == '':
        winner, board = handle_turn(players, board, availablespots)

    #end of game. Congratulate winner
    congratulate_winner(winner, players)


def choose_players():
    #inputs can be: random, human, alphabeta 
    #if no inputs give, assume human vs random. 

    if len(sys.argv) > 1: 
        player_one = sys.argv[1].lower().strip()
        player_two = sys.argv[2].lower().strip()
    else:
        player_one = 'human'
        player_two = 'random'
    
    if player_one != "random" and player_one !="alphabeta" and player_one != "human":  
        print('Invalid entry for Player 1. Must be: human, random, or alphabeta')
        print('Try Again') 
        exit()
    elif player_two != "random" and player_two !="alphabeta" and player_two != "human":  
        print('Invalid entry for Player 2. Must be: human, random, or alphabeta')
        print('Try Again') 
        exit()

    #if everything looks good:
    print('    *** NEW GAME ***\n')

    return [player_one, player_two]

def display_gameboard(board_state): 
    #this function just displays the game board
    #input is a list of strings designating the current board state 

    if not 'X' in board_state: #if it's the first turn, display move options
        print('')
        print('_' + board_state[6] + '_|_' + board_state[7] + '_|_' + board_state[8] + '_' + '      _7_|_8_|_9_')
        print('_' + board_state[3] + '_|_' + board_state[4] + '_|_' + board_state[5] + '_' + '  =   _4_|_5_|_6_')
        print(' ' + board_state[0] + ' | ' + board_state[1] + ' | ' + board_state[2] + ' ' + '       1 | 2 | 3 ')
        print('')
    else:
        print('')
        print('_' + board_state[6] + '_|_' + board_state[7] + '_|_' + board_state[8] + '_')
        print('_' + board_state[3] + '_|_' + board_state[4] + '_|_' + board_state[5] + '_')
        print(' ' + board_state[0] + ' | ' + board_state[1] + ' | ' + board_state[2])
        print('')


def check_winner(board_state, availablespots): 
    #this function checks if there is either a winner or a tie. 

    winner = '' 

    #check rows
    if (len(set(board_state[:3]))==1) and board_state[0] != ' ': #'set' reduces list to only unique values
        winner = board_state[0]
    elif (len(set(board_state[3:6]))==1) and board_state[3] != '_': 
        winner = board_state[3]
    elif (len(set(board_state[6:]))==1) and board_state[6] != '_': 
        winner = board_state[6]

    #check columns
    if len(set([board_state[0], board_state[3], board_state[6]])) == 1: 
        winner = board_state[0]
    elif len(set([board_state[1], board_state[4], board_state[7]])) == 1: 
        winner = board_state[1]
    elif len(set([board_state[2], board_state[5], board_state[8]])) == 1: 
        winner = board_state[2]

    #check diagnols
    if len(set([board_state[0], board_state[4], board_state[8]])) == 1: 
        winner = board_state[0]
    elif len(set([board_state[2], board_state[4], board_state[6]])) == 1: 
        winner = board_state[2]

    #if no more spaces and no winner, it's a draw
    if availablespots == [] and winner == '':
        winner = 'Draw' 

    return winner 


def handle_turn(players, board_state, availablespots):
    #this function handles a single turn cycle including: player one input, computer turn, and checking for a winner

    winner = '' 
    turn = 0 
    marks = ['X','O']
    while turn < 2:
        if winner == '': 
            if players[turn] == 'human':
                winner, board_state, availablespots = play_human(board_state, availablespots, marks[turn])
            elif players[turn] == 'random':
                winner, board_state, availablespots = play_random(board_state, availablespots, marks[turn]) 
            elif players[turn] == 'alphabeta':
                winner, board_state, availablespots = play_alphabeta(board_state, availablespots, marks[turn]) 
            
            display_gameboard(board_state)
        
        turn += 1 
        
    
    return winner, board_state


def play_human(board_state, availablespots, mark):
    #handles a turn for a human player: prompt, validate, and execute move 
    #returns the winner (str) and the new board state (list of str's), and available spots (list of str's) 

    pos = str(input(mark + 's turn. Choose a position: ')).strip()
    while pos not in availablespots: #check to make sure user selection is in available spots. 
        if pos.lower() == 'exit' or pos.lower() == 'end': #if at any point, user inputs "end", end then game. 
            print('GAME OVER') 
            exit()
        pos = str(input('That spot isnt available. Choose a position: ')).strip()
    availablespots.remove(pos) #remove this position from available spots
    board_state[int(pos)-1] = mark #put a mark in the chosen location 

    #check for winner 
    winner = check_winner(board_state, availablespots) 

    return winner, board_state, availablespots

def play_random(board_state, availablespots, mark):
    #handles a turn for a random player
    #returns the winner (str) and the new board state (list of str's), and available spots (list of str's) 

    pos = random.choice(availablespots)
    availablespots.remove(pos)
    board_state[int(pos)-1] = mark #put a mark in the computer's location          
    
    #check for winner 
    winner = check_winner(board_state, availablespots) 

    return winner, board_state, availablespots

def congratulate_winner(winner, players):
    #Prints winner message and end game 
    
    def generic_win_message(winner):
        #support function for congratulate_winner()
        if winner == 'X':
            print('Player One Won!!!') 
        else:
            print('Player Two Won!!!') 

    if winner == 'Draw':
        print('Its a TIE!! :/')
        print('GAME OVER') 
        exit()

    #print different messages depending on who's playing the game. 
    if players[0] == players[1] and players[0] == 'human': #both humans
        generic_win_message(winner)
    elif players[0] != 'human' and players[1] != 'human': #both computers
        if winner == 'X':
            print (players[0] + ' as Player One won the game!')
        else:
            print (players[1] + ' as Player Two won the game!')
    else: #one human, one computer
        if (winner == 'X' and players[0] != 'human') or (winner == 'O' and players[1] != 'human'):
            print('Wow... You lost...')
        else:
            print('Congratulations!!! You Won!!!') 

    print('\nGAME OVER')


def play_alphabeta(board_state, availablespots, mark):
    #plays and executes an optimal move using minimax with alphabeta pruning
    #input is the board state, a list of available positions for minimax player, and a mark X or O denoting the player's position
    #returns winner (X or O), board state, and availablespots 

    utility_list = [] 

    #find optimal choice
    for move in availablespots:
        #create subsequent game boards
        sub_board = copy.deepcopy(board_state)
        sub_avail_spots = copy.deepcopy(availablespots)
        sub_avail_spots.remove(move)
        sub_board[int(move)-1] = mark

        #fill utility list with moves choices and their values 
        utility_list.append ((move, a_b_minimum_move(toggle(mark), sub_board, sub_avail_spots, -2.0, 2.0)))

    #sort utility list based on utility value in descending order
    utility_list.sort(key=lambda x: x[1], reverse=True) 

    #if multiple moves have the same utility, choose them at random. 
    options_list = []
    for i in range(len(utility_list)-1):
        if utility_list[0][1] == utility_list[i][1]:
            options_list.append(utility_list[i][0]) #add only the move position, not the utility

    pos = random.choice(options_list)

    #execute final choice 
    availablespots.remove(pos)
    board_state[int(pos)-1] = mark #put a mark in the computer's choice          
    
    #check for winner 
    winner = check_winner(board_state, availablespots) 

    return winner, board_state, availablespots


def a_b_minimum_move (mark, board_state, availablespots, alpha, beta):
    #support function for alphabeta player
    #simulates an opponent's move. 'mark' input designates player X or O 
    #returns the integer value of this board_state's utility [-1,1]
    
    utility_list = []
    util = '' 

    #check for subsequent winner 
    sub_winner = check_winner(board_state, availablespots) #returns a mark X or O 
    if sub_winner == mark:  #if the winner is the opponent
        util = -1.0
    elif sub_winner == toggle(mark): 
        util = 1.0
    elif sub_winner == 'Draw':
        util = 0.0
    elif sub_winner == '': #else, game is still going

        for move in availablespots:
            #create subsequent game boards
            sub_board = copy.deepcopy(board_state)
            sub_avail_spots = copy.deepcopy(availablespots)
            sub_avail_spots.remove(move)
            sub_board[int(move)-1] = mark

            #fill utility list with moves and their values 
            utility_list.append ((move, a_b_maximum_move(toggle(mark), sub_board, sub_avail_spots, alpha, beta)))

            #pruning 
            if utility_list[len(utility_list)-1][1] <= alpha: #if most recent value is smaller than alpha, don't worry about the rest of the options. 
                return utility_list[len(utility_list)-1][1]
            elif utility_list[len(utility_list)-1][1] < beta: 
                beta = utility_list[len(utility_list)-1][1]
                util = beta

    if util == '': #if no beta was crossed, sort to find best util. 
        #sort utility_list in ascending order
        utility_list.sort(key=lambda x: x[1], reverse=False) 
        util = utility_list[0][1]

    return util


def a_b_maximum_move (mark, board_state, availablespots, alpha, beta):
    #support function for alphabeta player. It's a mirror of a_b_minimum_move
    #simulates a maximum move. 'mark' input designates player X or O 
    #returns the integer value of this board_state's utility [-1,1]
    
    utility_list = []
    util = ''

    #check for subsequent winner 
    sub_winner = check_winner(board_state, availablespots) #returns a mark X or O 
    if sub_winner == mark:  #if the winner is the maximum player
        util = 1.0
    elif sub_winner == toggle(mark): 
        util = -1.0
    elif sub_winner == 'Draw':
        util = 0.0
    elif sub_winner == '': #else, game is still going
        
        for move in availablespots:
            #create subsequent game boards
            sub_board = copy.deepcopy(board_state)
            sub_avail_spots = copy.deepcopy(availablespots)
            sub_avail_spots.remove(move)
            sub_board[int(move)-1] = mark
        
            #fill utility list with moves choices and their values 
            utility_list.append ((move, a_b_minimum_move(toggle(mark), sub_board, sub_avail_spots, alpha, beta)))
            
            #pruning 
            if utility_list[len(utility_list)-1][1] >= beta: #if most recent value is greater than beta, don't worry about the rest of the move options. 
                return utility_list[len(utility_list)-1][1]
            elif utility_list[len(utility_list)-1][1] > alpha: 
                alpha = utility_list[len(utility_list)-1][1]
                util = alpha
    
    if util == '': #if no alpha was crossed, sort to find best util. 
        #sort utility_list in ascending order
        utility_list.sort(key=lambda x: x[1], reverse=True) 
        util = utility_list[0][1]

    return util

def toggle(mark):
    #switches an 'X' to an 'O' for the alphabeta simulations
    if mark == 'X':
        return 'O'
    else:
        return 'X' 





#start a new game as defined above
new_game()
