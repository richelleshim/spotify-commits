import os

def setup_env():
    print("Welcome! Let's configure your Spotify API keys.")

    client_id = input("Enter your Spotify Client ID: ").strip()
    client_secret = input("Enter your Spotify Client Secret: ").strip()
    redirect_uri = input("Enter your Spotify Redirect URI (default: http://localhost:8888/callback): ").strip()

    if not redirect_uri:
        redirect_uri = "http://localhost:8888/callback"

    # Write to .env file
    with open(".env", "w") as env_file:
        env_file.write(f"SPOTIPY_CLIENT_ID={client_id}\n")
        env_file.write(f"SPOTIPY_CLIENT_SECRET={client_secret}\n")
        env_file.write(f"SPOTIPY_REDIRECT_URI={redirect_uri}\n")

    print("\nConfiguration saved to .env!")
    print("You can edit this file later if needed.")

if __name__ == "__main__":
    setup_env()
