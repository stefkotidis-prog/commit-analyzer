import requests

url = "https://api.github.com/repos/Significant-Gravitas/AutoGPT/commits"

print("Fetching data from GitHub API...")
response = requests.get(url)

data = response.json()

keywords = ["fix", "bug", "error"]
bug_fixes_count = 0

for commit in data:
    message = commit['commit']['message'].lower()
    
    if any(word in message for word in keywords):
        bug_fixes_count += 1

print("-" * 30)
print(f"Analyzed the {len(data)} most recent commits.")
print(f"Found {bug_fixes_count} commits related to bugs/fixes.")