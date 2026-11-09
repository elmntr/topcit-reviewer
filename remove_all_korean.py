import re

korean_re = re.compile(r'[\uac00-\ud7a3]+')

# 1. Clean data-exam.js
with open('/home/justin/Desktop/review/review/js/data-exam.js', 'r', encoding='utf-8') as f:
    exam_text = f.read()

exam_text = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', exam_text)
# Any standalone Korean word if any
exam_text = korean_re.sub('', exam_text)

with open('/home/justin/Desktop/review/review/js/data-exam.js', 'w', encoding='utf-8') as f:
    f.write(exam_text)

# 2. Clean data-flashcards.js
with open('/home/justin/Desktop/review/review/js/data-flashcards.js', 'r', encoding='utf-8') as f:
    fc_text = f.read()

fc_text = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', fc_text)
fc_text = korean_re.sub('', fc_text)

with open('/home/justin/Desktop/review/review/js/data-flashcards.js', 'w', encoding='utf-8') as f:
    f.write(fc_text)

# 3. Clean data-quizzes.js
with open('/home/justin/Desktop/review/review/js/data-quizzes.js', 'r', encoding='utf-8') as f:
    qz_text = f.read()

qz_text = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', qz_text)
qz_text = korean_re.sub('', qz_text)

with open('/home/justin/Desktop/review/review/js/data-quizzes.js', 'w', encoding='utf-8') as f:
    f.write(qz_text)

# 4. Clean data-modules.js
with open('/home/justin/Desktop/review/review/js/data-modules.js', 'r', encoding='utf-8') as f:
    mod_text = f.read()

# Replace specific known table entries first
mod_text = mod_text.replace(r'\"원자값 (Atomic value)\"', r'\"Atomic values only\"')
mod_text = mod_text.replace(r'\"부분 함수 종속성 제거 (Full functional dependency)\"', r'\"Full functional dependency (No partial dependency)\"')
mod_text = mod_text.replace(r'\"이행적 함수 종속성 제거 (Transitive dependency)\"', r'\"Eliminate transitive dependency\"')
mod_text = mod_text.replace(r'\"모든 결정자가 후보키 (Determinant is Candidate Key)\"', r'\"Every determinant must be a candidate key\"')
mod_text = mod_text.replace(r'\"다치 종속성 제거\"', r'\"No multi-valued dependencies\"')
mod_text = mod_text.replace(r'\"조인 종속성 제거\"', r'\"No join dependencies\"')
mod_text = mod_text.replace(r'<td>제안서</td>', r'<td>Formal Proposal</td>')

# Remove parenthetical Korean
mod_text = re.sub(r'\s*\([^\)]*[\uac00-\ud7a3]+[^\)]*\)', '', mod_text)
# Remove any remaining Korean words
mod_text = korean_re.sub('', mod_text)

with open('/home/justin/Desktop/review/review/js/data-modules.js', 'w', encoding='utf-8') as f:
    f.write(mod_text)

print("All files processed.")
