from collections import defaultdict

# Exercise 1: Basic Word Counting
print(" # Exercise 1: Basic Word Counting")
words = ['apple', 'banana', 'apple', 'cherry', 'date', 'banana', 'apple']
# Convert this:
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(word_counts)

#soln
d = {}
for word in words:
    d[word] = d.get(word, 0) + 1
print(d)

from collections import Counter
d = Counter(words)
print(d)

## ok, have the Counter, but stil
## cool, used the d.get method. word.
#---------------------------------------------#



# Exercise 2: Character Frequency
print()
print('# Exercise 2: Character Frequency')

text = "mississippi"
# Convert this:
char_freq = {}
for char in text:
    if char not in char_freq:
        char_freq[char] = 0
    char_freq[char] += 1
print(char_freq)

d = {}
for char in text:
    d[char] = d.get(char, 0) + 1
print(d)

d = Counter(text)
print(d)













# Exercise 3: Vote Counting
print()
print('# Exercise 3: Vote Counting')
votes = ['yes', 'no', 'yes', 'abstain', 'yes', 'no', 'yes']
# Convert this:
vote_counts = {}
for vote in votes:
    if vote not in vote_counts:
        vote_counts[vote] = 0
    vote_counts[vote] += 1
print(vote_counts)


d = {} # use a dict to hold the counts for the votes.
for vote in votes:
    d[vote] = d.get(vote, 0) + 1
print(d)

d = { vote : d.get(vote, 0) for vote in votes } # are dict comps idiomatic?
print(d)                                        # not for counting, but for transforms

d = Counter(votes)
print(d)
















# Exercise 4: Grade Distribution
print()
print('# Exercise 4: Grade Distribution')
grades = ['A', 'B', 'A', 'C', 'B', 'A', 'F', 'D', 'A', 'C']
# Convert this:
grade_dist = {}
for grade in grades:
    if grade not in grade_dist:
        grade_dist[grade] = 0
    grade_dist[grade] += 1
print(grade_dist)

d = {}
for grade in grades:
    d[grade] = d.get(grade, 0) + 1
print(d)

d = Counter(grades)
print(d)







# Exercise 5: IP Address Frequency
print()
print('# Exercise 5: IP Address Frequency')

ip_addresses = ['192.168.1.1', '10.0.0.1', '192.168.1.1', '172.16.0.1', '10.0.0.1']
# Convert this:
ip_freq = {}
for ip in ip_addresses:
    if ip not in ip_freq:
        ip_freq[ip] = 0
    ip_freq[ip] += 1
print(ip_freq)

d = {}
for ip in ip_addresses:
    d[ip] = d.get(ip, 0) + 1
print(d)

d = Counter(ip_addresses)
print(d)

d = defaultdict(int)
for ip in ip_addresses:
    d[ip] += 1
print(d)






# Exercise 6: Word Length Distribution
print()
print( """Exercise 6: Word Length Distribution""")
"""Task: Count how many words of each length appear across all sentences. For example, in "The quick brown", lengths would be {3: 1, 5: 1, 5: 1} since there's one 3-letter word and two 5-letter words."""

sentences = ["The quick brown fox", "jumps over", "the lazy dog"]
# Convert this:
word_lengths = {}
for sentence in sentences:
    for word in sentence.split():
        length = len(word)
        if length not in word_lengths:
            word_lengths[length] = 0
        word_lengths[length] += 1
print(word_lengths)

## so I understand, k,v is word length, count
## get 
d = {}
for sentence in sentences:
    for word in sentence.split(' '):
        d[len(word)] = d.get(len(word), 0) + 1
print(d)


## Counter
ls = []
for sentence in sentences:
    for word in sentence.split(' '):
        ls.append(len(word)) 
d = Counter(ls)
print(d)



# zip it? no, take the word len, make a list pass to Counter. 
# there's a better way to make the list, but one thing at a time.
# yup, can make the list in another way, this is fine for now.
# the more verbose example I don't like much. I'm not usre if I need to practice that.
# it's kind of messy. I'll keep practicing for now.












# Exercise 7: User Activity Count
print()
print( """Exercise 7: User Activity Count""")
"""Task: Given a list of tuples containing (user, action) pairs, count how many actions each user has performed total, regardless of the action type."""

events = [
    ('user1', 'login'),
    ('user2', 'login'),
    ('user1', 'purchase'),
    ('user3', 'login'),
    ('user1', 'logout')
]
# Convert this:
user_activity = {}
for user, _ in events:
    if user not in user_activity:
        user_activity[user] = 0
    user_activity[user] += 1
print(user_activity)

# num actions per user
# get
d = {}
for user, _ in events:
    d[user] = d.get(user, 0) + 1
print(d)

# Counter
# so need to return the iterator? cool, used a generator expression. Nice.
# (also seeing that I'm getting a sense for what Counter needs.) cool.

d = Counter([user for user, _ in events])
print(d)
 
# defaultdict
d = defaultdict(int)
for user, _ in events:
    d[user] += 1
print(d)








# Exercise 8: File Extension Counter
print()
print( """Exercise 8: File Extension Counter""") 
"""Task: From a list of filenames, count how many files there are of each extension type (e.g., how many .pdf, .txt, .jpg files)."""

files = ['doc.pdf', 'file.txt', 'image.jpg', 'doc.pdf', 'file.pdf', 'image.jpg']
# Convert this:
extension_counts = {}
for file in files:
    ext = file.split('.')[-1]
    if ext not in extension_counts:
        extension_counts[ext] = 0
    extension_counts[ext] += 1
print(extension_counts)

# get
d = {}
for file in files:
    ext = file.split('.')[-1]
    d[ext] = d.get(ext, 0) + 1
print(d)

# counter
new = [file.split('.')[-1] for file in files]
d = Counter(new)
print(d)

# defdict
d = defaultdict(int)
for file in new:
    d[file] += 1
print(d)







## Exercise 9: Status Code Counter
print()
print("""Exercise 9: Status Code Counter""")
"""Task: Given a list of HTTP status codes from a web server's logs, count how frequently each status code appears to identify common response patterns."""

status_codes = [200, 404, 200, 500, 403, 404, 200, 200, 404]
# Convert this:
status_counts = {}
for code in status_codes:
    if code not in status_counts:
        status_counts[code] = 0
    status_counts[code] += 1
print(status_counts)

d = Counter(status_codes)
print(d)

d = defaultdict(int)
for i in status_codes:
    d[i] += 1
print(d)







## Exercise 10: Nested Category Counter
print()
print("""Exercise 10: Nested Category Counter""")
"""Task: From a list of (category, item) tuples, count how many items are in each main category, ignoring the specific items themselves."""

items = [
    ('electronics', 'laptop'),
    ('books', 'fiction'),
    ('electronics', 'phone'),
    ('books', 'fiction'),
    ('clothing', 'shirt')
]
# Convert this:
category_counts = {}
for category, _ in items:
    if category not in category_counts:
        category_counts[category] = 0
    category_counts[category] += 1
print(category_counts)

stuff = map(lambda x: x[0], items)
d = Counter(stuff)
print(d)

d = defaultdict(int)
for item in map(lambda x: x[0], items):
    d[item] += 1
print(d)
