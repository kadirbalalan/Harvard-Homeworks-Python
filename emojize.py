import emoji
emo = input("Input: ")
out = emoji.emojize(emo, language="alias")
print("Output:" , out)