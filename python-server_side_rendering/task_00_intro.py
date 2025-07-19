import os

def generate_invitations(template, attendees):
    # 1. Tip Kontrolü
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Boşluk Kontrolleri
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. Davetiyeleri üret
    for index, attendee in enumerate(attendees, start=1):
        # Placeholder’ları işleme
        personalized = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        # 4. Dosya yazımı
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
