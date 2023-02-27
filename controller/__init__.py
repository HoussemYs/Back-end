# __all__=["login_controller", "configurations_controller", "permissions_controller", "profiles_controller", "roles_controller", "users_controller"]

import os
import glob

__all__=[os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]