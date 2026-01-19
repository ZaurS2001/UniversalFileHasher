import hashlib
import os
import tkinter as tk
from tkinter import filedialog

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    file_path = filedialog.askopenfilename(
        title="Select a file to hash",
        filetypes=[("All files", "*.*")]
    )
    
    root.destroy()
    return file_path

def generate_all_hashes(file_path):
    if not file_path or not os.path.isfile(file_path):
        print("No valid file selected.")
        return

    algorithms = hashlib.algorithms_available
    
    print(f"\n[!] Analyzing: {os.path.abspath(file_path)}")
    print("=" * 60)

    for alg in sorted(algorithms):
        try:
            if alg.startswith('shake_'):
                continue
                
            hash_obj = hashlib.new(alg)
            
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)
            print(f"{alg.upper():<15}: {hash_obj.hexdigest()}")
            
        except (ValueError, TypeError):
            continue
    input("\nPress any key to quit the program...")

if __name__ == "__main__":
    selected_file = get_file_path()
    if selected_file:
        generate_all_hashes(selected_file)
    else:
        print("Operation cancelled by user.")
