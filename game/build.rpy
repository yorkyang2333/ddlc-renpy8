# Build configuration for DDLC repackaged with Ren'Py 8.5.2

init python:
    # Basic build configuration
    build.directory_name = "DDLC-1.1.1"
    build.executable_name = "DDLC"

    # Classify files for distribution
    build.classify('game/**.rpa', 'all')
    build.classify('game/**.rpyc', 'all')
    # Prevent source files from shipping
    build.classify('game/**.rpy', None)
    # MUST exclude firstrun so the game initializes properly on the player's end!
    build.classify('game/script_version.txt', None)
    build.classify('game/python-packages/**', 'all')
    build.classify('characters/**', 'all')

    # Exclude cache and temporary files
    build.classify('game/cache/**', None)
    build.classify('game/saves/**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    # Exclude logs and scripts
    build.classify('**.json', None)
    build.classify('**.py', None)
    build.classify('log.txt', None)
    build.classify('errors.txt', None)
    build.classify('traceback.txt', None)

    # Documentation
    build.documentation('*.html')
    build.documentation('*.txt')

    # Allow integrated GPU for Mac
    build.allow_integrated_gpu = True
