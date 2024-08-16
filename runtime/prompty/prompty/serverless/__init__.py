# __init__.py
from prompty.core import InvokerException

try:
    from .executor import ServerlessExecutor
    from .processor import ServerlessProcessor
except ImportError:
    raise InvokerException("Error registering ServerlessExecutor and ServerlessProcessor", "serverless")