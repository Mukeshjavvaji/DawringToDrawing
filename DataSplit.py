from tensorflow.keras.preprocessing import image_dataset_from_directory


class DataSplit:
    def __init__(self, image_size, split_ratio=0.3, batch_size=40, seed=19999):
        self.split_ratio = split_ratio
        self.batch_size = batch_size
        self.seed = seed
        self.image_size = image_size

    def split_data(self):
        train_ds = image_dataset_from_directory(
            "dataset",
            validation_split=self.split_ratio,
            subset="training",
            seed=self.seed,
            color_mode="grayscale",
            image_size=self.image_size,
            batch_size=self.batch_size
        )

        val_ds = image_dataset_from_directory(
            "dataset",
            validation_split=self.split_ratio,
            subset="validation",
            seed=self.seed,
            color_mode="grayscale",
            image_size=self.image_size,
            batch_size=self.batch_size
        )

        return train_ds, val_ds
