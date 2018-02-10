import os
from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory."
    )
    missing_args_message = "You must provide fully qualified name of app."

    def handle(self, **options):
        # get app fully qualified name
        fully_qualname = options.pop('name')
        names = fully_qualname.split('.')
        app_name = names[-1]

        # check if app parent module exists
        cwd = os.getcwd()
        for i in range(len(names)):
            target = os.path.join(cwd, *names[:i+1])
            if not os.path.exists(target) and i != len(names) - 1:
                raise CommandError('parent module not exists.')

        if len(names) == 1:
            target = None
        else:
            os.makedirs(target, exist_ok=True)

        # overwrite template directory
        file_parent = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(file_parent, 'app_template')

        new_options = options.copy()
        new_options['ful_qualnme'] = fully_qualname
        new_options['template'] = template_dir

        super().handle('app', app_name, target, **new_options)
