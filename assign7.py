import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)

def is_valid_email(candidate):
    return bool(re.fullmatch(EMAIL_PATTERN, candidate))

sample_text = """
Welcome to the system. You can contact support@example.com or reach 
out directly to rahul_23@gmail.com for help. Please note that 
invalid emails like @missing-local.com will not work.
"""

found_emails = find_emails(sample_text)
print("Found emails:", found_emails)
print("Count:", len(found_emails))

test_strings = [
    "user@site.com", 
    "rahul_23@gmail.com", 
    "@missing-local.com", 
    "invalid.email@",
    "number@12345.com"
]

for string in test_strings:
    if is_valid_email(string):
        print(string, "- VALID")
    else:
        print(string, "- INVALID")