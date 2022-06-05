def find_anagrams(string1, string2):
# Strings are sorted and verified
    if(sorted(string1)== sorted(string2)):
        print("True")
    else:
         print("False")

string1 ="EARTH"
string2 ="HEART"

print( "String value1 : ", string1 )
print( "String value2 : ", string2 )

find_anagrams(string1, string2)