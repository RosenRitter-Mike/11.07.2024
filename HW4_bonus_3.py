sentence: str = "";
while True:
    str1: str = input("String 1: ");
    str2: str = input("String 2: ");
    if str1 == str2:
        break;
    else:
        sentence+=f"{str1} {str2} ";

print(sentence.strip());
