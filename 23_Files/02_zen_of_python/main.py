import this

zen_list = open('zen.txt', 'r')
bask_list = ''
for i_word in zen_list:
    bask_list = i_word + bask_list
print(this)
zen_list.close()
