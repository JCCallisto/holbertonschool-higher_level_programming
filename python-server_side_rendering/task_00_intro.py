import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template is not a string, no output files generated.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees is not a list of dictionaries, no output files generated.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return


    keys = ["name", "event_title", "event_date", "event_location"]
    for idx, attendee in enumerate(attendees, 1):
        processed = template
        for k in keys:
            val = attendee.get(k)

            if val is None:
                val = "N/A"
            processed = processed.replace("{" + k + "}", str(val))

        filename = f"output_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(processed)

try:
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
except ImportError:
    pass
