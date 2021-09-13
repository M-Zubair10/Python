# def removing_spaces(word):
#     '''
#     word: strings of letters of which spaces would be removed
#     return: new string with all space would be removed
#     '''
#     for i in word:
#         if i == " ":
#             word = word.replace(i, "")
#     return word
#
# def match_with_gaps(my_word, other_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     other_word: string, regular English word
#     returns: boolean, True if all the actual letters of my_word match the
#         corresponding letters of other_word, or the letter is the special symbol
#         _ , and my_word and other_word are of the same length;
#         False otherwise:
#     '''
#     check = False
#     my_word = removing_spaces(my_word)
#     while len(my_word) == len(other_word):
#         for i in my_word:
#             if i in other_word:
#                 check = True
#     if check:
#         return other_word

print(2601)