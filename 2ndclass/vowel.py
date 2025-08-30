def vowe(str):
    vow = "AEIOUaeiou"
    count=0
    for ch in str:
        if ch in vow:
            count+=1
    print("total count is:",count)
    if count != 0:
        print("vowel pst in string")
    else:
        print("not pst vow in str")
lin = input("Enter string is: ")
vowe(lin)
