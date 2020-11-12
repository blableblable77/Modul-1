def hollowTriangle(h):

    for i in range(h): #untuk membuat baris awal

        if i < 1:
            print('__'*(h-1)+'#', end='_'*(h-1))
            print()
        elif i < (h-1): #untuk membuat baris tengah

            for j in range (h-(i+1)):
                print('_', end=' ')
            print('#', end='_')

            for j in range ((i*2)-1):
                print('_', end=' ')
            print('#',end ='_')
            print()
        else: #untuk membuat baris akhir
            print('# '*((h*2)-1))

hollowTriangle(8)