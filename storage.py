import json
import os

def load_accounts():
    if not os.path.exists("accounts.json"):
        return {}

    try:
        with open("accounts.json","r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"⚠️ Error loading accounts: {e}")
        return {}

def save_accounts(accounts):
    try:
        with open("accounts.json","w") as f:
            json.dump(accounts, f, indent=2)
    except Exception as e:
        print(f"⚠️ Error saving accounts: {e}")