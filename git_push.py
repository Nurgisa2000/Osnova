# git@github.com:Nurgisa2000/Osnova.git

from os import system

ssh_url="git@github.com:Nurgisa2000/Osnova.git"
branch="master"
commit_message="U"

system('clear')
system('git init')
system('git add .')
system(f'git commit -m {commit_message}')
system(f'git remote add origin {ssh_url}')
system(f'git push -u origin {branch}')

print('Процесс успешно выполнено.')

