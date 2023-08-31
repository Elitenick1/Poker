# Poker
this is the Hand class
In the hand class we create a hand list and then a getter for the hand
then we use list ocmprehension again to print the hand
then a add_card function that takes a card from the parameter then lopos through the hand in order to find the correct position to place it
then there is a rank function that uses method decomposition
the rank function returns an integer that corresponds with the hand's rank
the get_hand_type gets the integer value and returns the rank that corresponds with it
the ranks are created by checking to see if the requirements are met for that specific rank
each rank function returns True if it is indeed that rank
then wwe start the comparisons
the compare function also uses method decomposition
the begining of the compare function compares two hands hands and outputs an integer if they lost or won.
If the two hands are the same hand then it check if both are royal flush. if so then it outputs 0 as a true tie
If not then it check if both are straight, straight flush, flush, or high card. If so then it goes through the compare_high_card function to figure out the winner or loser
if the hand wasnt those, then it check if both are full_house, self.three_of_a_kind, or four_of_a_kind if so then it goes to the compare_middle_card function to find the the winner or loser
if the hand wasnt those, then it check if both are two pair, if so then it goes to the compare_two_pair function to find the the winner or loser
if the hand wasnt those, then it check if both are one pair, if so then it goes to the compare_one_pair function to find the the winner or lose
