def function(i=32, j=0):

    if i > 127:
        return
    else:
        j += 1
        print(f'{i} - {chr(i)}', end=" ")
        if j == 10:
            print(" ")
            function(i + 1, j=0)
        else:
            function(i + 1, j=j)


function()