
from class_def import Runner_Details

def main():
    runner1 = Runner_Details("Anna", 30)
    runner2 = Runner_Details("Pat", 25)

    runner1.add_run(10)
    runner1.add_run(10)

    runner2.add_run(25)

    print("Name     Goal    Km Run      Remaining")
    print("-"* 45)

    runners = [runner1, runner2]

    for runner in runners:
        print(runner)

main()