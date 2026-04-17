import click

@click.command()
@click.option('-f', '--file', required=True)
def main(file):
    print(''' 
┌────────────────────────────────────────────┐
│              SSH Log Analyzer              │
└────────────────────────────────────────────┘  
''')

    with open(file, "r", encoding="utf-8") as openfile:
        lines = openfile.readlines()

        print('Successful:')
        for line in lines:
            if "Successful login" in line:
                print(line.strip())

        print('Failed:')
        for line in lines:
            if "Failed login" in line:
                print(line.strip())

if __name__ == '__main__':
    main()