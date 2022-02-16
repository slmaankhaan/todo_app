
from sqlalchemy.types import (
    String,
    TypeDecorator,
)
import json


class ArrayType(TypeDecorator):

    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)

    def copy(self):
        return ArrayType(self.impl.length)


