import subprocess

dependencies = [
    "pygame",
    "time",
    "random",
    "webbrowser"
]

def install_dependencies():
    for dependency in dependencies:
        try:
            subprocess.run(["pip", "install", dependency], check=True)
            print(f"Installed {dependency} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {dependency}. Error: {e}")

if __name__ == "__main__":
    install_dependencies()
