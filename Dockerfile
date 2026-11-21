FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -c constraints-py312.txt '.[dev]'
ENV PIXELBENCH_TRACE_BACKEND=off
# The sandbox needs Landlock and seccomp inside the container (Linux kernel 5.13 or later on the host).
ENTRYPOINT ["python"]
CMD ["scripts/reproduce_paper.py"]
