from jsonargparse import CLI
from defs import Converter, MyConverter

def main(converter: Converter):
    print(f"Success! converter={converter}")

if __name__ == "__main__":
    CLI(main)

