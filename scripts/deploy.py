import os

from utils import Pexpect


def deploy():
    DEPLOY_HOST = os.getenv('DEPLOY_HOST')
    DOCKER_COMPOSE_FILE = os.getenv('DOCKER_COMPOSE_FILE', 'local.yml')
    DOCKER_COMPOSE = f'docker-compose -f {DOCKER_COMPOSE_FILE}'
    EXPECT_VALUE = os.getenv('EXPECT_VALUE', '~/spa_django_application#')

    expect = Pexpect(DEPLOY_HOST, default_expect=EXPECT_VALUE)
    expect.cmd('cd spa_django_application/')
    expect.cmd('git pull')
    expect.cmd(f'{DOCKER_COMPOSE} stop')
    expect.cmd(f'{DOCKER_COMPOSE} up -d')
    expect.cmd('exit', expect='logout')


if __name__ == '__main__':
    deploy()
