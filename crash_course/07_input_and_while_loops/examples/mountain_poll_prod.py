from typing import Dict


def collect_poll_responses() -> Dict[str, str]:
    responses: Dict[str, str] = {}
    while True:
        name = input("\nEnter your name: ").strip()
        if not name:
            print("Name cannot be empty. Try again.")
            continue

        mountain = input("Which mountain would you like to climb someday? ").strip()
        if not mountain:
            print("Mountain name cannot be empty. Try again.")
            continue

        responses[name] = mountain

        repeat = input("Would you like to let another person respond? (yes/no): ").strip().lower()
        if repeat == 'no':
            break
        elif repeat != 'yes':
            print("Invalid input. Assuming 'yes' and continuing...\n")

    return responses


def display_poll_results(responses: Dict[str, str]) -> None:
    print("\n--- Poll Results ---")
    for name, mountain in responses.items():
        print(f"{name} would like to climb {mountain}.")


def main() -> None:
    responses = collect_poll_responses()
    display_poll_results(responses)


if __name__ == "__main__":
    main()
