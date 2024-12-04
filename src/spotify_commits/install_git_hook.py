import os
import shutil
import sys

def install_git_hook(repo_path="..."):
    """Installs the prepare-commit-msg hook into the .git/hooks directory."""
    repo_path="..."
    hooks_dir = os.path.join(repo_path, ".git", "hooks")
    hook_name = "prepare-commit-msg"
    source_hook = os.path.join(os.path.dirname(__file__), "../git-hooks", hook_name)
    target_hook = os.path.join(hooks_dir, hook_name)

    print(f"Source hook: {source_hook}")
    print(f"Target hook: {target_hook}")

    if not os.path.exists(hooks_dir):
        print("Error: Not a Git repository (or any of the parent directories).")
        sys.exit(1)

    # Check if the source hook exists
    if not os.path.exists(source_hook):
        print(f"Error: Source hook file '{source_hook}' does not exist.")
        sys.exit(1)

    # Copy the hook
    try:
        shutil.copyfile(source_hook, target_hook)
        os.chmod(target_hook, 0o755)  # Make it executable
        print(f"Hook '{hook_name}' installed successfully in {hooks_dir}.")
    except Exception as e:
        print(f"Failed to install hook: {e}")
        sys.exit(1)

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    install_git_hook(repo_path)
