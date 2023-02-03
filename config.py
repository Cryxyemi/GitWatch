from src.GitWatchClass import GitWatch


watch = GitWatch()
watch.add_watch(
    absolute_path="C:/Users/USER/Desktop/gitwatch",
    repo_url="https://github.com/Cryxyemi/GitWatch",
    interval=60
)
