l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a true." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for false.")
else:
    print("%s is a false." % l)
