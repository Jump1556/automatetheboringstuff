import os

#example for Windows
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
#C:\Users\asweigart\accounts.txt
#C:\Users\asweigart\details.csv
#C:\Users\asweigart\invite.docx


#example for OS
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/:/Users/asweigart', filename))
