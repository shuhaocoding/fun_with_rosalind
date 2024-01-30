# Given a string s, and a substring t
s,t = input().split()
l = []
# Initialize the position of the substring
pos = 0
# Start a loop to count all the occurrences of the substring
while True:
    try:
        new_pos = s.index(t)+1 # Find the substring
        pos += new_pos # Update the substring index
        l.append(str(pos)) # Generate a list of substring positions
        s = s[new_pos:] # Truncate the previous string for the next search
    except:
        print(' '.join(l))
        break # Break the loop when there is no substring to find