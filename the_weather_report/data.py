def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.readlines()

def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]
