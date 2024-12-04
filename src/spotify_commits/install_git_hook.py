import os
import shutil
import sys

def install_git_hook(repo_path="."):
    hook_name = "prepare-commit-msg"
    hooks_dir = os.path.join(repo_path, ".git", "hooks")
    
    if not os.path.exists(hooks_dir):
        print("Error: Not a Git repository (or any of the parent directories).")
        sys.exit(1)

    # Path to the hook template
    hook_template_path = os.path.join(
        os.path.dirname(__file__), "git_hooks", hook_name
    )

    # Destination for the hook in the repository
    destination_path = os.path.join(hooks_dir, hook_name)

    # Copy the hook
    shutil.copyfile(hook_template_path, destination_path)

    # Make it executable
    os.chmod(destination_path, 0o755)

    print(f"Git hook '{hook_name}' installed successfully in {hooks_dir}.")

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    install_git_hook(repo_path)
