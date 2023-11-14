counter=0
charaters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             '~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+'
             ]

file_open = open('word.txt','w')

for i in charaters:
    for j in charaters:
        for k in charaters:
            for l in charaters:
                guess = str(i) + str(j) + str(k) + str(l)
                file_open.write(guess)
                file_open.write('\n')
                counter = counter+1
print("word of {} password created".format(counter))

