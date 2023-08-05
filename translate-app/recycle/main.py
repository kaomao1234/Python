# Based on this file:
#   https://github.com/pallets/werkzeug/blob/master/werkzeug/_reloader.py


import time
import os
import sys
import subprocess
import view
PY2 = sys.version_info[0] == 2


class Reloader(object):

    RELOADING_CODE = 3

    def start_process(self):
        """Spawn a new Python interpreter with the same arguments as this one,
        but running the reloader thread.
        """
        while True:
            print("starting Tkinter application...")

            args = [sys.executable] + sys.argv
            env = os.environ.copy()
            env['TKINTER_MAIN'] = 'true'

            # a weird bug on windows. sometimes unicode strings end up in the
            # environment and subprocess.call does not like this, encode them
            # to latin1 and continue.
            if os.name == 'nt' and PY2:
                for key, value in env.iteritems():
                    if isinstance(value, unicode):
                        env[key] = value.encode('iso-8859-1')

            exit_code = subprocess.call(args, env=env,
                                        close_fds=False)
            if exit_code != self.RELOADING_CODE:
                return exit_code

    def trigger_reload(self):
        self.log_reload()
        sys.exit(self.RELOADING_CODE)

    def log_reload(self):
        print("reloading...")


def run_with_reloader(root, *hotkeys):
    """Run the given application in an independent python interpreter."""
    import signal
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    reloader = Reloader()
    start_time: float = time.time()
    try:
        if os.environ.get('TKINTER_MAIN') == 'true':

            for hotkey in hotkeys:
                root.bind_all(hotkey, lambda event: reloader.trigger_reload())

            if os.name == 'nt':
                root.wm_state("iconic")
                root.wm_state("zoomed")

            end_time: float = time.time()
            print("reload time: ",format(end_time-start_time,".4f"))
            root.mainloop()
        else:
            sys.exit(reloader.start_process())

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    from customtkinter import CTk

    class App(CTk):
        def __init__(self):
            CTk.__init__(self)
            self.title("Ctrl-R for reload")
            view.View(self).pack(fill="both", expand=True)

    run_with_reloader(App(), "<Control-R>", "<Control-r>")
