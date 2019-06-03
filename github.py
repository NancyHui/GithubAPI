from api.repositories.repos import Repos


class Github(object):
    def __init__(self, **kwargs):
        self.api_host = 'https://api.github.com'
        self.repos = Repos(self.api_host, **kwargs)


if __name__ == '__main__':
    username = 'NancyHui'
    orgname = 'TestUpCommunity'

    token = '17b1194abec78f97006e547185bc5cbd780fab88'
    github = Github(token=token)

    # # 137
    r137 = github.repos.branches.get_branch_protection(username, 'hello-world', 'readme-edits')
    print(r137.status_code)
    print(r137.text)

