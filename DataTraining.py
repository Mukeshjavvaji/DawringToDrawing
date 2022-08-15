class DataTraining:
    def __init__(self, epochs):
        self.epochs = epochs

    def fit(self, model, train_ds, val_ds):
        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=self.epochs,
            verbose=1
        )

        model.save('models/model_20220814-115719')

        return model
