

def repeat_message(msg, n):

    for i in range(n):
        print(msg)
    

def is_triangle_number(n):
    res = 0

    for i in range(1, n+1):
        res += i
    
    if res % 3 == 0:
        return True
    else:
        return False

def print_odds_down(n):
    
    for i in range(n, 0, -1):
        if n <= 0:
            break
        if n % 2 == 0:
            continue
        else:
            print(n)
            n -= 2


def rate_username(username):
    if not username:
        return "Invalid"
    elif username.isalpha():
        return "Poor"
    elif username.isalnum():
        return "Good"
    else:
        return "Excellent"

def mirror_sentence(sentence):
    sentence = sentence.strip().split()
    return " ".join(sentence[::-1])


