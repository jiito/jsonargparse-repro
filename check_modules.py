import sys
import os
import minimal_repro  # This imports it as a module

class Model:
    pass

def check():
    main_model = Model
    imported_model = minimal_repro.Model
    
    print(f"Main Model: {main_model}, Module: {main_model.__module__}")
    print(f"Imported Model: {imported_model}, Module: {imported_model.__module__}")
    
    main_mod = sys.modules['__main__']
    imported_mod = sys.modules['minimal_repro']
    
    print(f"Main module file: {getattr(main_mod, '__file__', None)}")
    print(f"Imported module file: {getattr(imported_mod, '__file__', None)}")
    
    # Check if they point to the same file
    if getattr(main_mod, '__file__', None) and getattr(imported_mod, '__file__', None):
        print(f"Files match: {os.path.abspath(main_mod.__file__) == os.path.abspath(imported_mod.__file__)}")

if __name__ == "__main__":
    check()

