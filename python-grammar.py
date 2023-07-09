print("hello world")
s = ['a']
for i in range(5):
    #append(アペンド)は最後に追加できる
    s.append(chr(ord(s[i]) + 1))
print(s)
#insertで指定した場所に追加できる
s.insert(0, 'i')
print(s)
#popは指定した配列番号を消してくれる
s.pop()
print(s)
s.pop(0)
print(s)

a = []
b = []

for i in range(5):
    a.append(i + 1)
    b.append(i + 6)

a += b
print(a)

#indexは何番目に数字や文字があるのかを返してくれる
print(a.index(1))

if 90 in a:
    print(a.index(90))

s = 'My name is Mike'
to_split = s.split()
print(to_split)

#joinは与えられた文字にしたかってリストを結合していく
x = '$$$'.join(to_split)
print(x)
