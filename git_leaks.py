#! user/bin/python3

from git import Repo
import re #signal
import time
from tqdm import tqdm



REPO_DIR = './skale/skale-manager'
KEY_WORDS = ['credentials','password','key'] #,'password','username','key'

def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def load():
    
    time.sleep(1)

    

if __name__ == '__main__':
    
    commits = extract(REPO_DIR)
    commits_of_interest = []

    # Barra de progreso
    for commit in tqdm (range (len(commits)), desc="Loading..."):
        
        for word in KEY_WORDS:
            if re.search(word, commits[commit].message, re.IGNORECASE):
                commits_of_interest.append(commits[commit])
                
    for i in commits_of_interest:
        print('Commit: {} - {}'.format(i.hexsha, i.message))
    
    
                
    


                

    