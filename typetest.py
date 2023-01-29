import random, time 
words = ["girl", "not", "how", "is", "soon", "then", "big", "those", "list", "more", "three", "saw", "often", "put"]
test = ' '.join(random.choices(words, k=20))
print(test)
start = time.time()
type = input("type: ")
end = time.time()
total_time = end - start
wpm = round(len(test) / 5 / total_time * 60,1)
fails = []
errors = []
typed = 0
for word, guess in zip(test.split(), type.split()):
    if word != guess:
        fails.append(f"{word} {guess!r}")
        errors.append(word)
    else:
        fails.append(word)
    typed += 1
print(f"\n{' '.join(fails)}")
c = len(test) - len(' '.join(errors))
precision = round((c / len(test)) * 100,2)
wpm_total = round(wpm * (precision / 100), 1)
if typed != len(test.split()):
    print("\nyou haven't type enough words")
else:
    print(f"\n(Net | Gross): {wpm_total}|{wpm} in {round(total_time,2)} Seconds - Acurracy {precision}%")
