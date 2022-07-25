# iterating over a dict
'''
Write a loop that prints each country's population in country_pop. Sample output for the given program:
United States has 318463000 people.
India has 1247220000 people.
Indonesia has 252164800 people.
China has 1365830000 people.
'''

country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
} # country populations as of 2014


for country,pop in country_pop.items():
    print(country, 'has', pop, 'people.')

    '''
    Output:
    China has 1365830000 people.
India has 1247220000 people.
United States has 318463000 people.
Indonesia has 252164800 people.
'''