import subprocess
import sys
import pkg_resources

def install(package):
    
    list_of_package =([p.project_name for p in pkg_resources.working_set])  


    if package in list_of_package:
        pass
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])




