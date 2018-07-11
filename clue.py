"""
alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alp = alp + alp
clue="g fmnc wms bgblr rpylqjyrc gr zw fylb rfyrq ufyr amknsrcpq ypc dmp bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle sqgle qrpgle kyicrpylq() gq pcamkkclbcb lmu ynnjw ml rfc spj"
clue=list(clue)

for i in clue:
   if i ==" ":
     print " ",
   elif i == "(":
     print "(",
   elif i == ")":
     print ")",
   else:
     print alp[(alp.index(i))+2],

"""

#second method

from string import maketrans

alp="abcdefghijklmnopqrstuvwxyz"
alp2=list(alp)

for i in range(2):
    alp2.insert(0,alp2.pop())
alp2="".join(map(str,alp2))
print alp
print alp2

trans=maketrans(alp2,alp)

clue="g fmnc wms bgblr rpylqjyrc gr zw fylb rfyrq ufyr amknsrcpq ypc dmp bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle sqgle qrpgle kyicrpylq() gq pcamkkclbcb lmu ynnjw ml rfc spj"

print clue.translate(trans)
