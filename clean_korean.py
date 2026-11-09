import re, json

korean_re = re.compile(r'[\uac00-\ud7a3]+')

# 1. Clean data-exam.js
with open('/home/justin/Desktop/review/review/js/data-exam.js', 'r', encoding='utf-8') as f:
    exam_content = f.read()

# Replace parenthetical korean like (단위 테스트) -> ""
exam_clean = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', exam_content)
# Check if any remaining Korean
rem = korean_re.findall(exam_clean)
print(f"data-exam.js: remaining Korean matches after pass 1: {len(rem)}")
if rem:
    print(rem[:10])

# 2. Clean data-flashcards.js
with open('/home/justin/Desktop/review/review/js/data-flashcards.js', 'r', encoding='utf-8') as f:
    fc_content = f.read()

fc_clean = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', fc_content)
rem_fc = korean_re.findall(fc_clean)
print(f"data-flashcards.js: remaining Korean matches after pass 1: {len(rem_fc)}")
if rem_fc:
    print(rem_fc[:10])

# 3. Clean data-quizzes.js
with open('/home/justin/Desktop/review/review/js/data-quizzes.js', 'r', encoding='utf-8') as f:
    qz_content = f.read()

qz_clean = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', qz_content)
rem_qz = korean_re.findall(qz_clean)
print(f"data-quizzes.js: remaining Korean matches after pass 1: {len(rem_qz)}")

# 4. Clean data-modules.js
with open('/home/justin/Desktop/review/review/js/data-modules.js', 'r', encoding='utf-8') as f:
    mod_content = f.read()

mod_clean = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', mod_content)
rem_mod = korean_re.findall(mod_clean)
print(f"data-modules.js: remaining Korean matches after pass 1: {len(rem_mod)}")
if rem_mod:
    print(rem_mod[:10])

