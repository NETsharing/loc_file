def pid_locker():
    if os.access(os.path.expanduser("~/.lockfile.yos_migrator.lock"), os.F_OK):
        pidfile = open(os.path.expanduser("~/.lockfile.yos_migrator.lock"), "r")
        pidfile.seek(0)
        old_pd = pidfile.readline()
        if os.path.exists("/proc/%s" % old_pd):
            exit(1)
        else:
            os.remove(os.path.expanduser("~/.lockfile.yos_migrator.lock"))
    pidfile = open(os.path.expanduser("~/.lockfile.yos_migrator.lock"), "w")
    pidfile.write("%s" % os.getpid())
    pidfile.close()
