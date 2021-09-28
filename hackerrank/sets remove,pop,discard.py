n =int(input())
s =set(input().split())
num= int(input())
for i in range(num):
     string=input()
     if (string.find('remove') >= 0):
      b=int()
      s.remove(b)

     elif(string.find('discard')>=0):
      c=int()
      s.discard(c)
     elif(string.find('pop')>=0):

      s.pop(-1)

print(s)

 # elif (inp.find('remove') >= 0):
 #    b = inp[7:]
 #    b = int(b)
 #    l.remove(b)
 # elif (inp.find('print') >= 0):
 #    print(l)
 # elif (inp.find('append') >= 0):
 #    c = inp[7:]
 #    c = int(c)
 #    l.append(c)
 #
 # elif (inp.find('pop') >= 0):
 #    l.pop(-1)
 # elif (inp.find('reverse') >= 0):
 #    l.reverse()
 # elif (inp.find('sort') >= 0):
 #    l.sort()