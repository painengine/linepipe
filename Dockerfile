FROM python:3.8
ADD . build/
RUN apt update && apt upgrade && apt clean
RUN cd build \
	&& git describe --long --always --dirty \
	&& pip install --upgrade pip \
	&& pip install -v .
