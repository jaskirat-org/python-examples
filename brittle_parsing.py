def parse_config_file(filename):
  config_data = {}
  with open(filename, "r") as f:
    for line in f:
      if not line.startswith("#") and "=" in line:
        key, value = line.strip().split("=")
        config_data[key] = value.strip() 
  return config_data

config = parse_config_file("settings.cfg")
try:
  api_key = config["api_key"]  
except KeyError:
  print("Error: Missing API key in configuration file!")

