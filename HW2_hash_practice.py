import matplotlib.pyplot as plt
from collections import Counter

# 讀取檔案並統計詞頻
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()  # 逐行讀取
    
    word_count = Counter(words)  # 使用 Counter 建立詞頻表
    return word_count

# 畫直方圖
def plot_histogram(word_count):
    sorted_words = word_count.most_common()  # 按頻率排序
    words, counts = zip(*sorted_words)  # 拆分為兩個 list
    
    plt.figure(figsize=(12, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xticks(rotation=90)  # 讓 x 軸標籤旋轉方便閱讀
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Word Frequency Histogram")
    plt.show()

# 主程式
if __name__ == "__main__":
    filename = "hw2_data.txt"
    word_count = count_words(filename)
    
    # 1. 總共有多少個不重複的英文字
    print(f"Total unique words: {len(word_count)}")
    
    # 2. 每個英文字的出現次數
    for word, count in word_count.items():
        print(f"{word}: {count}")
    
    # 3. 繪製直方圖
    plot_histogram(word_count)

