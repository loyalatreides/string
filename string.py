letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello world'
print(greeting)
print(len(greeting))

multiline_string = '''My name is Kamran Habib. 
I enjoying learning new things.
along with playing football'''
print(multiline_string)

first_name = 'Kamran'
last_name = 'Habib'
full_name = 'Kamran' + ' ' + 'Habib'
print(full_name)

print('I hope all of you are interested in the class today. \nare you?')
print('How\tare\tyou\ttoday?')
print('Day 1\t3\t5')
print('Day 2\t2\t5')
print('Day 3\t2\t5')
print('Day 4\t2\t5')
print('This is a backslash symbol(\\)')
print('In every programming language starts with \"Hello, World\"')

#old format
#strings only
first_name = 'Kamran'
last_name = 'Habib'
langauge = 'Python'
formatted_string = 'I am %s,%s I study %s' %(first_name, last_name, langauge)
print(formatted_string)

#string and numbers
radius = int(10)
pi = float(3.14)
area = pi * radius ** 2
formatted_string = 'The area of the circle with a radius %d is %f' %(radius, area)
print(formatted_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formatted_string = 'Following are the python libraries %s' %(python_libraries)
print(formatted_string)

#new format
first_name = 'Kamran'
last_name = 'Habib'
language = 'Python'
formatted_string = 'I am {} {}. I study {}'.format(first_name, last_name, langauge)
print(formatted_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

#strings and numbers
radius = int(input('Enter the radius: '))
pi = float(3.14)
area = pi * radius ** 2
formatted_string = ('The area of the circle with radius {} is {}'.format(radius, area))
print(formatted_string)

#Python Strings as Sequence of Characters
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Accessing Characters in Strings by Python
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
third_letter = langauge[2]
print(third_letter)
fourth_letter = language[3]
print(fourth_letter)
fifth_letter = language[4]
print(fifth_letter)
sixth_letter = language[5]
print(sixth_letter)

second_last_letter = language[-2]
print(second_last_letter)

last_letter = language[-1]
print(last_letter)

#Slicing
language = 'Python'
slicing = language[0:3]
print(slicing)
slicing = language[2:6]
print(slicing)
slicing = language[3:]
print(slicing)
slicing = language[:4]
print(slicing)
slicing = language[-3:]
print(slicing)
slicing = language[:-4]
print(slicing)

#reversing string
greeting = 'Hello, World'
print(greeting[::-1])

#skipping characters while slicing
school_name = 'Hamdard Public School'
slicing_skipping = school_name[0:7:2]
print(slicing_skipping)

#capitalize()
challenge = 'thirty days of Python'
print(challenge.capitalize())

#count('enter substring')
challenge = 'Thirty days of Python'
print(challenge.count('y'))
print(challenge.count('a'))
print(challenge.count('t'))

#endswith()
challenge = 'Thirty days of Python'
print(challenge.endswith('on'))
print(challenge.endswith('da'))

#expandtabs()
challenge = 'Thirty\tdays\tof\tPython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))
print(challenge.expandtabs(30))

#find()
challenge = 'thirty days of python'
print(challenge.find('a'))
print(challenge.find('th'))
print(challenge.find('r'))

#rfind
challenge = 'Thirty days of Python'
print(challenge.rfind('o'))
print(challenge.rfind('n'))

#format()
first_name = 'Kamran'
last_name = 'Habib'
age = 25
job = 'Student'
Sentence = 'I am {} {}. I am {} years old and I am {}'.format(first_name, last_name, age, job)
print(Sentence)

radius = int(input('Enter radius of the circle: '))
pi = 3.14
area = pi * radius ** 2
print('Area of the circle with radius {} is {}'.format(radius, area))

#index()
challenge = 'Thirty days of Python'
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index(sub_string, 9)) #error

#rindex()
challenge = 'Thirty days of Python'
sub_string = 'da'
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string, 4))

#isalnum()
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysofPython'
print(challenge.isalnum())
challenge = '30 Days of Python'
print(challenge.isalnum())

#isalpha()
#isdecimal()
#isdigit()
#isnumeric()
#isidentifier
#islower()
#isupper()

#join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

#strip
challenge = '30 days of pythoooonn'
print(challenge.strip('on'))

#replace()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

#split()
challenge = 'Thirty days of Python'
print(challenge.split())
print(challenge.split('+'))

#title
challenge = 'thirty days of python'
print(challenge.title())

#swapcase()
challenge = 'thirty days of python'
print(challenge.swapcase())

#startswith()
challenge = 'Thirty days of python'
print(challenge.startswith('Thirty'))
print(challenge.startswith('30'))

#Exercises Day 4
#1
w1 = 'Thirty'
w2 = '\tDays'
w3 = '\tOf'
w4 = '\tPython'
sentence = w1 + w2 + w3 + w4
print(sentence)

#2
w1 = 'Coding' 
w2 = ' for'
w3 = ' all'
sentence = w1 + w2 + w3
print(sentence)

#3
company = 'Coding For All'
print(company) #4
print(len(company)) #5
company_1 = company.upper()
print(company_1) #6
company_2 = company.lower()
print(company_2) #7
company_3 = company.capitalize()
print(company_3) #8
company_4 = company.title()
print(company_4) #8
company_5 = company.swapcase()
print(company_5) #8
slicing = company[0:6]
print(slicing) #9

company = 'Coding For All'
find = 'Coding'
print(company.index(find)) #10
print(company.find(find)) #10
print(company.replace('Coding', 'Python')) #11 #12
print(company.split()) #13

#14
tech_comp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_comp.split())

#15
company = 'Coding for all'
print(company[0])
print(company[-1]) #16
print(company[10]) #17
#18 Skipped Acronym Parts
#19 Skipped Acronym Parts

company = 'Coding For All'
print(company.index('C')) #20
print(company.index('F')) #21
print(company.rfind('l')) #22

sentence = 'You cannot end a sentence with because because because is a conjuntion'
print(sentence.index('because')) #23
print(sentence.find('because')) #23
print(sentence.rindex('because')) #24
print(sentence[31:-15]) #25 #27
print(sentence.index('because')) #26

#28 #29 Skipped
sentence = '    Coding For All      '
print(sentence[4:-1]) #30

sentence = '30DaysOfPython'
print(sentence.isidentifier()) #31
sentence_2 = 'thirty_days_of_python'
print(sentence_2.isidentifier()) #31

#32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '#'.join(python_libraries)
print(result)

#33
one = 'I \nam \nenjoying \nthis \nchallenge.'
two = 'I \njust \nwonder \nwhat \nis \nnext'
print(one)
print(two)

#34
one = 'Name \tAge \tCountry \tCity'
two = 'Asabeneh \t250 \tFinland \tHelsinki'
print(one)
print(two)

#35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters sqaure.'.format(radius, area))

#36
num_1 = 8
num_2 = 6
result_1 = num_1 + num_2
result_2 = num_1 - num_2
result_3 = num_1 * num_2
result_4 = num_1 / num_2
result_5 = num_1 % num_2
result_6 = num_1 // num_2
result_7 = num_1 ** num_2
print('{} + {} = {}'.format(num_1, num_2, result_1))
print('{} - {} = {}'.format(num_1, num_2, result_2))
print('{} * {} = {}'.format(num_1, num_2, result_3))
print('{} / {} = {}'.format(num_1, num_2, result_4))
print('{} % {} = {}'.format(num_1, num_2, result_5))
print('{} // {} = {}'.format(num_1, num_2, result_6))
print('{} ** {} = {}'.format(num_1, num_2, result_7))
