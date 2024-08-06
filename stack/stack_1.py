def check_match(expression):
    stack =[] #스택
    #괄호 짝으로 딕셔너리를 생성을 함
    matching_dict ={')':'(', '}': '{', ']': '['}

    # 입력받은 문자열을 순회
    for ch in expression:
        # 열린 괄효를 만날 때
        if ch in matching_dict.values():
            stack.append(ch)
        elif ch in matching_dict.keys():
            #스택이 비어있거나 짝이 없으면
            if not stack or stack[-1] != matching_dict[ch]:
                return False
            #스택에서 꺼낸다
            stack.pop()
    return not stack # 스택이 남아 있으면 짝이 안맞는 걸로 간주
example = ['(a(b)','a(b)c)', 'a{b(c[d]e}f)']
for ex in example:
    if check_match(ex):
        print(f'{ex}는 올바른 괄호')
    else:
        print(f'{ex}는 올바르지 않은 괄호')