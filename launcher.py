"""Por pura preguiça, vai usar o antigo tk root do Updater... bom não dura tanto e mal é notavel
então deixei só pra não explodir
"""
import multiprocessing
import sys


def run():
    multiprocessing.freeze_support()
    self_test = len(sys.argv) == 3 and sys.argv[1] == '--self-test'
    if not self_test:
        from auto_update import update_frozen_app
        if update_frozen_app():
            return 0
    from main import main
    return main()


if __name__ == '__main__':
    sys.exit(run())
