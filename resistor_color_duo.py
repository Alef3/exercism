def value(colors):
    
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    
    result = map(lambda i : str(all_colors.index(i)), colors[:2])
    
    return int(''.join(result))