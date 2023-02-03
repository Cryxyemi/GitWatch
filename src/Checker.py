import os
import shutil
import asyncio
import time
from src.helpers import get_zip, writefile, unzip
from src.vars import GITHUB_URL_ZIP


async def check_watch(watch: tuple):
    path = watch[0]
    repo_url = watch[1]
    name = watch[2]
    interval = watch[3]
    auto_start = watch[4]

    while True:
        print("Checking for updates...")
        start_time = time.time()

        zip_bin = await get_zip(repo_url + GITHUB_URL_ZIP)
        await writefile(zip_bin, f'files/{name}.zip')
        unzip(f'files/{name}.zip', 'files')

        os.remove(f'files/{name}.zip')
        del zip_bin

        same_files = True
        ending = '-master'

        if not os.path.exists(f'files/{name}-master'):
            ending = '-main'


        things = []
        git_files = []

        for thing in os.scandir(path):
            things.append(thing)

        for git_file in os.scandir(f'files/{name}{ending}'):
            git_files.append(git_file)

        if len(things) != len(git_files):
            same_files = False

        if len(things) > len(git_files):
            for file in things:
                for g_file in git_files:
                    if not os.path.exists(f'files/{name}{ending}/{file.name}'):
                        same_files = False
                        break

                    if not os.path.exists(f'{path}/{g_file.name}'):
                        same_files = False
                        break

                    if file.name == g_file.name:
                        if file.is_file():
                            if file.stat().st_size != g_file.stat().st_size:
                                same_files = False
                                break

                        elif file.is_dir():
                            if file.stat().st_mtime != g_file.stat().st_mtime:
                                same_files = False
                                break

        else:
            for g_file in git_files:
                for file in things:
                    if not os.path.exists(f'files/{name}{ending}/{file.name}'):
                        same_files = False
                        break

                    if not os.path.exists(f'{path}/{g_file.name}'):
                        same_files = False
                        break

                    if file.name == g_file.name:
                        if file.is_file():
                            if file.stat().st_size != g_file.stat().st_size:
                                same_files = False
                                break

                        elif file.is_dir():
                            if file.stat().st_mtime != g_file.stat().st_mtime:
                                same_files = False
                                break

        if not same_files:
            print(f'Updating {name}...')
            shutil.rmtree(path)

            shutil.copytree(f'files/{name}{ending}', path)

        if same_files:
            print("No updates found")

            shutil.rmtree(f'files/{name}{ending}')

        end_time = time.time()
        passed_time = end_time - start_time

        await asyncio.sleep(interval + passed_time)
