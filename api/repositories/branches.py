from core.rest_client import RestClient


class Branches(RestClient):
    # 137
    def get_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-branch-protection
        """
        headers = {'Accept': 'application/vnd.github.luke-cage-preview+json'}
        return self.get('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), headers=headers, **kwargs)
