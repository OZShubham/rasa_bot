FROM rasa/rasa:2.8.0-full

# Copy your Rasa project files to the container
COPY . /app

# Expose the Rasa server port
EXPOSE 5005

# Set the working directory
WORKDIR /app

# Start the Rasa server
CMD ["rasa", "run", "-p", "5005"]
    