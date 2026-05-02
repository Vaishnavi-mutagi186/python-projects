import time

sentence = "Python programming is fun and powerful"

print("Typing Speed Test")
print("-------------------")
print("Type the following sentence:\n")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(sentence.split())

speed = (words / time_taken) * 60

print("\nTime taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(speed, 2), "WPM")

if typed_text == sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Some mistakes")