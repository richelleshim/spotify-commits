from setuptools import setup, find_packages

setup(
    name="spotify-commits",
    version="1.0.0",
    author="Richelle Shim",
    author_email="richelleshim@gmail.com",
    description="A Git hook to append the current Spotify song to commit messages.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/richelleshim/spotify-commits",
    packages=find_packages(),
    install_requires=[
        "spotipy",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "spotify-git-bot=spotify_commits.spotify_bot:main",
            "setup-spotify-env=spotify_commits.setup_env:setup_env",
            "install-git-hook=spotify_commits.install_git_hook:install_git_hook",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
