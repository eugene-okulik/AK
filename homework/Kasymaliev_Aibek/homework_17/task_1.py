import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path file")
parser.add_argument("--text", help="text if file")
args = parser.parse_args()

info = []

print("DEBUG: path =", args.path)
for file_name in os.listdir(args.path):
    print("DEBUG: found file:", file_name)
    file_path = os.path.join(args.path, file_name)
    if not os.path.isfile(file_path):
        continue
    try:
        with open(file_path, "r", encoding="utf-8") as log_text:
            for line_number, line in enumerate(log_text, start=1):
                words = line.strip().split()
                for i, word in enumerate(words):
                    if args.text in word:
                        start = max(0, i - 5)
                        end = i + 6
                        match_text = " ".join(words[start:end])
                        info.append((file_name, line_number, match_text))
                        print(f"Файл: {file_name}, Строка: {line_number}, Найденный текст: {match_text}")

    except Exception as e:
        print(type(e), e)
