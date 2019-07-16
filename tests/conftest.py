import os
import pytest
import shutil
import logging
from sphinx.testing.path import path
from sphinx.util.logging import NAMESPACE

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'


@pytest.fixture(scope='function')
def app(app, caplog):
    #app.warningiserror = True # Uncomment to get a stack trace of the warning
    # Set the capture level for the sphinx logger
    caplog.set_level(logging.WARNING, logger=NAMESPACE)
    # Force sphinx logger propagate to true because otherwise pytest will not
    # be able to capture the logging events from sphinx.
    logger = logging.getLogger(NAMESPACE)
    logger.propagate = True
    return app


def _initialize_test_directory(session):
    testroot = os.path.join(str(session.config.rootdir), 'tests')
    tempdir = os.path.abspath(os.getenv('SPHINX_TEST_TEMPDIR',
                              os.path.join(testroot, 'build')))
    os.environ['SPHINX_TEST_TEMPDIR'] = tempdir

    print('Temporary files will be placed in %s.' % tempdir)

    if os.path.exists(tempdir):
        shutil.rmtree(tempdir)

    os.makedirs(tempdir)


def pytest_sessionstart(session):
    _initialize_test_directory(session)
