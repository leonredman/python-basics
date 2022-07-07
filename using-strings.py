# using strings - mad libs game
#A 'Mad Libs' style game where user enters nouns,
#verbs, etc., and then a story using those words is ouput.

#Get user's words
relative = input('Enter a type of relative: \n')
food = input('Enter a type of food: \n')
adjective = input('Enter an adjective: \n')
period = input('Enter a time period: \n')

#Tell the story
print('My', relative, 'says eating', food)
print('will make me more', adjective)
print('so now I eat it every', period)

