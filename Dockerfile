FROM python:3.7

# Set timezone to JST
ENV TZ Asia/Tokyo

# Install packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    ca-certificates \
    locales && \
    locale-gen ja_JP.UTF-8 && \
    echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Language
ENV LANG ja_JP.UTF-8

ENV APP_ROOT /var/app/
WORKDIR $APP_ROOT

RUN pip install --upgrade pip && pip install pipenv

# Install gcloud.
RUN pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib \
    && curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /var/app/google-cloud-sdk.tar.gz  \
    && mkdir -p /usr/local/gcloud \
    && tar -C /usr/local/gcloud -xvf /var/app/google-cloud-sdk.tar.gz \
    && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

COPY Pipfile $APP_ROOT
COPY Pipfile.lock $APP_ROOT
RUN pipenv install --dev
