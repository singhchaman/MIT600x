c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c=c+1
print "Number of vowels:", c


c=0
for i in range(1,len(s)-1):
    if s[i-1:i+2]=='bob':
        c=c+1
print "Number of vowels:", c


curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest