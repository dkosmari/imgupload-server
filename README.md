# imgupload-server

This is a very simple web server that accepts image uploads through HTTP.

It was created to upload screenshots on the Wii U using the Home Menu's web browser. The
web pages were optimized for the Wii U's gamepad screen.


## Prerequisites

- Python

- (Optional) `virtualenv` module (if you want to run in a virtual environment)


## Usage (with `virtualenv`)

1. Run the `run.sh` script.

2. On the Wii U, navigate to the `http://ADDRESS:8080/` where `ADDRESS` is the address of
   the machine running this server.
   
3. Tap **Browse**, select a screen (TV or gamepad), then tap **Upload**.

4. The image will be uploaded to the web server, inside the directory `uploads`.


## Usage (without `virtualenv`)

0. Install the requirements by running 
   `pip install --requirement requirements.txt --upgrade`

1. Run `python imgupload-server.py`

2. On the Wii U, navigate to the `http://ADDRESS:8080/` where `ADDRESS` is the address of
   the machine running this server.
   
3. Tap **Browse**, select a screen (TV or gamepad), then tap **Upload**.

4. The image will be uploaded to the webserver, inside the directory `uploads`.


## Security

There is NO SECURITY implemented in this server. Anyone can upload anything they want. DO
NOT leave this server exposed to the internet, nor to your roommates.
