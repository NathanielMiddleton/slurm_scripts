import subprocess
import json

# Run sinfo --json and capture the output
output = subprocess.run(["sinfo", "--json"], 
capture_output=True)

# Check if the command was successful
if output.returncode == 0:
    # Parse the json output
    data = json.loads(output.stdout)

    # Loop through the nodes and print their details
    for node in data["nodes"]:
        # Get the node name, state, allocated memory and total memory
        name = node["name"]
        state = node["state"]
        alloc_mem = node["alloc_memory"]
        total_mem = node["real_memory"]
        total_cpus = node["cpus"]
        alloc_cpus = node["alloc_cpus"]
        total_gres = node["gres"]
        alloc_gres = node["gres_used"]

       "gres": "gpu:a100:1",
       "gres_used": "gpu:a100:1(IDX:0)"

        # Calculate the percentage of consumed memory
        percent_mem = round(alloc_mem / total_mem * 100, 2)
        available_cpus = total_cpus - alloc_cpus

        # Print the details
        print(f"Node: {name}")
        print(f"State: {state}")
        print(f"Allocated memory: {alloc_mem} MB")
        print(f"Total memory: {total_mem} MB")
        print(f"Percentage of consumed memory: {percent_mem}%")
        print(f"Available CPUs: {available_cpus} out of {total_cpus}")
        if total_gres:
            print(f"{alloc_gres})
        print()
else:
# Print an error message if the command failed
    print(f"Error: sinfo --json failed with code {output.returncode}")
