# TO DO List

## Set up a Python Environment

```sh
python -m venv .venv
```
For Windows 
```sh
PS> python -m venv venv
```
For Linux/Mac Shell
```sh
$ python3 -m venv venv
```

install numpy and opencv (if already have, Skip)
```
python3 -m pip install opencv-python
python3 -m pip install numpy
```

Go Unto which folder directory you wanted to test,
In my case it's blurring
```sh
cd blurring
python3 image-blurring.py
```

You can edit the parameters or set an image by editing
```py
image_name = 'YOUR_SPECIFIED_IMAGE'
```
