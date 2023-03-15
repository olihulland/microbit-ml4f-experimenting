fileInPath = "source/simpleBinaryModel.ml4f"
outDir = "source/"
outName = "model"

count = 0
byte_array = []
with open(fileInPath, "rb") as binary_file:
    while byte := binary_file.read(1):
        count += 1
        byte_array.append(int.from_bytes(byte, byteorder="little"))

print(f"count: {count}")

cppOutStr = f"""
    #include <cstdint>
    #include "{outName}.h"
    
    const uint8_t model [] = {{
        {str(byte_array)[1:-1]}
    }};
"""

headerOutStr = """
    #include <cstdint>
    
    extern const uint8_t model [];
"""

with open(f"{outDir}{outName}.cpp", "w") as f:
    f.write(cppOutStr)

with open(f"{outDir}{outName}.h", "w") as f:
    f.write(headerOutStr)