# Write your solution here

patterns = []
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Get your number of layers
number = int(input("Layers: "))
if 2<=number<=26:

    for size in range(number):
        # update more layer with latest character or pattern horizontally
        for pattern_indx in range(len(patterns)):
            # old layers become the internal laer
            mid_pattern = patterns[pattern_indx]
            # current character become outer layer 
            side_pattern = alphabets[size]
            # srround them internal layer with outer layer till the end of a pattern
            patterns[pattern_indx] = side_pattern + mid_pattern + side_pattern
        

        # get and update new layers from the bottom
        patterns.append((2*size+1)*alphabets[size])

        # mirror latest character layer from bottom to the top vertically
        if size != 0:
            patterns.insert(0, (2*size+1)*alphabets[size])


    # print all the pattern
    for pattern in patterns:
        print(pattern)