FROM python:3.6

# add requirements.txt to the image
# ADD ./app/requirements.txt /app/requirements.txt

# set working directory to /app/
WORKDIR /app/

# install python dependencies
# RUN pip install -r requirements.txt

# create unpriviledged user
RUN adduser --disabled-password --gecos '' user
