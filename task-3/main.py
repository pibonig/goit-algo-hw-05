import timeit
from collections import defaultdict

# Читання текстових файлів
with open('./стаття 1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('./стаття 2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()


# Алгоритми пошуку
class StringMatchingAlgorithms:
    @staticmethod
    def knuth_morris_pratt(text, pattern):
        def kmp_table(pattern):
            table = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                if pattern[i] == pattern[j]:
                    j += 1
                    table[i] = j
                else:
                    if j != 0:
                        j = table[j - 1]
                        i -= 1
                    else:
                        table[i] = 0
            return table

        table = kmp_table(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = table[j - 1]
                else:
                    i += 1
        return -1

    @staticmethod
    def rabin_karp(text, pattern):
        d = 256
        q = 101
        n = len(text)
        m = len(pattern)
        h = 1
        p = 0
        t = 0

        for i in range(m - 1):
            h = (h * d) % q

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for i in range(n - m + 1):
            if p == t:
                if text[i:i + m] == pattern:
                    return i

            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t += q

        return -1

    @staticmethod
    def boyer_moore(text, pattern):
        def bad_char_table(pattern):
            table = defaultdict(lambda: -1)
            for i in range(len(pattern)):
                table[pattern[i]] = i
            return table

        bad_char = bad_char_table(pattern)
        m = len(pattern)
        n = len(text)
        s = 0

        while s <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            if j < 0:
                return s
            else:
                s += max(1, j - bad_char[text[s + j]])
        return -1


if __name__ == "__main__":
    # Підрядки для пошуку
    existing_substring = "алгоритми"
    non_existing_substring = "вигаданий"

    # Вимірювання часу роботи алгоритмів
    algorithms = [
        ('Knuth-Morris-Pratt', StringMatchingAlgorithms.knuth_morris_pratt),
        ('Rabin-Karp', StringMatchingAlgorithms.rabin_karp),
        ('Boyer-Moore', StringMatchingAlgorithms.boyer_moore),
    ]


    def measure_time(algorithm, text, pattern):
        return timeit.timeit(lambda: algorithm(text, pattern), number=10)


    results = {}

    for name, algorithm in algorithms:
        results[name] = {
            'Text 1 (Existing)': measure_time(algorithm, text1, existing_substring),
            'Text 1 (Non-Existing)': measure_time(algorithm, text1, non_existing_substring),
            'Text 2 (Existing)': measure_time(algorithm, text2, existing_substring),
            'Text 2 (Non-Existing)': measure_time(algorithm, text2, non_existing_substring),
        }

    # Визначення найшвидшого алгоритму
    for text_key in ['Text 1 (Existing)', 'Text 1 (Non-Existing)', 'Text 2 (Existing)', 'Text 2 (Non-Existing)']:
        best_algorithm = min(results.keys(), key=lambda k: results[k][text_key])
        print(f"{text_key}: Найшвидший алгоритм - {best_algorithm}")

    # Висновок в Markdown форматі
    with open('./results.md', 'w', encoding='utf-8') as f:
        f.write("# Порівняння ефективності алгоритмів пошуку підрядка\n\n")
        for name, result in results.items():
            f.write(f"## {name}\n")
            for text_key, time in result.items():
                f.write(f"- {text_key}: {time:.6f} секунд\n")
            f.write("\n")
        f.write("## Висновки\n")
        for text_key in ['Text 1 (Existing)', 'Text 1 (Non-Existing)', 'Text 2 (Existing)', 'Text 2 (Non-Existing)']:
            best_algorithm = min(results.keys(), key=lambda k: results[k][text_key])
            f.write(f"- {text_key}: Найшвидший алгоритм - {best_algorithm}\n")

    print("Аналіз завершено. Результати збережено у файлі results.md.")
