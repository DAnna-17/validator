import csv

def is_login(s):
    i = s.find("@")
    s1 = ''
    for k in range(len(s)):
        if s[k] not in ".{[()]}":
            s1 = s[k] + s1
        else:
            break

    f = 1

    for k in range(len(s)):
        if s[k] not in ".{[()]}" and f:
            s1 = s[k] + s1
        else:
            break

        if not (s[k] in ".{[()]}" and f):
            s1 = s[k] + s1
        v1 = ord('a') <= ord(s[k]) <= ord('z') or ord('0') <= ord(s[k]) <= ord('9') or s[k] in '._-' or ord('A') <= ord(s[k]) <= ord('Z')
        if not v1 and k != i:
            w.append(s)
            return False
    v2 = 0 < len(s[:i]) < 129 and 3 <= len(s[i + 1:]) <= 256 and not(s[i+1:][0] in '-._' or s[0] in '_-.' or s[-1] in '-._' or s[:i][-1] in '_-.')
    ans = '.' in s[i + 1:] and 0 < len(s[:i]) < 129 and 3 <= len(s[i + 1:]) <= 256 and not '..' in s[:i] and v2
    if not ans:
        w.append(s)
    return ans


t = []
w = []
table_name = input('Введите название файда без указания типа:')
with open(table_name + '.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for email in reader:
        if email:
            t.append(email[0].strip()) if is_login(email[0].strip()) else None
print(t)
print('-----------------------------')
t = set(t)
for i in w:
    print(i)
out_name = table_name + '(1)'
with open(out_name + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in t:
        writer.writerow([i])
