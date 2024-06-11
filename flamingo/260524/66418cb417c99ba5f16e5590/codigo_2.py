import pandas as pd
import numpy as np
from PIL import Image
import torch
from torchvision import transforms


class FKRDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file, image_dir, transform=None):
        self.keypoints_frame = pd.read_csv(csv_file)
        self.image_dir = image_dir
        self.transform = transform

    def __len__(self):
        return len(self.keypoints_frame)

    def __getitem__(self, idx):
        image_name = self.keypoints_frame.iloc[idx, 0]
        image_path = f"{self.image_dir}/{image_name}"
        image = Image.open(image_path)
        original_size = image.size

        keypoints = self.keypoints_frame.iloc[idx, 1:].values
        keypoints = keypoints.astype("float").reshape(-1, 2)

        sample = {
            "image": image,
            "keypoints": keypoints,
            "original_size": original_size,
        }

        if self.transform:
            sample = self.transform(sample)

        return sample


class ResizeTransform:
    def __init__(self, output_size):
        self.output_size = output_size

    def __call__(self, sample):
        image, keypoints, original_size = (
            sample["image"],
            sample["keypoints"],
            sample["original_size"],
        )
        new_h, new_w = self.output_size
        image = image.resize((new_w, new_h))

        # Scale the keypoints
        keypoints = keypoints * [new_w / original_size[0], new_h / original_size[1]]

        return {"image": image, "keypoints": keypoints, "original_size": (new_w, new_h)}


transform = ResizeTransform((256, 256))  # Resize the image to 256x256
dataset = FKRDataset("keypoints.csv", "images", transform)
