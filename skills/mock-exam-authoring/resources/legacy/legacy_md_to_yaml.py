"""One-off converter: AZ-900-mock-exam.md -> az-900.exam.yaml"""
import re, sys, yaml

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")

DOMAINS = [
    ("cloud-concepts", "Describe cloud concepts", "25–30%"),
    ("azure-architecture-services", "Describe Azure architecture and services", "35–40%"),
    ("management-governance", "Describe Azure management and governance", "30–35%"),
]
domain_topics = {d[0]: [] for d in DOMAINS}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


domain = None
topic = None
questions = {}
mode = "q"
cur = None
cur_ans = None

for ln in lines:
    m = re.match(r"# Domain (\d): ", ln)
    if m:
        domain = DOMAINS[int(m.group(1)) - 1][0]
        continue
    if ln.startswith("# Answer key"):
        break
    if ln.startswith("# Part 2"):
        domain = None
        continue
    m = re.match(r"## (.+?) \(Q(\d+)–Q(\d+)\)$", ln)
    if m:
        title = m.group(1)
        dm = re.match(r"Domain (\d) additions: (.+)", title)
        if dm:
            domain = DOMAINS[int(dm.group(1)) - 1][0]
            title = "Additional: " + dm.group(2)
        topic = slug(title)
        if topic not in [t["id"] for t in domain_topics[domain]]:
            domain_topics[domain].append({"id": topic, "title": title})
        mode = "q"
        cur = None
        continue
    if ln.startswith("### Answers"):
        mode = "a"
        cur = None
        continue
    if ln.startswith("# ") or ln.startswith("## "):
        continue
    if mode == "q":
        m = re.match(r"\*\*Q(\d+)\.\*\* (.*)", ln)
        if m:
            qid = int(m.group(1))
            cur = {"id": qid, "domain": domain, "topic": topic, "text": m.group(2), "options": []}
            questions[qid] = cur
            continue
        m = re.match(r"- ([A-D])\) (.*)", ln)
        if m and cur:
            cur["options"].append({"id": m.group(1), "text": m.group(2)})
            continue
        if cur and ln.strip() and not cur["options"]:
            cur["text"] += "\n" + ln
    else:
        m = re.match(r"\*\*Q(\d+) – ([A-D])\.\*\* (.*)", ln)
        if m:
            cur_ans = questions[int(m.group(1))]
            cur_ans["correct"] = [m.group(2)]
            cur_ans["explanation"] = m.group(3)
            continue
        m = re.match(r"- ([A-D](?:(?:, and |, | and )[A-D])*): (.*)", ln)
        if m and cur_ans:
            ids = re.findall(r"[A-D]", m.group(1))
            for o in cur_ans["options"]:
                if o["id"] in ids:
                    o["explanation"] = m.group(2)
            continue

text = "\n".join(lines)
key = text.split("# Answer key")[1].split("## Topic coverage")[0]
pairs = re.findall(r"(\d+) \| ([A-D])", key)
for q, a in pairs:
    assert questions[int(q)]["correct"] == [a], f"Key mismatch Q{q}"
assert len(questions) == 75 and len(pairs) == 75, (len(questions), len(pairs))

for q in questions.values():
    assert len(q["options"]) == 4 and "correct" in q, q["id"]
    q["type"] = "single"

exam = {
    "schema_version": 1,
    "id": "az-900",
    "title": "AZ-900 Mock Exam: Microsoft Azure Fundamentals",
    "description": "75 multiple-choice questions across the three AZ-900 skill domains.",
    "source_note": "Based on the skills measured as of July 20, 2026.",
    "language": "en",
    "pass_score_percent": 70,
    "domains": [
        {"id": i, "title": t, "weight": w, "topics": domain_topics[i]} for i, t, w in DOMAINS
    ],
    "questions": [questions[k] for k in sorted(questions)],
}


class D(yaml.SafeDumper):
    pass


def str_rep(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


D.add_representer(str, str_rep)
with open(dst, "w", encoding="utf-8") as f:
    yaml.dump(exam, f, Dumper=D, sort_keys=False, allow_unicode=True, width=100)
print("questions:", len(questions))
