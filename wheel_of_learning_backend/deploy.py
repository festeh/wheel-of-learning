import remoto
import shlex


class Tool:

    @staticmethod
    def exist_cmd() -> str:
        return ""

    @staticmethod
    def install_cmd() -> str:
        return ""


class Path:

    PATH = "/root/.local/bin"

    @staticmethod
    def exist_cmd() -> str:
        return """python3 -c 'import os; exit(1) if "/root/.local/bin" not in os.environ["PATH"] else exit(0)'"""

    @staticmethod
    def install_cmd() -> str:
        cmd1 = """echo "export PATH=/root/.local/bin:$PATH" >> /root/myrc"""
        cmd2 = """echo "export PATH=/root/.local/bin:$PATH" >> /root/.bashrc"""
        cmd3 = """echo "export PATH=/root/.cargo/bin:$PATH" >> /root/myrc"""
        return f"""{cmd1} && {cmd2} && {cmd3}"""


class Poetry(Tool):

    @staticmethod
    def exist_cmd() -> str:
        return "poetry --version"

    @staticmethod
    def install_cmd() -> str:
        return "curl -sSL https://install.python-poetry.org | python3"

class Rust(Tool):
    @staticmethod
    def exist_cmd() -> str:
        return "cargo --version"

    @staticmethod
    def install_cmd() -> str:
        return "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"

class Just(Tool):
    @staticmethod
    def exist_cmd() -> str:
        return "just --version"

    @staticmethod
    def install_cmd() -> str:
        return "cargo install just"

class Nginx(Tool):
    @staticmethod
    def exist_cmd() -> str:
        return "nginx -v"

    @staticmethod
    def install_cmd() -> str:
        return "apt-get update && apt-get install -y nginx"

class Npm(Tool):
    @staticmethod
    def exist_cmd() -> str:
        return "npm --version"

    @staticmethod
    def install_cmd() -> str:
        return "sudo apt install -y nodejs npm"

class Repo(Tool):
    @staticmethod
    def exist_cmd() -> str:
        return "cd wheel-of-learning && git fetch --all && git reset --hard origin/master"

    @staticmethod
    def install_cmd() -> str:
        return "git clone https://github.com/festeh/wheel-of-learning.git"

def prepare_cmd(cmd):
    cmd = cmd.strip()
    # cmd = cmd.replace('$', '\\$')
    # cmd = cmd.replace('`', '\\`')
    cmd = cmd.replace('"', '\\"')
    pre_cmd = "touch /root/myrc && source /root/myrc"
    cmd = f"""bash -c "{pre_cmd} && {cmd}" """
    return shlex.split(cmd.strip())


def check_exists(cmd: str):
    prep_cmd = prepare_cmd(cmd)
    try:
        out, err, code = remoto.process.check(conn, prep_cmd)
    except Exception as e:
        print(e)
        return False
    print("\n".join(out))
    if err:
        print("Error:", err)
        return False
    return True
    return code == 0


def run(cmd: str):
    prep_cmd = prepare_cmd(cmd)
    print(f"Running {prep_cmd}")
    try:
        remoto.process.run(conn, prep_cmd)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    tools = [Path, Poetry, Rust, Just, Repo, Nginx, Npm]
    conn = remoto.Connection("linode")
    for tool in tools:
        if not check_exists(tool.exist_cmd()):
            run(tool.install_cmd())
