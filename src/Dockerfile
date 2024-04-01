FROM python:3


RUN mkdir /src
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN pip install fastai
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
COPY . /src
WORKDIR /
RUN export FLAKS_APP=src
