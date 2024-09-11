# Global variables

# Game board
board = ["-","-","-",
	"-","-","-",
	"-","-","-"]

game_still_going = True

# Winner or tie
winner = None

# Current Turn
current_player = "X"


# to display the current board
def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


# begin tictactoe game
def play_game():


	#Display initial board
	display_board()

	while game_still_going:
		
		# take a single turn of the current player
		handle_turn(current_player)

		# chcek if game ended
		check_if_game_over()

		flip_player()

	# game ended
	if winner == "X" or winner == "O":
		print(winner + " won.")
	elif winner == None:
		print("Tie.")	


# to take a single turn of a the current player
def handle_turn(player):
	
	print(current_player + "'s turn.")

	# To get initial posiion
	position = input("Choose a position from 1-9: ")

	while position not in ["1","2","3","4","5","6","7","8","9"]:
		position = input("Choose a position from 1-9: ")

	position = int(position)-1

	#checks if place is already played
	while board[position] != "-":
		print("Place already taken, try again")
		play_game()
		

	board[position] = current_player

	# Display board with new played turn
	display_board()

# checks if the game ended
def check_if_game_over():
	check_win()
	check_tie()


#check for winner
def check_win():

	global winner

	# check the rows
	row_winner = check_rows()

	# check the columns
	column_winner = check_columns()

	# check the diagonals
	diagonal_winner = check_diagonals()

	if row_winner:
		# there was a win
		winner = row_winner
	elif column_winner:
		# there was a win
		winner = column_winner
	elif diagonal_winner:
		# there was a win
		winner = diagonal_winner
	else:
		winner = None

	return

# check the rows
def check_rows():
	#set up global variable
	global game_still_going
	# check if rows have same value
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"

	#return the winner
	if row_1 or row_2 or row_3:
		game_still_going = False
	if row_1:
		return board[0]
	if row_2:
		return board[3]
	if row_3:
		return board[6]

	return

# check the columns
def check_columns():
	#set up global variable
	global game_still_going
	# check if rows have same value
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	#return the winner
	if column_1 or column_2 or column_3:
		game_still_going = False
	if column_1:
		return board[0]
	if column_2:
		return board[1]
	if column_3:
		return board[2]

	return

# check the diagonals
def check_diagonals():
	#set up global variable
	global game_still_going
	# check if rows have same value
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[2] == board[4] == board[6] != "-"


	#return the winner
	if diagonal_1 or diagonal_2:
		game_still_going = False
	if diagonal_1:
		return board[0]
	if diagonal_2:
		return board[2]	

	return


# check for a tie
def check_tie():
	# set up global variable
	global game_still_going
	#global board
		
	if "-" not in board:
		game_still_going = False
	
	return

# change current player to other player
def flip_player():
	#set up global variable
	global current_player

	if current_player == "X":
		current_player = "O"
	else: current_player = "X"

	return

play_game()

