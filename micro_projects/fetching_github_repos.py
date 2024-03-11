import requests


def fetch_user_repositories(username: str) -> list[dict]:
    data_list = []
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    data = response.json()
    for repo in data:
        data_list.append(repo)
    return data_list


def display_repository_info(repositories: list[dict]) -> None:

    for repo in repositories:
        name = repo["name"]
        description = repo["description"]
        language = repo["language"]
        stars_count = repo["stargazers_count"]

        print(f"Repostiory: {name}")
        print(f"With description: {description}")
        print(f"Repository language: {language}")
        print(f"Having {stars_count} stars")
        print()


def main():
    repositories = fetch_user_repositories("zahariev-webbersof")
    display_repository_info(repositories=repositories)


if __name__ == "__main__":
    main()
