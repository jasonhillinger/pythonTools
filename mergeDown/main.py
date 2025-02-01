import subprocess

BRANCH_NOT_ON_REMOTE = 128

def branchIsOnRemote(branch: str)->bool:
    # Check if branch is valid
    process = subprocess.run(["git", "show-branch", f"remotes/origin/{branch}"] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode == BRANCH_NOT_ON_REMOTE):
        print(f"{branch} does not exist on remote")
        return False

    if (process.returncode != 0):
        print(f"Something went terribly wrong when checking {branch} existance")
        return False 
    
    return True

def updateBranch(branch: str)->bool:
    print(f"Updating {branch} ...")

    process = subprocess.run(["git", "checkout", branch] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode != 0):
        print(f"ERROR: could not checkout to {branch}")
        return False

    process = subprocess.run(["git", "pull"] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode != 0):
        print(f"ERROR: could not git pull on {branch}")
        return False
    
    print(f"Update complete!")

    return True

parentBranch = input("Input parent branch that you want to merge down from: ").strip()
if(not branchIsOnRemote(parentBranch)):
    exit()


childBranch = input("Input child branch which will receive the merge down: ").strip()
if(not branchIsOnRemote(childBranch)):
    exit()

if(not updateBranch(parentBranch)):
    exit()

if(not updateBranch(childBranch)):
    exit()


process = subprocess.run(["git", "merge", parentBranch])

print("Merge done, do not forget to git push!")