FROM python:3.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /house_price_prediction
COPY poetry.lock pyproject.toml /house_price_prediction/

RUN $HOME/.poetry/bin/poetry install --no-dev

COPY . /house_price_prediction

ENTRYPOINT /root/.poetry/bin/poetry run python -u -m house_price_prediction.main