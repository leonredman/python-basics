'''
Complete the following program using functions from the table above to 
find some statistics about basketball player Lebron James. The code 
below provides lists of various statistical categories for the years 
2003- 2013. Compute and print the following statistics:

Total career points
Average points per game
Years of the highest and lowest scoring season
'''
#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
total_career_points = 0
total_career_points = sum(points)
print(total_career_points)

# Print Average PPG
average_PPG = 0
average_PPG = total_career_points / len(points)
print(average_PPG)

# Print best scoring year
max_points = max(points)
high_year_index = points.index(max_points) + 1
print('Highest scoring year:',high_year_index, '- max points:', max_points)


# Print worst scoring year
least_points = min(points)
low_year_index = points.index(least_points) + 1
print('Lowest scoring year:', low_year_index, '-low points:', least_points)

'''
yeild:
21081
2108.1
Highest scoring year: 3 - max points: 2478
Lowest scoring year: 1 -low points: 1654

'''


