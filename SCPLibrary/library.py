from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
from scp import SCPClient
from errors import SCPNotConnectedError

try:
    from _version import __version__, __revision__
except ImportError:
    __version__ = "UNKNOWN"
    __revision__ = "UNKNOWN"

class SCPLibrary(object):
    """Robot Framework test library for Secure Copy (SCP).

    This library can be used to copy files to and from a remote machine using Secure Copy (SCP). It uses the
    Paramiko SSH Python library (just like robotframework-sshlibrary) and an SCP wrapper ('scp' by James Bardin).

    The library does not currently support Jython or IronPython at this time.

    == Table of contents ==

    - `Connection`
    - `File transfer`

    = Connection =

    Before files can be transferred a connection to remote machine must first be made. A connection can be made with the
    `Open Connection` keyword. This library currently only supports username/password authentication, but key-based
    connections should be implemented soon.

    Connections should be closed using the `Close Connection` when they are no longer in use.

    = File transfer =

    Files can be uploaded to the remote machine using the `Put File` keyword or downloaded to the local machine using
    the `Get File` keyword. Currently, only single-file transfers are supported.

    A connection must be made using the `Open Connection` keyword before file transfers may be made.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.scp_client = None

    def open_connection(self, hostname, port='22', username=None, password=None):
        """Opens a new SCP connection to the given host.

        The default port used is `22`:
        | Open Connection | host.tylercrumpton.com |

        A different port may be optionally given by using the `port` argument:
        | Open Connection | host.tylercrumpton.com | port=4242 |

        Authentication may be done using a username and password:
        | Open Connection | host.tylercrumpton.com | username=tyler | password=iamateapot |
        """
        try:
            port = int(port)
        except:
            raise ValueError('Port must be a valid number.')
        self.ssh.connect(hostname, port=port, username=username, password=password)
        self.scp_client = SCPClient(self.ssh.get_transport())

    def close_connection(self):
        """Closes the SCP connection.

        Example:
        | Open Connection  | host.tylercrumpton.com | username=tyler    | password=iamateapot |
        | Get File         | tea.txt                | /mytea/newtea.txt |
        | Close Connection |
        """
        if self.scp_client is not None:
            self.scp_client.close()
            self.scp_client = None

    def put_file(self, local_filepath, remote_filepath):
        """Uploads a file to the remote machine from the local machine.

        Note: A connection to the remote machine must be made first using the `Open Connection` keyword.

        Examples:
        | Put File | mytea.txt | /home/tyler/tea.txt |
        | Put File | mytea.txt | /home/tyler/        |
        """
        if self.scp_client is None:
            raise SCPNotConnectedError("An SCPLibrary connection must be created first using the 'Open Connection' keyword.")
        self.scp_client.put(local_filepath, remote_filepath, recursive=False)

    def put_directory(self, local_directory, remote_filepath):
        """Uploads a directory to the remote machine from the local machine.

        Note: A connection to the remote machine must be made first using the `Open Connection` keyword.

        Examples:
        | Put File | mytea_dir | /home/tyler/newtea_dir |
        | Put File | mytea.txt | /home/tyler/           |
        """
        if self.scp_client is None:
            raise SCPNotConnectedError("An SCPLibrary connection must be created first using the 'Open Connection' keyword.")
        self.scp_client.put(local_directory, remote_filepath, recursive=True)

    def get_file(self, remote_filepath, local_filepath, recursive=False):
        """Downloads a file from the remote machine to the local machine.

        `remote_filepath` determines the path to retrieve from remote host. Shell wildcards and environment variables
        on the remote machine may be used.

        Setting `recursive` to True will transfer files and directories recursively.

        Note: A connection to the remote machine must be made first using the `Open Connection` keyword.

        Example:
        | Get File | /home/tyler/tea.txt | sametea.txt |                |
        | Get File | /home/tyler/*.txt   | myteas/     |                |
        | Get File | /home/tyler/        | mytylerdir/ | recursive=True |
        """
        if self.scp_client is None:
            raise SCPNotConnectedError("An SCPLibrary connection must be created first using the 'Open Connection' keyword.")
        self.scp_client.get(remote_filepath, local_filepath, recursive=recursive)
e