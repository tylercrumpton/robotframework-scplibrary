from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
from scp import SCPClient
from errors import SCPNotConnectedError

class SCPLibrary(object):

    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.scp_client = None

    def open_connection(self, hostname, port=22, username=None, password=None):
        self.ssh.connect(hostname, port=port, username=username, password=password)
        self.scp_client = SCPClient(self.ssh.get_transport())

    def put_file(self, local_filepath, remote_filepath):
        if self.scp_client is None:
            raise SCPNotConnectedError("An SCPLibrary connection must be created first using the 'Open Connection' keyword.")
        self.scp_client.put(local_filepath, remote_filepath)

    def get_file(self, remote_filepath, local_filepath):
        if self.scp_client is None:
            raise SCPNotConnectedError("An SCPLibrary connection must be created first using the 'Open Connection' keyword.")
        self.scp_client.get(remote_filepath, local_filepath)
