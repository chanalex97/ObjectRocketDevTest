# Use an official Python runtime as a parent image
FROM python:3-onbuild
# Set the working directory to /ObjectRocketDevTest
WORKDIR /ObjectRocketDevTest
#Copy the contents of the current directory into the container at /ObjectRocketDevTest
COPY . /ObjectRocketDevTest

CMD ["python", "./main.py"]