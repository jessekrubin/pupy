from subprocess import PIPE
from subprocess import run


def test_version():
    """

    """
    proc = run(args=["pupy", "--version"], stdout=PIPE, stderr=PIPE)
    version = proc.stdout.decode()
    assert "pupy version" in version.lower()


def test_V():
    """

    """
    proc = run(args=["pupy", "-V"], stdout=PIPE, stderr=PIPE)
    version = proc.stdout.decode()
    assert "pupy version" in version.lower()
