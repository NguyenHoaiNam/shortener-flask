import os
from alembic import command as alembic_command
from alembic import config as alembic_config


def init_config():
    """Initialize and return the Alembic configuration."""

    config = alembic_config.Config(
        os.path.join(os.path.dirname(__file__), 'alembic.ini')
    )
    config.set_main_option('script_location',
                           'migration:migration_alb')
    return config


def upgrade(to_version='head'):
    """Upgrade to the specified version."""
    alembic_cfg = init_config()
    alembic_command.upgrade(alembic_cfg, to_version)


def history(verbose):
    alembic_cfg = init_config()
    alembic_command.history(alembic_cfg, verbose=verbose)


def current(verbose):
    alembic_cfg = init_config()
    alembic_command.current(alembic_cfg, verbose=verbose)


def stamp(to_version='head'):
    """Stamp the specified version, with no migration performed."""
    alembic_cfg = init_config()
    alembic_command.stamp(alembic_cfg, to_version)


def generate(autogenerate=True, message='generate changes', sql_url=None):
    """Generate a version file."""
    alembic_cfg = init_config()
    alembic_command.revision(alembic_cfg, message=message,
                             autogenerate=autogenerate)
