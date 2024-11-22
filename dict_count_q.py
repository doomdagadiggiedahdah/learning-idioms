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






## Exercise 6: Word Length Distribution
#sentences = ["The quick brown fox", "jumps over", "the lazy dog"]
## Convert this:
#word_lengths = {}
#for sentence in sentences:
#    for word in sentence.split():
#        length = len(word)
#        if length not in word_lengths:
#            word_lengths[length] = 0
#        word_lengths[length] += 1
#
















## Exercise 7: User Activity Count
#events = [
#    ('user1', 'login'),
#    ('user2', 'login'),
#    ('user1', 'purchase'),
#    ('user3', 'login'),
#    ('user1', 'logout')
#]
## Convert this:
#user_activity = {}
#for user, _ in events:
#    if user not in user_activity:
#        user_activity[user] = 0
#    user_activity[user] += 1
#

## Exercise 8: File Extension Counter
#files = ['doc.pdf', 'file.txt', 'image.jpg', 'doc.pdf', 'file.pdf', 'image.jpg']
## Convert this:
#extension_counts = {}
#for file in files:
#    ext = file.split('.')[-1]
#    if ext not in extension_counts:
#        extension_counts[ext] = 0
#    extension_counts[ext] += 1
#

## Exercise 9: Status Code Counter
#status_codes = [200, 404, 200, 500, 403, 404, 200, 200, 404]
## Convert this:
#status_counts = {}
#for code in status_codes:
#    if code not in status_counts:
#        status_counts[code] = 0
#    status_counts[code] += 1
#

## Exercise 10: Nested Category Counter
#items = [
#    ('electronics', 'laptop'),
#    ('books', 'fiction'),
#    ('electronics', 'phone'),
#    ('books', 'fiction'),
#    ('clothing', 'shirt')
#]
## Convert this:
#category_counts = {}
#for category, _ in items:
#    if category not in category_counts:
#        category_counts[category] = 0
#    category_counts[category] += 1
