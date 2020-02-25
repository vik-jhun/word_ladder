#!/bin/python3

from collections import deque
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:
    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file
    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)
    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    words = open(dictionary_file).readlines()
    wordList = []
    for i in words:
        wordList.append(i.strip("\n"))

    print(wordList)

    if start_word == end_word:
        return [start_word]

    word_stack = [] #     Create a stack
    word_stack.append(start_word) # Push the start word onto the stack
    word_queue = deque()  # Create a queue
    word_queue.appendleft(word_stack)  # Enqueue the stack onto the queue

    while len(word_queue) != 0: # While the queue is not empty
        temp = word_queue.pop() #     Dequeue a stack from the queue AND save
        for word in wordList: #     For each word in the dictionary
            if _adjacent(word, temp[-1]): #         If the word is adjacent to the top of the stack
                temp_copy = copy.deepcopy(temp)
                temp_copy.append(word)
                if word == end_word: # If this word is the end word
                    for j in range(1, len(temp_copy)-2):
                        if _adjacent(temp[j-1],temp[j+1]):
                            temp_copy.pop(j)
                    return (temp_copy)
                word_queue.appendleft(temp_copy)
                wordList.remove(word)






#                 The front stack plus this word is your word ladder.
#             Make a copy of the stack
#             Push the found word onto the copy
#             Enqueue the copy
#             Delete word from the dictionary


    #     if start_word in wordList:
    #         wordList.remove(start_word)
        
    # if end_word not in wordList:
    #     return 0
        
    # wordList.append(end_word)
    # queue = collections.deque([[start_word, 1]])
    # leng = len(start_word)
    
    # while queue:
    #     word, length = queue.popleft()
    #     if word == end_word:
    #         return length
    #     for n in wordList:
    #         if sum(n[i] != word[i] for i in xrange(leng)) == 1:
    #             wordList.remove(n)
    #             queue.append([n,length+1])
    # return 0   



def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    i = 0
    while i < len(ladder)-1:
        if _adjacent(ladder[i], ladder[i+1]) == True:
            i += 1
        else:
            return False
    return True




def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
        
    count_diffs = 0
    if len(word1) == len(word2):
        for a, b in zip(word1, word2):
            if a!= b:
                count_diffs += 1
    if count_diffs == 1:
        return True
    else:
        return False


