from quickdraw import QuickDrawData

from DataAcquisition import DataAcquisition
from DataSplit import DataSplit
from DataModelling import DataModelling
from DataTraining import DataTraining

# -------------Global Variables------------
EXAMPLES = 1200
IMAGE = (28, 28)
SPLIT_RATIO = 0.2
BATCH_SIZE = 32
SEED = 2022
EPOCHS = 14
# -----------------------------------------


if __name__ == "__main__":
    da = DataAcquisition()
    for label in QuickDrawData().drawing_names:
        da.generate_class_images(label, max_drawings=EXAMPLES, recognized=True)

    ds = DataSplit(IMAGE, SPLIT_RATIO, BATCH_SIZE, SEED)
    train, val = ds.split_data()

    dm = DataModelling(IMAGE)
    model = dm.compile_model(dm.generate_model())

    dt = DataTraining(EPOCHS)
    # Now the model is ready for predictions and etc
    model = dt.fit(model, train, val)
