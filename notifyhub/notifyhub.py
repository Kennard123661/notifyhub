import inspect
import os
import notifyhub.bots as bots
from functools import wraps


class watch(object):
    def __init__(self, messenger, **kwargs):
        super(watch, self).__init__()
        self.messenger = messenger
        self.kwargs = kwargs

    def __call__(self, func):
        # get filename
        @wraps(func)
        def wrapper():
            source_file = inspect.getsourcefile(func)
            source_filename = os.path.split(source_file)[-1].split('.')[:-1]

            function_name = str(func.__name__)
            function_info = '.'.join(source_filename + [function_name])
            send_message(message='INFO: task {} started!'.format(function_info),
                         messenger=self.messenger,
                         **self.kwargs)
            try:
                func()
                send_message(message='INFO: task {} completed'.format(function_info),
                             messenger=self.messenger,
                             **self.kwargs)
            except:
                send_message(message='ERR: task {} failed'.format(function_info),
                             messenger=self.messenger,
                             **self.kwargs)
                raise  # raises the exception function
        return wrapper


def send_message(message, messenger, **kwargs):
    frame_info = inspect.stack()[1]
    filepath = os.path.abspath(frame_info[1])
    del frame_info  # drop the reference to the stack frame to avoid reference cycles

    message = '{}\nfrom {}'.format(message, filepath)
    try:
        if messenger == 'telegram':
            telegram.send_message(message, chat_id=kwargs['chat_id'], bot_token=kwargs['bot_token'])
        else:
            raise NotImplementedError
    except:
        _handle_exception(message=message, messenger=messenger)
        return False
    return True


def _handle_exception(message, messenger):
    print('ERROR: Message {} failed to be send'.format(message, messenger))


def main():
    raise NotImplementedError


if __name__ == '__main__':
    main()
