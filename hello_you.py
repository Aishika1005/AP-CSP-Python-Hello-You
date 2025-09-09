"""
This program asks a user for thier name and says "Hello, name!"
Aishika Kolla - September 2025
"""

# This is a single line comment
def main() -> None:
  name: str = "Aishika"
  print("Hello,", name, "!")
  print("Hello," + name + "!")
  print(f"Hello, {name}")

if __name__ == "__main__":
    main()