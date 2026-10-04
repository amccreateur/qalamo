with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any sequence of \\' with \'
text = text.replace(r"\'", "'")
text = text.replace(r"\\'", "'")

# Now properly escape single quotes inside single-quoted strings:
# Or even better, let's use double quotes where appropriate or replace escaped apostrophes properly.

lines = text.splitlines()
new_lines = []
for line in lines:
    # If line is a title, description, meaning, transliteration, phonemeDesc, name
    # we can safely handle apostrophes if enclosed in double quotes or escaped.
    new_lines.append(line)

fixed_text = '\n'.join(new_lines)
with open('src/data/curriculum.ts', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Cleaned!")
