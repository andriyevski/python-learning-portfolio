# Homework from file tasks/8_14_Cars.md
## Task ## : 8.14
# 8_14_Cars
from typing import Dict, Any

def make_car(company: str, model: str, **car_info: Dict[str,Any]) -> Dict[str, Any]:
    """
    Car information about a car return in a dictionary
    """
    car = {
        'company' : company.title(),
        'model' : model.title()
        }
    car.update(car_info)
    return car


def main():
    result_1 = make_car('Nissan', 'X-Trail', color='Brown', engine=2.0, transmission = 'Auto')
    result_2 = make_car('Bmw', '7-Series', color='Ocean Blue', engine=4.4, transmission = 'Auto')
    print(result_1)
    print(result_2)

if __name__ == "__main__":
    main()
