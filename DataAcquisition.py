from pathlib import Path
from quickdraw import QuickDrawDataGroup


class DataAcquisition:
    def __init__(self) -> None:
        self.image_size = (28, 28)

    def generate_class_images(self, name, max_drawings, recognized):
        directory = Path("dataset/" + name)

        if not directory.exists():
            directory.mkdir(parents=True)

        images = QuickDrawDataGroup(
            name, max_drawings=max_drawings, recognized=recognized)

        for img in images.drawings:
            filename = directory.as_posix() + "/" + str(img.key_id) + ".png"
            img.get_image(stroke_width=3).resize(
                self.image_size).save(filename)
