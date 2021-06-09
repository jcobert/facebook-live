import requests
import subprocess

user_id = "INSERT YOUR FACEBOOK USER ID HERE"
access_token = "INSERT YOUR FACEBOOK API USER ACCESS TOKEN HERE"
url = f"https://graph.facebook.com/{user_id}/live_videos"
status = "LIVE_NOW"
title = "MY DEFAULT LIVE STREAM TITLE"
description = "MY DEFAULT LIVE STREAM DESCRIPTION"

print("\n*********************************")
print("Facebook Live Stream Configurator")
print("*********************************\n")
print("This program generates a new live stream and copies the stream key to your clipboard.\n")
print("These are the default Title and Description values:")
print(f"Title: {title}\nDescription: {description}\n")

user_title = input("Enter a title (leave blank for default)... ")
user_description = input("Enter a description (leave blank for default)... ")

if user_title != "":
    title = user_title
if user_description != "":
    description = user_description

params = {
    "status": status,
    "title": title,
    "description": description,
    "access_token": access_token
}

response = requests.post(url, params=params)
data = response.json()
stream_url = data["secure_stream_url"]
key_start_index = stream_url.rfind("/")
stream_key = stream_url[key_start_index + 1:]


def copy_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

copy_to_clipboard(stream_key)

print("\nThe stream key has been copied to your clipboard. Just in case, here it is:\n")
print(stream_key)

