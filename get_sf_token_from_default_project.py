from subprocess import PIPE, Popen

CLI_SF_ORG_DISPLAY = ['sf', 'org', 'display']

# INIT MAIN METHOD
def getSfAccessToken():
    access_token = ''
    process = Popen(CLI_SF_ORG_DISPLAY, stdout=PIPE, stderr=PIPE)
    process.wait()
    stdout, stderr = process.communicate()

    for line in stdout.decode('utf-8').splitlines():
        if 'Access Token' in line:
            access_token = line.split()[2]

    return access_token

##Test
if __name__ == '__main__':
    getSfAccessToken()