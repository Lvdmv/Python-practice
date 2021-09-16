def cipher(i_word):
    rew_word = []
    for i_ch in i_word:
        if i_ch.isalpha():
            rew_word.append(alphabet[(alphabet.index(i_ch) - 1)])
        else:
            rew_word.append(simbol[(simbol.index(i_ch) - 1)])
    return ''.join(rew_word)

def alpha(i_word, k):
    new_list = list(i_word[::-1])
    for i in new_list[:k]:
        if i != '(':
           new_list.append(new_list[0])
           new_list.remove(new_list[0])
        else:
            new_list.remove(i)
            new_list.append("'")
    i_word = new_list[::-1]
    return ''.join(i_word)

def revers(i_elem, k):
    if i_elem.islower():
        j.append(alpha((cipher(i_elem)), k % len(i_elem)))
    else:
        j.append(alpha((cipher(i_elem.lower())), k % len(i_elem)).title())




alphabet = 'abcdefghijklmnopqrstuvwxyz'
simbol = '(,-!",-*+-./('
cipher_text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
              'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
              'fTjnqm tj scfuuf ibou fy/dpnqm ' \
              'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
              'uGmb tj fuufsc ouib oftufe/ ' \
              'bstfTq jt uufscf uibo otf/ef ' \
              'uzSfbebcjmj vout/dp ' \
              'djbmTqf dbtft ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
              'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
              'Fsspst tipvme wfsof qbtt foumz/tjm ' \
              'omfttV mjdjumzfyq odfe/tjmf ' \
              'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
              'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
              'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv i/Evud ' \
              'xOp tj scfuuf ibou /ofwfs ' \
              'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
              'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
              'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
              'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. futm pe psfn gp tf"uip'

j = []
k =3
new_word = []
for i_elem in cipher_text.split():
    revers(i_elem, k)
    if '/' in i_elem:
        k += 1

print(('.\n'.join((' '.join(j)).split('.'))))



