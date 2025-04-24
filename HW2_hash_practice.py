import matplotlib.pyplot as plt

def count_words(filepath):
    word_count = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

filename = "/Users/kai/Desktop/資料結構/HW2/hw2_data.txt"
word_count = count_words(filename)

print(f"不重複的英文字數量：{len(word_count)}")

for word, count in word_count.items():
    print(f"{word}: {count}")

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

words = [item[0] for item in sorted_words]
counts = [item[1] for item in sorted_words]

words = words[:30]
counts = counts[:30]

plt.figure(figsize=(12, 6))
plt.bar(words, counts, color='skyblue')
plt.xticks(rotation=90)
plt.xlabel("英文單字")
plt.ylabel("出現次數")
plt.title("英文字出現頻率直方圖")
plt.tight_layout()
plt.show()