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
        successful = 0
        failed = 0

        print('Successful:')
        for line in lines:
            if "Successful login" in line:
                print(line.strip())
                successful += 1
        

        print('\nFailed:')
        for line in lines:
            if "Failed login" in line:
                print(line.strip())
                failed += 1

        print('\nStatistic:')
        print(f'Number of successful attempts: {successful}')
        print(f'Number of failed attempts: {failed}')

if __name__ == '__main__':
    main()