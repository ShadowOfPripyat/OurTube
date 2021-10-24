
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import OurTubeError
from .controllers.base import Base
import os
from tinydb import TinyDB
from cement.utils import fs
from .controllers.downloads import Downloads

# configuration defaults
CONFIG = init_defaults('ourtube')
CONFIG['ourtube']['db_file'] = '~/.ourtube/db.json'

def extend_tinydb(app):
    #app.log.info('extending ourtube application with tinydb')
    db_file = app.config.get('ourtube', 'db_file')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    #app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(db_file))


class OurTube(App):
    """OurTube primary application."""

    class Meta:
        label = 'ourtube'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Downloads,
        ]

        hooks = [
            ('post_setup', extend_tinydb),
        ]


class OurTubeTest(TestApp,OurTube):
    """A sub-class of OurTube that is better suited for testing."""

    class Meta:
        label = 'ourtube'


def main():
    with OurTube() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except OurTubeError as e:
            print('OurTubeError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
