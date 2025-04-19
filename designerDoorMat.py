def designer_door_mat(n, m):
    for i in range(1, n, 2): # start at one going by two (staying odd) to maintain symmetry
        patter = ('.|.' * i).center(m, '-')
        print(patter)
    
    print('WELCOME'.center(m, '-'))

    for i in range(n-2, 0, -2):
        patter = ('.|.' * i).center(m, '-')
        print(patter)



designer_door_mat(7, 21)