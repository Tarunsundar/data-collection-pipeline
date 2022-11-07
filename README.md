# Data Collection pipeline

This is a python program written to automate the process of Data collection from a chosen
website, For this project, coinmarketcap, a finance based website had been chosen.
implemented a class for the data collection schema
	
    Parameters & Attributes
    _______________________

    rps_choice : list
    List of choices in this game for user.
 
     rps_choice_2 : list
    List of choices in this game for the computer.

    winner: list
    List of possible winners of this game

    CPU_choice: list
    CPU_choice from list of possible choices

    user_choice: list
    user_choice from list of possible choices

    computer_wins: int
    this attribute is to store the number of computer wins

    player_wins: int
    this attribute is to store the number of player_wins.
    
    winner : list
    List of possible winners in this game.
    
    winner_Index : list
    winner of the game, this index from the possible list of winners.

    Method
    ______

    count_down()
    
    this function waits for the user's
    visual input for some time to capture 
    the player's hand movements

    get_prediction()
    
    this function returns the pre-built method for the rock, 
    paper and scissors game.

    get_computer_choice()
  
    this function gets the computer choice from list of possible choices
    of the game using random() function and provides this as computer's choice
    
    get_user_choice()
  
    this function gets the user choice from the images from the coamera
    using the trained machine learning models and using some programming logics.

    get_result()
    this function gets the final result of the game after getting the inputs
    from the user and computer with the help of rock, paper and scissors logic.

    play()
    this is the main method which integrates chunks of codes(functions) 
    to develope this game neatly while following good coding practices.



