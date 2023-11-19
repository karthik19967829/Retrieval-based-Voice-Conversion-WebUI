import numpy as np
import os
# Set the directory path
directory_path = '/workspace/karthik/Retrieval-based-Voice-Conversion-WebUI/logs/mute/3_feature768'

# Check if the directory exists
if not os.path.exists(directory_path):
    print(f"The directory {directory_path} does not exist.")
else:
    # Iterate over the files in the directory
    for filename in os.listdir(directory_path):
        # Check for .npy extension
        if filename.endswith('.npy'):
            file_path = os.path.join(directory_path, filename)
            
            try:
                # Load the numpy array from .npy file
                data = np.load(file_path)
                print(f"{filename}: shape {data.shape}")
                print(data)
            except Exception as e:
                print(f"Could not load {filename}: {e}")
