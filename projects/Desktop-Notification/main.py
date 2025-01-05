# install plyer using this command "pip install plyer"
from plyer import notification

# Display a notification with an icon
notification.notify(
    title="Python Project", # This is the Title
    message="Here is your notification body", # This is the body of the notification
    app_icon="logo.ico",  # Replace with the path to your icon file
    timeout=10  # Duration in seconds
)
