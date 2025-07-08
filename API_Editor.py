import os
from dotenv import load_dotenv

def update_gemini_api_key(new_key: str, env_file=".env"):
    """
    Updates the GEMINI_API_KEY in the .env file.
    Creates the file if it doesn't exist.
    """
    # Load existing env vars if any
    load_dotenv(dotenv_path=env_file)

    lines = []
    key_found = False

    # Read existing content
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    lines.append(f"GEMINI_API_KEY={new_key}\n")
                    key_found = True
                else:
                    lines.append(line)

    if not key_found:
        lines.append(f"GEMINI_API_KEY={new_key}\n")

    # Write updated content
    with open(env_file, "w") as f:
        f.writelines(lines)