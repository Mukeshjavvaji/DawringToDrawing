from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization


class DataModelling:
    def __init__(self, image):
        self.input_shape = (image[0], image[1], 1)

    def generate_model(self):
        model = Sequential([
            Rescaling(1. / 255, input_shape=self.input_shape),
            BatchNormalization(),
            Conv2D(6, kernel_size=(3, 3), padding="same", activation="relu"),
            Conv2D(8, kernel_size=(3, 3), padding="same", activation="relu"),
            Conv2D(10, kernel_size=(3, 3), padding="same", activation="relu"),
            BatchNormalization(),
            MaxPooling2D(pool_size=(2, 2)),
            Flatten(),
            Dense(700, activation='relu'),
            BatchNormalization(),
            Dropout(0.2),
            Dense(500, activation='relu'),
            BatchNormalization(),
            Dropout(0.2),
            Dense(400, activation='relu'),
            Dropout(0.2),
            Dense(345, activation='softmax')
        ])

        return model

    def compile_model(self, model):
        model.compile(
            optimizer="adam",
            loss=SparseCategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        return model
