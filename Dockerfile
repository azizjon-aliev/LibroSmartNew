# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set environment variables
ENV DJANGO_ENV=production \
    PROJECT_DIR="/code" \
    PORT=8000 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Set working directory
WORKDIR $PROJECT_DIR

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev

# Copy only requirements to cache them in docker layer
COPY requirements.txt $PROJECT_DIR/

# Install project dependencies:
RUN pip install -r $PROJECT_DIR/requirements.txt

# Copy project files and directories
COPY . $PROJECT_DIR/

# Setting up proper permissions:
RUN chmod +x ${PROJECT_DIR}/scripts/start_api.sh \
  && mkdir -p /${PROJECT_DIR}/media /${PROJECT_DIR}/static \
  && chmod +x /${PROJECT_DIR}/media/ /${PROJECT_DIR}/static/


# This container exposes port 8000 to the outside world
EXPOSE $PORT

# Run the application:
CMD ["./scripts/start_api.sh"]