#this is a Program that prints out numbers 1 to 100
twodivisors = [3, 5]
#these are the words that will be printed
# if the number is divisible by 3, it prints Crackle
#if the number is divisible by 5, it prints Pop
#if the number is divisible by 3 and 5, it prints CracklePop
wordstoprint = ['Crackle' , 'Pop']
twodivisors_wordstoprint = dict(zip(twodivisors,wordstoprint))
for i in range(101):
    print (i)
    for threeandfive in twodivisors:
        if i % threeandfive == 0:
            print (twodivisors_wordstoprint[threeandfive],
sep= '' , end='')
            print('', end='\n')


