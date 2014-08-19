# coding:utf8

import sys
import json
import code
import signal
import threading
import traceback
from gfirefly.server.server import FFServer
from gevent import monkey
monkey.patch_os()


def dump_stacks(signal, frame):
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    codes = []
    for threadId, stack in sys._current_frames().items():
        codes.append("\n# Thread: %s(%d)" % (id2name.get(threadId, ""), threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            codes.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                codes.append("  %s" % (line.strip()))
                print "\n".join(codes)


def print_stack(signal, frame):
    d = {'_frame': frame}  # Allow access to frame object.
    d.update(frame.f_globals)  # Unless shadowed by global
    d.update(frame.f_locals)

    i = code.InteractiveConsole(d)
    message = "Signal received : entering python shell.\nTraceback:\n"
    message += ''.join(traceback.format_stack(frame))
    i.interact(message)


if __name__ == "__main__":
    signal.signal(signal.SIGUSR1, print_stack)
    signal.signal(signal.SIGUSR2, dump_stacks)

    args = sys.argv
    servername = None
    config = None
    if len(args) > 2:
        servername = args[1]
        config = json.load(open(args[2], 'r'))
    else:
        raise ValueError
    dbconf = config.get('db')
    memconf = config.get('memcached')
    sersconf = config.get('servers', {})
    masterconf = config.get('master', {})

    model_default_config = config.get('model_default', {})
    model_config = config.get('models', {})

    serconfig = sersconf.get(servername)
    ser = FFServer()
    ser.config(serconfig, servername=servername, dbconfig=dbconf, memconfig=memconf, masterconf=masterconf,
               model_default_config=model_default_config, model_config=model_config)
    ser.start()
