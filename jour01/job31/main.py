notes = [98,58,44,78]
def Calcul(notes) :
    for i in range (0,len(notes),1) :
        # print(notes[i])
        if notes[i]>=40:
            reg = 100 - notes[i]
            # print(r)
            # print(notes[i])
            div = reg % 5

            if(div < 3) :

                notes[i] = notes[i] + div

    return(notes)

print(Calcul(notes))