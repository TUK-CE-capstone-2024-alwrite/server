from torch import nn
import torch
from fastai.vision.all import Learner, Adam, DataLoaders, SaveModelCallback, EarlyStoppingCallback
import numpy as np

from src.EasyOCR.minji.dataset import train_test_data
from src.EasyOCR.minji.model import Model
from src.EasyOCR.minji.wrappers import CTCWrapper, distance_wrapper, accuracy_wrapper

loss_func = CTCWrapper(nn.CTCLoss(reduction="mean", zero_infinity=True))

def main():
    """Train the neural network using the default parameters."""
    train, val = train_test_data()
    dataloaders = DataLoaders(train, val)
    
       # 이전에 훈련된 모델 불러오기
    pretrained_model_dict = torch.load('src/EasyOCR/model_minji/model_3rd.pth', map_location=torch.device('cpu'))
    # 모델 추출
    pretrained_model = pretrained_model_dict['model']
    
    model = Model()

    # Adding Early Stopping Callback
    early_stopping = EarlyStoppingCallback(monitor='valid_loss', patience=5)

    learn = Learner(
        dataloaders,
        model,
        loss_func=loss_func,
        opt_func=Adam,
        metrics=[distance_wrapper, accuracy_wrapper],
        cbs=[
            SaveModelCallback("valid_loss", fname="valid_loss_best"),
            SaveModelCallback("distance_wrapper", fname="distance_best", comp=np.less),
            SaveModelCallback(
                "accuracy_wrapper", fname="accuracy_best", comp=np.greater
            ),
            early_stopping,  # Include the Early Stopping Callback
        ],
    )
    # Learning rate found by using learn.lr_find()
    learn.fit_one_cycle(10, 0.0014)
    
    learn.save('src/EasyOCR/model_minji/model_4th')

if __name__ == "__main__":
    main()
