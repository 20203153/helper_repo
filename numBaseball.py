def prob_3(target, input):
    b, s = 0, 0
    for idx in range(len(input)):
        if input[idx] == target[idx]:
            s+=1
        elif input[idx] in target:
            b += 1
    return f'{s}S{b}B' if b+s else 'OUT'


# OUT
# {}S{}B
print("Expected: 1S1B <->", prob_3("123", "325"))
print("Expected: OUT <->", prob_3("123", "999"))
print("Expected: 3S0B <->", prob_3("123", "123"))
print("Expected: 0S3B <->", prob_3("123", "231"))








