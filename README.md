# Facebook Live Stream Configurator


This Python script taps into the Facebook Live Video API and starts a new live stream. You can then configure your streaming software such as OBS, using the RTMPS secure stream URL provided by Facebook.

The program works by sending a POST request to the Facebook Live Video API, passing along parameters such as title and description for the live stream. A JSON object is returned, which includes the secure stream URL.

In the case of configuring OBS for Facebook streaming, the Facebook Live URL is predefined and only the stream key must be entered. This program parses the stream key from the JSON data and copies it to the clipboard so it can be easily pasted into your streaming software.

### Facebook Live Video API
For more information on the Facebook Live Video API, visit:
https://developers.facebook.com/docs/live-video-api/


### OBS
For more information on OBS, visit:
https://obsproject.com
