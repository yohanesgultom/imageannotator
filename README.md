# Image Annotator
Image face annotator with Django

### Dependency:

* Python 2.x >= 2.7
* Django >= 1.10

### Running

Default run script below will bring the app up in `http://localhost:8000`

```
python manage.py runserver
```

### Usage guide

* Put the files in a directory inside `<strong>annotator/static/images/video/` eg. (`annotator/static/images/video/01`)
* Select directory to load the images/frames and start annotating
* Click on the image to add an annotation (rectangle shape)
* Drag the rectangle to match desired position
* Resize the rectangle by clicking it and slide the slider in the toolbar
* To indicate that the face has mouth opened click the rectangle and check Mouth open in toolbar (the rectangle will be Orange instead of Yellow)
* Click the rectangle and press [Delete] key (in keyboard) to remove it
* Press [Left arrow] or [Right arrow] key (in keyboard) to navigate between image (frame)
* Press Save button to save the annotation to server (as pickle). The file will be saved in `annotator/_config/directoryname` eg. (`annotator/_config/01`)
