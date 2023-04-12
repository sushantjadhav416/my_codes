letter='''Dear <|Name|>,
you are selected

Date:<|date|>'''
Name=input("Enter the name:")
date=input('Enter teh date:')
letter=letter.replace("Name",Name)

letter=letter.replace("date",date)
print(letter)
print(letter.find("  "))