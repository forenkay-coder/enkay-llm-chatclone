"""Vercel serverless entrypoint for Python.

This file exposes the FastAPI app for Vercel's Python runtime by
importing the ASGI handler from the backend.
"""

from backend.main import handler as app