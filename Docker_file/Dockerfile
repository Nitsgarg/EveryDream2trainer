#specify base image

FROM ubuntu

#maintainer of the image
MAINTAINER nitika garg <nitikagarg5665@gmail.com>

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app


# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

#Set the startup command
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]