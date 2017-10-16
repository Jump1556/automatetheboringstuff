#! /usr/bin/env python3
# random_quiz_files.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_num in range(35):
    quiz_file = open('capitalsquiz%s.txt' % (quiz_num +1), 'w')
    answer_key = open('capitalsquiz_anwsers%s.txt' % (quiz_num +1), 'w')

quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz_num +1))
quiz_file.write('\n\n')

states = list(capitals.keys())
random.shuffle(states)

for quiz_num in range(50):
   correct_answ = capitals[states[question_num]]
   wrong_answ = list(capitals.values())
   del wrong_answ[wrong_answ.index(correct_answ)]
   wrong_answ = random.sample(wrong_answ, 3)
   anws_options = wrong_answ + [correct_answ]
   random.shuffle(anws_options)

 # TODO: Write the question and answer options to the quiz file.

# TODO: Write the answer key to a file.