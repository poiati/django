# For testing that auth backends can be referenced using a convenience import
from .test_auth_backends import ImportedModelBackend, OtherImportedModelBackend

__all__ = ['ImportedModelBackend', 'OtherImportedModelBackend']
