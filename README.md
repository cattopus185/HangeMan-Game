# HangeMan-Game
This is my first self coded program for the game hangmen. Perhaps it can help more self-taught beginner programmer to learn more about the way how I think about constructing a project.

The core concept of my way of thinking is that 
1) breaking the answer words into a list for each one of its letters
2) makesure the EMPTY placeholder for OUR answer word has the same list length as the COMPUTER choice word
3) Then replace the placeholder in OUR answer word with the input from the human player, 
    if the input letter found in the COMPUTER choice word, then use the indices of the COMPUTER choice word,
    and then make the indices into a list, which is for iteration into a new list that is to replace the EMPTY placeholders in OUR answer word.
5) Then rejoin both the list of OUR answer owrds, and the list of COMPUTER choice word to compare their similarity 
