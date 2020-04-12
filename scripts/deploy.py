import os
import sys

from utils import Pexpect


def deploy():
    DEPLOY_HOST = os.getenv('DEPLOY_HOST', 'root@134.122.115.153')
    # DEPLOY_VERSION = os.getenv('DEPLOY_VERSION')
    # DOCKER_COMPOSE_FILE = os.getenv('DOCKER_COMPOSE_FILE', 'docker-prod.yml')
    # DOCKER_COMPOSE = f'docker-compose -f {DOCKER_COMPOSE_FILE}'
    EXPECT_VALUE = os.getenv('EXPECT_VALUE', '~#')
    #
    # ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
    #
    # VERSION_FILE_PATH = os.getenv('VERSION_FILE_PATH', '.version')
    # VERSION = os.getenv('CI_PIPELINE_ID', 'Unknown')
    # DEPLOY_DATE = str(date.today())
    #
    # if not DEPLOY_HOST or not DEPLOY_VERSION:
    #     raise ValueError('No env vars provided')
    #
    # if ENVIRONMENT != 'dev':
    #     sync_backups()

    expect = Pexpect(DEPLOY_HOST, default_expect=EXPECT_VALUE)
    expect.cmd('docker run --rm -it -p 80:80 strm/helloworld-http')
    # expect.cmd('docker run -d -p 80 tutum/hello-world')
    # expect.cmd('pushd /srv/employee-profile/')
    # expect.cmd('git fetch origin')
    # expect.cmd(f'git checkout {DEPLOY_VERSION}')
    # expect.cmd(f'{DOCKER_COMPOSE} stop')
    # expect.cmd(f'yes yes | {DOCKER_COMPOSE} rm -v web celery client nginx')
    # expect.cmd(f'{DOCKER_COMPOSE} up -d')
    # client_ok = expect.cmd(f'{DOCKER_COMPOSE} logs --tail 1 -f client', expect=['Running on http://0.0.0.0:3000', 'Failed to build client!'], timeout=600)
    # if client_ok == 1:  # Failed to build client!
    #     sys.exit(1)
    # expect.send_break()
    # expect.cmd(f'echo {VERSION}/{DEPLOY_DATE} > {VERSION_FILE_PATH}')
    # expect.send_break()
    # expect.cmd(f'{DOCKER_COMPOSE} logs --tail 1 -f web', expect=['spawned uWSGI http 1',  'spawned .* offload threads', 'HTTP/1.0 200'])
    # expect.send_break()
    # expect.cmd('exit', expect='logout')


if __name__ == '__main__':
    deploy()
