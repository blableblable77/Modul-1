    
num=[5, 3, 2, 8, 1, 4]
odd=[] 
even=[]
result1=[]  # 
result2=[] #
result=[] #untuk menampung semua angka ganjil genap
for i in num:
    if ( i% 2 ) == 0: 
            even.append(i)  #untuk menampung angka genap
    else :
            odd.append(i) #untuk menampung angka bukan genap

odd.sort() #mengurutkan angka ganjil dari terkecil
even.sort(reverse=True) #mengurutkan angka genap dari terkecil lalu direverse

for i in range(len(num)): 
    list=num[i]
    if list % 2== 0:
        result1.append(even[0])
        even.pop(0)
    else: 
        result1.append('')

for i in range(len(num)):
    list = num[i]
    if list %2!=0:
        result2.append(odd[0])
        odd.pop(0)
    else:
        result2.append('')
print(result1)
print(result2)
result1[0]=result2[0]
result1[1]=result2[1]
result1[4]=result2[4]
result.append(result1)

print(result)

    
    

