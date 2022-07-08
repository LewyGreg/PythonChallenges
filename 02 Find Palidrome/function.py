def isPalindrome(expression):
    if isinstance(expression, str):
        print("input expression: \'",expression,"\' is correct")
        cleanExpressionForward = list()
        cleanExpressionBackward = list()
        for character in expression:
            if character.isalpha():
                cleanExpressionForward.append(character)
        print(cleanExpressionForward)
        for character in reversed(expression):
            if character.isalpha():
                cleanExpressionBackward.append(character)
        print(cleanExpressionBackward)
        if cleanExpressionBackward == cleanExpressionForward:
            return True
        else:
            return False
    else:
        print("input is not valid string")




isPalindrome(10)

print(isPalindrome("kajak"))