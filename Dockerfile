# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /src
WORKDIR /src

# Install dependencies
ADD requirement.txt /src/
RUN pip install -r requirement.txt

# Copy project
ADD . /src/