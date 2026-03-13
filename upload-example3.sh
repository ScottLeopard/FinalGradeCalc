# Before running the SCP command on your local computer, 
# make sure you have completed these steps on the server:
#  (1) Running `django_setup.sh`
#  (2) Running `python manage.py startapp <app_name>`
#
# The following SCP command is for Google Cloud.
# For AWS EC2, use your PEM file instead.

KEY_FILE="~/.ssh/id_ed25519_google_cloud"   # SSH key file
USER="msong_gclassroom"                     # Remote username
IP="104.197.57.71"                           # Remote server IP
WORKSPACE="~/webworkspace"                  # Remote directory

scp -r -i $KEY_FILE ./* $USER@$IP:$WORKSPACE
