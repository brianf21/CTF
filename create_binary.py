import os
import struct
import random

# Function to create binary file with hidden flag
def create_binary_file_with_hidden_flag(filename, flag):
    # Create some random binary data
    random_data_length = 2048  # Medium sized file
    random_bytes = bytearray(random.randint(0, 255) for _ in range(random_data_length))
    
    # Convert the flag to bytes
    flag_bytes = flag.encode('utf-8')
    
    # Choose a random position to insert the flag
    # We'll keep it away from the very beginning and end
    position = random.randint(512, random_data_length - 512 - len(flag_bytes))
    
    # Create the final binary data with the flag embedded
    binary_data = random_bytes[:position]
    binary_data.extend(flag_bytes)
    binary_data.extend(random_bytes[position:random_data_length-len(flag_bytes)])
    
    # Add some metadata and headers to make it look like a legitimate file
    header = bytearray([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])  # PNG-like header
    
    # Add some fake metadata
    metadata = bytearray()
    metadata.extend(struct.pack('>I', random.randint(1000000, 9999999)))  # Some random integers
    metadata.extend(b'DATA')  # Marker
    metadata.extend(struct.pack('>H', random.randint(1, 65535)))  # More random data
    
    # Combine everything
    final_data = header + metadata + binary_data
    
    # Write to file
    with open(filename, 'wb') as f:
        f.write(final_data)
    
    return {
        'filename': filename,
        'size': len(final_data),
        'flag_position': position + len(header) + len(metadata),
        'flag': flag
    }

# Create the file with the hidden flag
result = create_binary_file_with_hidden_flag('hidden_flag_file.bin', 'bcCTF{y0u_f0und_th3_fl4g}')

# Print information about the file (for demonstration purposes)
print(f"Binary file created: {result['filename']}")
print(f"File size: {result['size']} bytes")
print(f"Flag '{result['flag']}' hidden at position: {result['flag_position']}")

# Code to find the hidden flag (for testing/verification)
def find_flag(filename, flag_pattern="bcCTF{"):
    with open(filename, 'rb') as f:
        data = f.read()
    
    position = data.find(flag_pattern.encode('utf-8'))
    if position >= 0:
        # Try to extract the complete flag assuming it ends with '}'
        end_position = data.find(b'}', position)
        if end_position >= 0:
            return data[position:end_position+1].decode('utf-8')
    return None

# Verify that the flag can be found
found_flag = find_flag(result['filename'])
print(f"Flag found in verification: {found_flag}")
