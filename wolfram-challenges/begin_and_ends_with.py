# Problem: https://challenges.wolframcloud.com/challenge/words-beginning-and-ending-with-a-given-letter

from typing import List


def same_start_end_words(letter: str, wordlist: List[str]) -> List[str]:
    results = []

    for word in wordlist:
        if word.startswith(letter) and word.endswith(letter):
            results.append(word)
    return results


if __name__ == '__main__':
    wordlist = ['brian', 'baobab', 'barb', 'year', 'yucky', 'today', 'yes', 'nowhere']
    res = same_start_end_words('b', wordlist)
    print(res)
