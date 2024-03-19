import scratchattach as scratch3
import google.generativeai as genai
import time

encoded = ''

GOOGLE_API_KEY = 'GOOGLE_API_KEY_HERE'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

alphabet = ['', '', '', '', '', '', '', '', '', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*', '!', '?', ' ', ',', '.', '-', "'", '"', '\n', ':', 'Ü', 'ö', '/', '`', '(', ')', 'Ñ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ';', '_', '=', '°', '️️️️️️️', '#']

numbers = []

project = scratch3.get_project(983854750)
# This line logs into your Scratch account:
session = scratch3.Session(
    "YOUR_SESSION_ID_HERE",
    username="USERNAME_HERE")  # Replace with your username

# This line connects to your project's cloud variables:
conn = session.connect_cloud('PROJECT_ID_HERE')

# Get the value of a cloud variable:
time.sleep(1)
conn.set_var('SERVER', '0')
conn.set_var('USER', '0')
conn.set_var('VERSION', '0')
user = scratch3.get_var("PROJECTID_HERE", "VARIABLE")


def encode(text):
    global encoded
    encoded = ''
    idx = 0
    for i in range(len(text)):
        letter = text[idx]
        list_index = alphabet.index(letter)
        encoded = encoded + str(list_index)
        idx += 1

    print(encoded)


decoded = ''


def decode(encoded_str):
    idx = 0
    lnumbers = []
    while idx < len(encoded_str):
        number = int(encoded_str[idx:idx + 2])
        lnumbers.append(number)
        idx += 2

    decode_part(lnumbers)


def decode_part(pnumbers):
    global decoded
    decoded = ''
    for num in pnumbers:
        letter = alphabet[num]
        decoded = decoded + letter


print("Successfully launched!")


while True:
    user = scratch3.get_var("PROJECTID_HERE", "VARIABLE_HERE")
    print(user)
    time.sleep(0.6)
    if not user == '0':
        print(user)
        decode(user)
        time.sleep(1)
        print(decoded)
        response = model.generate_content(decoded)
        time.sleep(1)
        print('Gemini: ' + response.text)
        encode(response.text.upper())
        conn.set_var('VARIABLE_HERE', encoded[0:255])
        time.sleep(0.6)
        conn.set_var('VARIABLE_HERE', '0')
        conn.set_var('VARIABLE_HERE', '0')
