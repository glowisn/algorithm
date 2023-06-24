str = input()
for st in str:
    if st.islower():
        print(st.upper(),end='')
    elif st.isupper():
        print(st.lower(),end='')