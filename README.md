# diy-flipbook
Create your own Flipbooks (Daumenkinos).

## Dependencies

* [OpenCV](https://pypi.org/project/opencv-python/)
* [imageio](https://pypi.org/project/imageio/)
* [python-docx](https://pypi.org/project/python-docx/)

## Usage

There are two ways to create a flipbook.  

Either pass the path to an existing GIF / video to the program ...  

```bash
python src/main.py -f path_to_existing_file.gif
```

... or if no filepath is given, the camera stream will be opened and you can record a GIF from there.  

```bash
python src/main.py
```

There exist several command line arguments (see below) that allow you to customize your recording and the flipbooks size.  

The program will generate a flipbook for you in a Word-document so that you will only need to cut the frames out and connect them using a binder clip or something similiar. 

### Command line arguments

| flag | name | description | default |
| :---: | :--- | :--- | :--- |
| `-h` | `--help` | show this help message and exit | `None` |
| `-d` | `--device-id` | the id of the camera that shall be used | `1` |
|  | `--fps` | the fps to be used for recording (only available in camera mode) | `10` |
|  | `--square` | make the frame square (it will not be resized but cropped to the smaller edge length, only available in camera mode) | `False` |
|  | `--height` | height of the flipbook in cm | `3.0` |
|  | `--left-margin` | margin to the left of the image in cm that can be used to unite the single paper sheets | `3.0` |
|  | `--sheet-margin` | margin of the A4 sheet in cm used for top, bottom, left, right. Choose it depending on what your printer is capable of. | `1.27` |
| `-f` | `--filepath-video` | path to a an existing video or GIF that shall be converted to a flipbook. If not set, the camera stream will be used. | `None` |

### Key bindings

| key | usage |
| :---: | :--- |
| `SPACE` | take a video (start / stop with `SPACE`) |
| `q` or `ESC` | quit the program |

## Further notes / To Do's

* adapt the fps of existing videos
