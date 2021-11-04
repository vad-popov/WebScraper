unit = int(input())
if unit < 1:
    print('no army')
elif unit < 10:
    print('few')
elif unit < 50:
    print('pack')    
elif unit < 500:
    print('horde')
elif unit < 1000:
    print('swarm')    
else:
    print('legion')
