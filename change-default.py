import os


def list_all_in_dir(mypath, recurse=False, path=False):
    """
    Returns a string list of every file in a directory.
    Pass recurse=True to get a list of all files in subdir as well.
    Pass path=True to get the full path instead of just file name.

    """
    if recurse:
        out = []
        for f in os.listdir(mypath):
            loc = os.path.join(mypath, f)
            if os.path.isfile(loc):
                if path:
                    out.append(loc)
                else:
                    out.append(f)
            elif os.path.isdir(loc):
                out = out + list_all_in_dir(loc, True, path)
        return out
    else:
        return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]


regions = list_all_in_dir('./config-files')
i = 0
for region in regions:
    print(str(i) + ": " + region)
    i = i + 1
region = input("Which region would you like?")

creds = list_all_in_dir('./cred-files')
i = 0
for cred in creds:
    print(str(i) + ": " + cred)
    i = i + 1

cred = input("Which credentials file would you like?")


os.system("ln -fs config-files/" + regions[int(region)] + " config")
os.system("ln -fs cred-files/" + creds[int(cred)] + " credentials")