from setuptools import setup, find_packages
import logging
print(">>> logging module:", logging.__file__)

setup(
  name="agentic-trading-system",
  version="0.0.1",
  author="Praveen",
  author_email="pks101295@gmail.com",
  packages=find_packages(),
  install_requires=['langchain','lancedb','tavily-python','polygon-api-client','langgraph'],
)