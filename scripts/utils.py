import sys

import pexpect


class Pexpect:
    def __init__(self, host, default_expect=']#', timeout=300):
        self.host = host
        self.default_expect = default_expect
        self.child = pexpect.spawn(f'ssh {host}', timeout=timeout, encoding='utf-8')
        self.child.logfile = sys.stdout
        self.child.expect(default_expect)

    def cmd(self, cmd, expect=None, timeout=None):
        if not expect:
            expect = self.default_expect
        self.child.sendline(cmd)
        return self.child.expect(expect, timeout=timeout)

    def send_break(self, expect=None):
        if not expect:
            expect = self.default_expect
        self.child.send('\003')
        self.child.expect(expect)
