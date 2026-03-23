"""Simple data-cleaning simulation using Python data structures."""


def remove_duplicate_records(records):
    """Remove duplicate records based on record id."""
    unique_records = {}

    for record in records:
        unique_records[record["id"]] = record

    return list(unique_records.values())


def is_valid_record(record):
    """Validate a simulated record using business rules."""
    name = record.get("name", "").strip()
    age = record.get("age")
    city = record.get("city", "").strip()

    return bool(name) and isinstance(age, int) and age > 0 and bool(city)


def clean_records(records):
    """Remove duplicates and invalid records from a dataset."""
    deduplicated_records = remove_duplicate_records(records)
    cleaned_records = [record for record in deduplicated_records if is_valid_record(record)]
    unique_cities = {record["city"] for record in cleaned_records}

    city_counts = {}
    for city in unique_cities:
        city_counts[city] = sum(1 for record in cleaned_records if record["city"] == city)

    return cleaned_records, unique_cities, city_counts


def main():
    """Run a small data-cleaning workflow with sample records."""
    raw_records = [
        {"id": 1, "name": "Aarav", "age": 24, "city": "Mumbai"},
        {"id": 2, "name": "Bhavna", "age": 29, "city": "Delhi"},
        {"id": 2, "name": "Bhavna", "age": 29, "city": "Delhi"},
        {"id": 3, "name": "", "age": 31, "city": "Pune"},
        {"id": 4, "name": "Diya", "age": -5, "city": "Bengaluru"},
        {"id": 5, "name": "Eshan", "age": 27, "city": "Chennai"},
    ]

    cleaned_records, unique_cities, city_counts = clean_records(raw_records)

    print("Cleaned records:")
    for record in cleaned_records:
        print(record)

    print("\nUnique cities:", unique_cities)
    print("City counts:", city_counts)


if __name__ == "__main__":
    main()
