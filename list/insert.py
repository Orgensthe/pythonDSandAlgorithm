def solution1(L, x):
    answer = []

    while L:
        temp = L.pop(0)
        if temp < x:
            answer.append(temp)
        else:
            answer = answer + [x] + [temp] + L
            break
            
    temp = answer.pop()
    
    if temp < x :
        answer.append(temp)
        answer.append(x)
    else:
        answer.append(temp)
    return answer

print(solution1(	[20, 37, 58, 72, 91], 65))



def solution2(L, x):
    answer = []

    while L:
        temp = L.pop(0)
        if temp < x :
            answer.append(temp)
        else:
            if x in answer:
                answer.append(temp)
            else:
                answer.append(x)
                answer.append(temp)

    if x not in answer:
        answer.append(x)
    return answer