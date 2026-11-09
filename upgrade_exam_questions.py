import json, re

with open('/home/justin/Desktop/review/review/js/data-exam.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse questions from the js file
m = re.search(r'var EXAM_QUESTIONS\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print("Could not parse EXAM_QUESTIONS")
    exit(1)

questions = json.loads(m.group(1))
print(f"Loaded {len(questions)} questions.")

# Set default format: 'mcq'
for q in questions:
    q['format'] = 'mcq'

# Convert selected questions to short_answer and calculation:
conversions = {
    "q7": {
        "format": "calculation",
        "placeholder": "Enter numerical complexity (e.g. 6)",
        "acceptableAnswers": ["6", "6.0", "v(g)=6", "v(g) = 6"]
    },
    "q8": {
        "format": "short_answer",
        "placeholder": "Enter technical term (e.g. Stubs)",
        "acceptableAnswers": ["stub", "stubs", "dummy stub", "dummy stubs"]
    },
    "q9": {
        "format": "short_answer",
        "placeholder": "Enter data structure name (e.g. Stack)",
        "acceptableAnswers": ["stack", "lifo stack", "call stack"]
    },
    "q10": {
        "format": "short_answer",
        "placeholder": "Enter license acronym (e.g. GPL)",
        "acceptableAnswers": ["gpl", "gnu gpl", "gpl v2", "gpl v3", "general public license", "gnu general public license"]
    },
    "q14": {
        "format": "short_answer",
        "placeholder": "Enter GoF pattern name (e.g. Observer)",
        "acceptableAnswers": ["observer", "observer pattern", "publish-subscribe", "pub-sub"]
    },
    "q21": {
        "format": "short_answer",
        "placeholder": "Enter SQL window function (e.g. DENSE_RANK)",
        "acceptableAnswers": ["dense_rank", "dense_rank()", "denserank", "dense rank"]
    },
    "q24": {
        "format": "short_answer",
        "placeholder": "Enter 2PL phase name (e.g. Shrinking Phase)",
        "acceptableAnswers": ["shrinking", "shrinking phase", "shrink phase"]
    },
    "q30": {
        "format": "short_answer",
        "placeholder": "Enter CPU register acronym or name (e.g. PC)",
        "acceptableAnswers": ["pc", "program counter", "program counter (pc)", "pc register"]
    },
    "q33": {
        "format": "calculation",
        "placeholder": "Enter usable storage capacity (e.g. 6TB or 6)",
        "acceptableAnswers": ["6tb", "6 tb", "6", "6 terabytes"]
    },
    "q39": {
        "format": "calculation",
        "placeholder": "Enter number of usable host IP addresses (e.g. 30)",
        "acceptableAnswers": ["30", "30 hosts", "30 usable hosts"]
    },
    "q40": {
        "format": "short_answer",
        "placeholder": "Enter TCP flag combination (e.g. SYN-ACK)",
        "acceptableAnswers": ["syn-ack", "syn/ack", "syn ack", "synack"]
    },
    "q42": {
        "format": "calculation",
        "placeholder": "Enter exact total number of keys (e.g. 19900)",
        "acceptableAnswers": ["19900", "19,900", "19900 keys"]
    },
    "q43": {
        "format": "short_answer",
        "placeholder": "Enter 4-letter cipher name (e.g. SEED)",
        "acceptableAnswers": ["seed", "seed cipher", "seed-128"]
    },
    "q49": {
        "format": "short_answer",
        "placeholder": "Enter cyber attack term (e.g. Qshing)",
        "acceptableAnswers": ["qshing", "qr phishing", "qr code phishing", "quishing"]
    },
    "q58": {
        "format": "short_answer",
        "placeholder": "Enter supply chain phenomenon name (e.g. Bullwhip Effect)",
        "acceptableAnswers": ["bullwhip", "bullwhip effect", "the bullwhip effect"]
    },
    "q59": {
        "format": "calculation",
        "placeholder": "Enter number of new communication channels (e.g. 18)",
        "acceptableAnswers": ["18", "18 channels", "18 new channels"]
    },
    "q60": {
        "format": "short_answer",
        "placeholder": "Enter 4-letter business principle acronym (e.g. MECE)",
        "acceptableAnswers": ["mece"]
    },
    "q62": {
        "format": "calculation",
        "placeholder": "Enter expected duration in days (e.g. 7.0 or 7)",
        "acceptableAnswers": ["7", "7.0", "7 days", "7.0 days"]
    },
    "q63": {
        "format": "calculation",
        "placeholder": "Enter Cost Variance CV in dollars (e.g. -20000)",
        "acceptableAnswers": ["-20000", "-$20000", "-20,000", "-$20,000", "-20k"]
    }
}

for qid, cfg in conversions.items():
    for q in questions:
        if q['id'] == qid:
            q.update(cfg)
            break

formats = {}
for q in questions:
    f = q['format']
    formats[f] = formats.get(f, 0) + 1

print("Question format distribution:", formats)

new_content = "// Official CICT / TOPCIT Full Simulation Mock Exam (65 Questions, 1000 Points)\n"
new_content += "// Includes Multiple Choice (MCQ), Short Answer (Fill-in), and Numerical Calculations\n\n"
new_content += "var EXAM_QUESTIONS = " + json.dumps(questions, indent=2, ensure_ascii=False) + ";\n\n"
new_content += 'if (typeof window !== "undefined") { window.EXAM_QUESTIONS = EXAM_QUESTIONS; }\n'

with open('/home/justin/Desktop/review/review/js/data-exam.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated js/data-exam.js!")
