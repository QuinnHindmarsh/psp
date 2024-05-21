secs = int(input('enter the number of seconds: '))

if secs < 0 and secs >= 100:
    print('first stage')
elif secs > 100 and secs <= 170:
    print('second stage')
elif secs > 170 and secs <= 260:
    print('third stage')
    
