#!/bin/env python3

# imgupload-server - A simple web server to accept image uploads.
#
# Copyright (C) 2024  Daniel K. O.
#
# SPDX-License-Identifier: GPL-3.0-or-later


import cherrypy
import datetime
import os


uploaddir = "uploads"


class ImgUploader(object):

    @cherrypy.expose
    def index(self, image=None):
        return """
<hml>
<head>
<title>Image upload</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<style>
form {
    max-width: 100%;
    max-height: 100%;
    width: 100%;
    height: 80%;
}
input {
    width: 100%;
    height: 40%;
    font-size: 2.0em;
    display: block;
}
input[type="file"]::-webkit-file-upload-button {
    width: 30%;
    height: 100%;
    display: block-inline;
}
div {
    padding: 1.5em;
}
</style>
</head>
<body>
<form method="post" action="upload" enctype="multipart/form-data">
<div><input type="file" name="image" accept="image/*,.png,.jpg"/></div>
<div><input type="submit" value="Upload"/></div>
</form>
</body>
</html>
"""


    @cherrypy.expose
    def upload(self, image):
        if image.file is None:
            return '<h1 style="color:red;">ERROR: no image selected!</h1>'
        os.makedirs(uploaddir, exist_ok=True)
        now = datetime.datetime.now()
        timestamp = now.isoformat(sep=" ", timespec="seconds").replace(":", "-")
        filename = "{}/[{}] {}".format(uploaddir, timestamp, image.filename)
        with open(filename, "wb") as f:
            f.write(image.file.read())
        return """
<html>
<head>
<title>Uploaded!</title>
<meta http-equiv="refresh" content="3; url=/" /><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>
<h1 style="text-align: center;"><font color="navy"><b>{}</b></font> uploaded.</h1>
</body>
</html>
""".format(image.filename)


if __name__ == '__main__':
    cherrypy.config["server.socket_host"] = "0.0.0.0"
    cherrypy.quickstart(ImgUploader())
