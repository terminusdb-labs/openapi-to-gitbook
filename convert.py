import sys
import yaml

def main():
    if len(sys.argv) < 2:
        print("Please provide a filename as the first argument")
        sys.exit(1)
    filename = sys.argv[1]
    process_yaml(filename)

def process_yaml(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
        for path, methods in data['paths'].items():
            print_entry(path, methods)

def print_entry(path, methods):
    for method in methods:
        print(f'''
{{% swagger src=".gitbook/assets/terminusdb.yaml" path="{path}" method="{method}" %}}
[terminusdb.yaml](.gitbook/assets/terminusdb.yaml)
{{% endswagger %}}

''')

if __name__ == '__main__':
    main()
