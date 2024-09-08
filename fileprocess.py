import json

def write_to_json(filename, data):
  """Writes data to a JSON file.

  Args:
    filename: The name of the JSON file.
    data: The data to be written (Python dictionary).
  """
  with open(filename, "r") as f:
    try:
      existing_data = json.load(f)
    except FileNotFoundError:
      existing_data = {}
  existing_data.update(data)  # Update with new data

  with open(filename, "w") as f:
    json.dump(existing_data, f, indent=4)


# new json file creating
def create_json_file(name,data_top_level=dict()):
    with open(name, "w") as f:
        json.dump(data_top_level, f, indent=4)
    print(f"\nFile {name} is created.")
    return "data.json"

