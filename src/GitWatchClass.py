class GitWatch:

    def __init__(self):
        self.watches = []

    def get_watches(self):
        return self.watches

    def add_watch(
        self, 
        absolute_path: str,
        repo_url: str,
        interval: int = 60, 
        auto_start: bool = False
    ):

        """
        Add a git watch
        `absolute_path`: absolute path to your script root folder
        `repo_url`: URL of the repository
        `interval`: The time between the checks
        `auto_start`: Start the main file of your script automatically (wip)
        """

        name = repo_url.split('github.com/')[1].split('/')[1]

        self.watches.append((absolute_path, repo_url, name, interval, auto_start))
