# Python refresher exercises
# part 1 
# May 25, 2020

# - This set of exercises uses topics from refreshers 1 and 2: basic data types and flow control
# - But, you're free to use other python concepts (functions, OOP) as well
# - My solution is directly below, but with a visual buffer so you don't see it accidentally.

# You should have gotten this file by forking the python_ex_1 project from my github
# repo: https://github.com/ChHarding/python_ex_1

# How to work the exercises:
# - Use a debugger to set a break point at the print() at the top of the solution part so you
#  don't accidentally run beyond it and see the solution. This is the "end" breakpoint
# - Set another "start" breakpoint at the print() that shows the start of each part
#  write you code between those break points
# - To run your code, start the debugger (will stop at the "start" breakpoint) and
#  hit step or continue. Once you have your bug free solution, remove the start and
#  end breakpoints and move on to the next part. Here's an example:


# part 0
# This is just a simple example to demonstrate how the start and end
# breakpoint system works
# Task: get the user's name with input() and print out Hello <name>
#print("start of part 0") # set breakpoint here
# your code here

'''
user_name = input("Enter your name here")
print("Hi " + user_name +"!") #attempted run .py to output as txt however it would not run pass this line, I wonder if input does not show correctly 
# CH: yes, my bad, this will wait for input so you'd have to comment it out for the > thing to run. I didn't think about that! 
'''

#print("end of 0") # set breakpoint here 
'''























# solution 1
name = input("What's your name?")
print("Hello", name)
'''

# Before we really start, a couple more things:
# - your solution may be different or even better than what I showed
# - Please get in the habit of documenting your code as you go along
#   You don't need to state the obvious but you should point out anything 
#   that could be interesting later.
# - After you've finished the code for a part (or even more often) you must
#   perform a commit! You should also push your commit to the remote master (Push)
#   once in a while

# Grading:
# - I will grade purely on effort based on your comments and commits!
# - Each part is worth 1 point
# - That means I don't really grade (judge you) by the quality of your code
# - Please give it your best shot and try to get a good result but it's up to you
#   you fancy you want to get. If you're stuck, you can't get a good result,
#   and you're out of time, just put in a (brief) comment about what you tried
#   and move on. If a part always produces an error (i.e. would stop execution)
#   use ''' ''' to comment out the entire part, that way your debugger won't stop!
#   I will still give you your point if I can see that you at least tried ... something!

# Handing in:
# - once you're done type this into your OS console in VS:
# python refresher_ex_1.py > results.txt
# this will run your file and put the output into results.txt.
# on Canvas hand in:
# - your version of this .py file
# - your results.txt
# - tell me the URL of your forked repo 

# part 1
# task:  L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# using both, indexing and slicing on L, assemble and print a new list N that contains:
# [0,2,3,[5,6],8,10] 
# as an example, here's  how i've constructed a similar list X which contains [[2, 3], [10]] from L:
#
# L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# X = [ L[2][1:-1], L[-1][2] ] 
# print(x)  => [[2, 3], [10]]
# You need to do something similar but end up with [0,2,3,[5,6],8,10] instead. One way to work 
# through this is to break the process down in small steps, store result of each step in a new variable
# and use those variables in the next step
#print("start of part 1") # set breakpoint here
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print(L)
# your code
'''
#1st attempt - N = [L[0], L[2][1],L[2][2],[[L[3][0][0], L[3][1][0]], L[4][0], L[4][-1]]
# print(N)
# -attempted to write out entire list in one line, not sure if this is it but the list within the list is hard to slice. 
# CH it's always advisable to break down things if needed. Don't be affraid to have lots of "helper" vars!
'''
a = [L[3][0][0], L[3][1][0]]
print(a)
N = [L[0], L[2][1],L[2][2], a, L[4][0], L[4][-1]]
print(N)

#print("end of 1") # set breakpoint here 
'''


























L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print("L is", L)
tmp1 = L[0] # 0
tmp2 = L[2][1] # 2
tmp3 = L[2][2] # 3
tmp4 = [L[3][0][0], L[3][1][0]] # [5, 6]
tmp5 = L[4][0] # 8
tmp6 = L[4][-1] # 10 
newL = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6] # create final list
print(newL) # [0, 2, 3, [5, 6], 8, 10]
'''

# part 2
# Task: Break s into sentences (which end in a .), count them and print them out using a loop:
# result: (I truncated them with ...)
# there are 4 sentences:
# Python is an interpreted, high-level, general-purpose programming language
#  Created by Guido van Rossum and first released in 1991, Python ...
#  Its language constructs and object-oriented approach aim to help programmers ...
#print("start of part 2") # set breakpoint here
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# your code here
'''
#1st attempt - attempted to use formatting to split sentences 
#print(s{.end="."}.format()) -- did not work 

#2nd attempt -trying to use for loops 
#for x in s:
    #if x end= "."
    #print(x) #second attempt, did not work.

#3rd attempt - trying to use slice, realized slice can only be used with int  
#print(s["Python":"."])

#4th attempt. Tried to explore the "three quotes" but did not seeem to work
#a = """s"""
#print(a)

#5th attempt
'''
sen = s.split(".")
print(sen)

for l in sen:
    print(l)

#print("end of 2") # set breakpoint here 
'''




























s = "Python is an interpreted, high-level, general-purpose programming language."
sentence_list = s.split('.')
print("there are", len(sentence_list), "sentences:")
for e in sentence_list:
    print(e)
'''
# part 3
# Task: 
# - break s into a list of words (i.e. now separated by space)
# - print out the word list (with a loop) so that every 2. word is in full uppercase.
# - optionally remove all periods and commas
# result:
# Python
# IS
# an
# INTERPRETED
# high-level
# GENERAL-PURPOSE
# programming
# LANGUAGE
#print("start of part 3") # set breakpoint here
# your code here

s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

'''
#1st attempt - using for loop
#for t in s:
    #print(t)


#2nd attempt - split + range 
#s.split()
#l = s.split()
#print(l)
#for num in range(3,-1,2): #pretty sure this part is not correct
    #print(num)


#3rd attempt 
#s.split()
#l = s.split()
#print(l.upper())  #realzied that .upper is for strings, not list

#4th attempt 
#l = s.split()
#a = print(l[::2])
#a = ['Python', 'an', 'high-level,', 'programming', 'Created', 'Guido', 'Rossum', 'first', 'in', "Python's", 'philosophy', 'code', 'with', 'notable', 'of', 'whitespace.', 'language', 'and', 'approach', 'to', 'programmers', 'clear,', 'code', 'small', 'large-scale']
#text_file = print("\n".join(a))
#type(text_file) #it would not let me run .upper directly so I had to check the type, it's showing NoneType.

#5th attempt 
#l = s.split()
#a = print(l[::2])
#a = ['Python', 'an', 'high-level,', 'programming', 'Created', 'Guido', 'Rossum', 'first', 'in', "Python's", 'philosophy', 'code', 'with', 'notable', 'of', 'whitespace.', 'language', 'and', 'approach', 'to', 'programmers', 'clear,', 'code', 'small', 'large-scale']
#b = [a[0],a[1],a[2][0:10],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15][0:10],a[16],a[17],a[18],a[19],a[20],a[21][0:5],a[22],a[23],a[24]]
#print(b)
#print("\n".join(b))

#e = print("\n".join(b))

#print(e.upper()) #tired structure data by getting rid of "," and ".", still says NoneType.

'''
#6th attempt BOOLEAN! with for loop

split_words = s.split()
print(split_words)
t = True
for i in split_words:
    # CH: as the 2 replaces have to be done for both True/False cases,
    # it's better to do this here
    # this also would alow you to have more replaces e.g. maybe you get a list of puntuation chars
    # and need to run through a battery of replaces in a for loop ...
    
    if t == True:
        print(i.replace(",","").replace(".",""))
        t = False
    else:
        print(i.upper().replace(".","").replace(",",""))
        t = True
    





#print("end of 3") # set breakpoint here 
'''


























# version 1 - using 1/-1
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = -1  # we start with 1 for normal print-out, then flip -1 for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == 1:
        print(w.upper())
    else:
        print(w)
    make_upper *= -1 # flip from 1 to -1 or vice versa

# version 2 - using 
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = False  # we start with False for normal print-out, then flip to True for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == True:
        print(w.upper())
        make_upper = False # it's currently True, so set to False
    else:
        print(w)
        make_upper = True # it must currently be False, so set to True
'''

# part 4
# task: abbreviate a potentially long string s to have the x first and x last chars with ... in between
# for x = 5 this would be: "A very long description" => "A ver...ption" (... is called filler)
# in a loop, set x from 5 to and to 15 and print out x and the abbreviated version 
# there'll be an issue where the result would actually be longer(!) than the un-abbreviated s. 
# For these cases, do not perform your abbreviation, simply print out s. Note that this
# should work for any other string a or filler as well, so don't hardcode things!
# 
# Optional:
# write a general function abbr(s, filler="...", total_width=15) which abbreviates s
# to total_width chars and uses the string filler in between them. Again, make sure the
# result would not be longer than s!
# call your function a couple of times with different parameters and also test edge cases
#print("start of part 4") # set breakpoint here
# a long string
s = "A very long description"
filler = "..."
# your code here
'''
#x = 5
# print(s[0:5] + filler + s[-6:-1]) - end indexing is not correct 


#x = 5
#print(s[0:5] + filler + s[-5:]) - this one is correct 
'''

for x in range(5,15):
    if x * 2 + len(filler) > len(s):
        print(x, s)
    else:
        abbr = (s[0:x] + filler + s[-x:])
        print(x,abbr)

# CH: very good! Now try to not use 5 and 15 and that specific string but rather the the len() of a string and work out those 2
# numbers from that. After that it should work with say s="An even longer description, yes, very long, indeed!"  
        
'''
#optional portion 
#s = "A very long description
#def abbr_s = (s, filler="...", total_width=15):
    #print(s[0:x] + filler + s[-x:])
    #abbr_s() 
    
#attempted but still need more knowledge on function overall to be able to pull this off

# CH: maybe do this now, after we've had a lecture on functions?
'''
#print("end of 4") # set breakpoint here 
'''































s = "A very long description" # a long string
filler = "..."
for x in range(5, 15):
    # check if abbreviation would be longer than s
    if x * 2 + len(filler) > len(s):
        print(x, s)
    else:
        abb_str = s[0:x] + filler + s[-x:] # slice off ends and glue together with filler chars
        print(x, abb_str)



def abbr(s, filler="...", total_width=15):
    #returns a copy of s abbreviated to total_width with filler in the middle
    x = total_width // 2 # integer division
    rem = total_width % 2 # remainder will be 1 if width is odd
    abb_str = s[0:x+rem] + filler + s[-x:] # for odd width, add one to front
    if len(abb_str) > len(s):
        return s
    return abb_str

# Test
s = "A very long description"
for tw in range(5, len(s)+1):
    print(tw, abbr(s, "...", tw))

# Edge cases
print(abbr("", "...", 0))
print(abbr("", "...", 999))
print(abbr("", "", 0))
print(abbr("", "", 999))
print(abbr("test", "...", 0))
print(abbr("test", "...", 999))
print(abbr("test", "", 0))
print(abbr("test", "", 999))
print(abbr("A very long description", "....................................", 999))
print(abbr("A very long description", "....................................", 0))
'''
