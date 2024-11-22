# Solutions (Try to solve before looking!):

def solution1():
    # Using Counter
    from collections import Counter
    return Counter(words)

def solution2():
    # Using get()
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

def solution3():
    # Using defaultdict
    from collections import defaultdict
    vote_counts = defaultdict(int)
    for vote in votes:
        vote_counts[vote] += 1
    return vote_counts

def solution4():
    # Using Counter with most_common()
    from collections import Counter
    return Counter(grades).most_common()

def solution5():
    # Using get() method
    ip_freq = {}
    for ip in ip_addresses:
        ip_freq[ip] = ip_freq.get(ip, 0) + 1
    return ip_freq

def solution6():
    # Using comprehension with Counter
    from collections import Counter
    return Counter(len(word) for sentence in sentences for word in sentence.split())

def solution7():
    # Using Counter with list comprehension
    from collections import Counter
    return Counter(user for user, _ in events)

def solution8():
    # Using Counter with map
    from collections import Counter
    return Counter(map(lambda x: x.split('.')[-1], files))

def solution9():
    # Simple Counter
    from collections import Counter
    return Counter(status_codes)

def solution10():
    # Using Counter with generator expression
    from collections import Counter
    return Counter(category for category, _ in items)
