def longest_substring(string):
    l = len(string)
    left = right = longest = 0
    store = {}
    longest_value = str()

    while right < l:
        letter = string[right]
        
        if letter not in store:
            store[letter] = True

            n = len(store)

            if n > longest:
                longest = n
                longest_value = ''.join(store.keys())
            
            right += 1
        else:
            value = string[left]
            del store[value]
            
            left += 1
    return longest_value, longest

if __name__ == '__main__':
    string = 'longestsubstring'
    result = longest_substring(string)
    print(result)
