import requests

def download_google_sheet(sheet_id, gid):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    response = requests.get(url)
    assert response.status_code == 200, 'Failed to download the file'

    csv = response.content
    return csv;


# Function that generates a card based on the inputted name and saves it as a .jpg file
def generate_card(name):
    OpenAiStuff.generate_and_save_image("Playing card of a board game, " + name, name + ".jpg")


# Function that returns a google sheet as a csv varaible based on a full google sheet url
def csv_from_google_sheet(google_sheet_url):
    google_sheet_id = google_sheet_url.split('/')[-2]
    google_sheet_gid = google_sheet_url.split('/')[-1].split('=')[-1]
    csv = download_google_sheet(google_sheet_id, google_sheet_gid)

    # Turn csv into array of arrays
    csv = csv.decode('utf-8')
    csv = csv.split('\r\n')
    csv = [row.split(',') for row in csv]
    return csv
