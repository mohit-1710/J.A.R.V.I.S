import subprocess

def list_installed_packages():

    try:
        installed_pacakages = subprocess.check_output(['pip' , 'freeze']).decode('utf-8')

        with open ('requirement.txt' , 'w') as file :
            file.write(installed_pacakages)

            print("the installed packages have been listed in requirements.txt")

    except subprocess.CalledProcessError as e :
        print(f"An error ocurred while listing the package: {e}")

if __name__ == "__main__":
    list_installed_packages()