import requests
import json  # Import json module for formatting


class WebsiteCheckerManager:
    def __init__(self):
        self.add_website_url: str = "http://127.0.0.1:5000/add_website"

    def add_website(self):
        print("What website would you like to add? (Start with https://)")
        _website_to_add: str = input().strip()

        if not _website_to_add.startswith("https://") and not _website_to_add.startswith("http://"):
            print("Error: Please enter a valid website URL starting with https:// or http://")
            return

        try:
            response = requests.post(self.add_website_url, json={"value": _website_to_add})
            data = response.json()

            if response.status_code == 200:
                print("\nWebsite added successfully!")
                print("Your current websites:\n")

                # Display websites in a user-friendly format
                for index, site in enumerate(data.get("websites", []), start=1):
                    print(f"   {index}. {site}")

            elif response.status_code == 400:
                print(f"\nError: {data.get('error', 'Unknown error occurred')}")

            else:
                print(f"\nUnexpected response: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"\nConnection error: {e}")


if __name__ == "__main__":
    website_checker_manager = WebsiteCheckerManager()

    print("""
      
    - Welcome! What would you like to do? -
    
    1. Add a website
    2. Delete a website
    3. Download a text file of the program
    
    (Enter 1, 2, or 3)
    
    """)

    like_to_do = input().strip()

    match like_to_do:
        case "1":
            website_checker_manager.add_website()
        case "2":
            print("Feature not implemented yet.")
        case "3":
            print("Feature not implemented yet.")
        case _:
            print("Invalid input. Please enter 1, 2, or 3.")
