import subprocess


def execute_command_project(pattern, directory, name, python_version, kivy_version, *args):
    command = f"kivymd.create_project {pattern} {directory} {name} {python_version} {kivy_version}"
    command = " ".join([command, *args])
    excutor = result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if (excutor.stderr):
        print("Errors:")
        print(result.stderr)
    return excutor.stdout
