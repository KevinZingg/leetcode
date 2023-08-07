import re

txt = "The rain in Spain"

x = re.search("Spa", txt)
y = re.findall("ai", txt)
z = re.findall("Portugal", txt)
a = re.search("\s", txt) #WhiteSpace
b = re.split("\s", txt)


print(x)
print(y)
print(z)
print(a)
print("The first white-space character is located in position:", a.start())
print(b)



'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group


https://www.w3schools.com/python/python_regex.asp

'''