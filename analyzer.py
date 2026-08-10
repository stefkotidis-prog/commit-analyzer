import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.github.com/repos/Significant-Gravitas/AutoGPT/commits?per_page=100"

categories = {
    "Bug Fixes": ["fix", "bug", "error", "patch", "hotfix"],
    "New Features": ["feat", "add", "implement", "new", "support"],
    "Documentation": ["docs", "readme", "documentation", "doc"],
    "Refactoring & Maintenance": ["refactor", "clean", "optimize", "chore"]
}

def categorize_commit(message):
    """Κατηγοριοποιεί το commit με βάση το taxonomy. Αν δεν ταιριάζει κάπου, πάει 'Other'."""
    message = message.lower()
    for category, keywords in categories.items():
        if any(word in message for word in keywords):
            return category
    return "Other"

print("Fetching data from GitHub API...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    parsed_commits = []
    for commit in data:
        msg = commit['commit']['message']
        author = commit['commit']['author']['name']
        
        cat = categorize_commit(msg)
        
        parsed_commits.append({
            "Author": author,
            "Category": cat,
            "Message_Length": len(msg)
        })

    df = pd.DataFrame(parsed_commits)
    
    print("-" * 30)
    print(f"Analyzed {len(df)} commits successfully.\n")

    category_counts = df['Category'].value_counts()
    print(category_counts)
    print("-" * 30)

    print("Generating chart...")
    plt.figure(figsize=(10, 6))

    category_counts.plot(kind='bar', color=['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#95a5a6'])
    
    plt.title('AutoGPT Commit Taxonomy Analysis', fontsize=14, fontweight='bold')
    plt.xlabel('Commit Category', fontsize=12)
    plt.ylabel('Number of Commits', fontsize=12)
    plt.xticks(rotation=45, ha='right') 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('commit_taxonomy_chart.png', dpi=300)
    print("Chart saved successfully as 'commit_taxonomy_chart.png'!")
    plt.show()

else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")