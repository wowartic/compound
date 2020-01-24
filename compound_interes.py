def compound(cash, interest, time):
    for i in range(time):
        cash = cash * interest
        print(cash)


cash = 7
interest = 1.02
time = 356

compound(cash, interest, time)
