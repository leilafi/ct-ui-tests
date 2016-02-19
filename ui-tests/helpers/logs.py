def start(thisAction):
    global action
    action = thisAction
    print "\nTEST: Started %s..." %action


def done():
    print "TEST: Finished"