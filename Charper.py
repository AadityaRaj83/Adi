def count_char(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
    return count
file = open("textadi.txt","w")
file.write("""hduehdjsdmnsdhfurhfbnbdofehiosbcbbfrhowieoueihdcbdbdbcncbjrhjhf
ewfdhfrfhiojksakjbdhkjfgeigiwoqopwqpwlssmmzjkewgdegdbcnbndbcjkjkehjkdhbndbbejkdbejeb
dbuiehieioewuopuryrtsbakpoqisnxbcxzbmcbifheworueuhdmnbasamnbxasjhqhdeiqehihdiehdehdsmndbsmsbkjehopeqpoahzsmcbdkhoichhjkhcjdgweiyioywopqpm
adbjkhdjkehoiewoirioewhkbcxnxbcmzbwiupqlamznxbcvqowueyrtrhfjdkdhfjgddd""")
file.close()
filename="textadi.txt"
with open(filename) as f:
    text=f.read()

for char in "abcdefghijklmnopwrstuvwxyz":
    perc=100 * count_char(text,char)/len(text)
    print("{0} - {1}%".format(char,round(perc,2)))

