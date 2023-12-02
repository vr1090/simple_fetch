FROM python:3.12
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip && \
    pip install pyinstaller
RUN pip install -r requirements.txt
RUN make build
RUN cp /app/dist/fetch .
RUN rm -rf src build dist main.spec makefile *.json *.html Dockerfile *.txt *.md
CMD ["/bin/bash"]
