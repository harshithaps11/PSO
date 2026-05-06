def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare (case insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Take input
s = input("Enter string: ")

if isPalindrome(s):
    print("Valid Palindrome")
else:
    print("Not a Palindrome")