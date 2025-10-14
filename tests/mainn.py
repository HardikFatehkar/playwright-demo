from daytona import Daytona, DaytonaConfig

# Define the configuration

config = DaytonaConfig(api_key="dtn_5241dd3c990bf1035bc820347c3ce1d4146d64e412aef0367ae78fde0efdcfe6")

# Initialize the Daytona client

daytona = Daytona(config)

# Create the Sandbox instance

sandbox = daytona.create()

# Run the code securely inside the Sandbox

response = sandbox.process.code_run('print("Hello World from code!")')
if response.exit_code != 0:
  print(f"Error: {response.exit_code} {response.result}")
else:
    print(response.result)

# Clean up

sandbox.delete()