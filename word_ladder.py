#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    with open (words5.dict) as wordList:
        xs = wordList.readlines()
    print ('xs=', xs)

    wordList.append(endWord)
    queue = collections.deque([[beginWord, 1]])
    leng = len(beginWord)
    
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for n in wordList:
            if sum(n[i]!=word[i] for i in xrange(leng))==1:
                wordList.remove(n)
                queue.append([n,length+1])
    return 0


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


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
