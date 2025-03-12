import requests

class GitHubUserFetcher:
    def __init__(self, username):
        self.url = f"https://api.github.com/users/{username}"

    def fetch_user(self):
        try:
            res = requests.get(self.url, timeout=5)
            if res.status_code == 200:
                u = res.json()
                return (f"👤 Name: {u.get('name', 'N/A')}\n📜 Bio: {u.get('bio', 'No bio')}\n"
                        f"📍 Location: {u.get('location', 'Unknown')}\n📂 Repos: {u['public_repos']}\n"
                        f"👥 Followers: {u['followers']}\n🖼 Profile: {u['avatar_url']}\n")
            return "⚠️ User not found!" if res.status_code == 404 else f"⚠️ Error: {res.status_code}"
        except requests.exceptions.ConnectionError:
            return "❌ Network error!"
        except requests.exceptions.Timeout:
            return "⏳ Request timed out!"
        except Exception as e:
            return f"❗ Error: {e}"

print(GitHubUserFetcher(input("GitHub username: ")).fetch_user())
