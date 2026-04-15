# Processes a list of African city populations (in millions) and finds the top 3
populations = [21.0, 5.0, 15.4, 3.2, 10.0, 7.8, 4.5]

# Initialize a list to hold the top 3 largest populations
top_3 = [0, 0, 0]

for pop in populations:
    if pop > top_3[0]:
        top_3[2] = top_3[1]
        top_3[1] = top_3[0]
        top_3[0] = pop
    elif pop > top_3[1]:
        top_3[2] = top_3[1]
        top_3[1] = pop
    elif pop > top_3[2]:
        top_3[2] = pop

print(f"The top 3 largest city populations (in millions) are: {top_3}")
