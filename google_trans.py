from googletrans import Translator
x = Translator()
text1 = input("Enter any text:")
text2 = input("Target language:")
res = x.translate(text1,dest=text2)
print("The Original:",text1)
print("The Translation:",res)

