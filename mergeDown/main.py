import subprocess

BRANCH_NOT_ON_REMOTE = 128
SUCCESS_RESPONSE = 0

def branchIsOnRemote(branch: str)->bool:
    # Check if branch is valid
    process = subprocess.run(["git", "show-branch", f"remotes/origin/{branch}"] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode == BRANCH_NOT_ON_REMOTE):
        print(f"{branch} does not exist on remote")
        return False

    if (process.returncode != SUCCESS_RESPONSE):
        print(f"Something went terribly wrong when checking {branch} existance")
        return False 
    
    return True

def updateBranch(branch: str)->None:
    print(f"Updating {branch} ...")

    process = subprocess.run(["git", "checkout", branch] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode != SUCCESS_RESPONSE):
        raise Exception(f"ERROR: could not checkout to {branch}")

    process = subprocess.run(["git", "pull"] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if (process.returncode != SUCCESS_RESPONSE):
        raise Exception(f"ERROR: could not git pull on {branch}")
    
    print(f"Update complete!")



if __name__ == "__main__":
    parentBranch = input("Input parent branch that you want to merge down from: ").strip()
    if(not branchIsOnRemote(parentBranch)):
        exit()


    childBranch = input("Input child branch which will receive the merge down: ").strip()
    if(not branchIsOnRemote(childBranch)):
        exit()

    try:
        updateBranch(parentBranch)
        updateBranch(childBranch)
    except:
        exit()



    process = subprocess.run(["git", "merge", parentBranch])

    print("Merge done, do not forget to git push!")