phrase="Don't panic!"
plist=list(phrase) #mengubah string ke list
print(phrase)
print(plist)

for i in range(4):
    plist.pop() #menghapus 4 karakter terakhir dengan loop

plist.pop(0) #menghapus indeks ke-0 yaitu 'D'
plist.remove("'") #menghapus karakter " ' "
plist.extend([plist.pop(),plist.pop()]) # meng swap karakter p dan a
plist.insert(2,plist.pop(3)) #memindahkan spasi

new_phrase=''.join(plist) #mengubah list ke string
print(plist)
print(new_phrase)
