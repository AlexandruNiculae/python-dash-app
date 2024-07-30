import os
import base64

from constants.storage import BATCH_SIZE


class ScreenshotsStorage:

    def __init__(self) -> None:
        self.dir_path = r"C:\Users\Developer\Pictures\Screenshots"
        self.batch_size = BATCH_SIZE

    def get_image_data(self, image_url: str) -> str:
        with open(image_url, "rb") as image_file:
            img_data = base64.b64encode(image_file.read())
            img_data = img_data.decode()
            img_data = "{}{}".format("data:image/jpg;base64, ", img_data)
            return img_data

    def get_image_urls(self, offset: int=0) -> list[str]:
        batch = []
        images = os.listdir(self.dir_path)
        for imagename in images[offset:offset+self.batch_size]:
            imagepath = os.path.join(self.dir_path, imagename)
            batch.append(imagepath)

        return batch
