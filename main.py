from dataclasses import dataclass
from typing import Self


@dataclass
class File:
    filepath: str

    @classmethod
    def create_file(cls, name: str, ext: str) -> Self:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...


file: File = File.create_file("test", "string")


with File("test") as file:
    print(file.filepath)


@dataclass
class JPEG(File):
    def jpeg_method(self) -> Self:
        ...


jpeg: JPEG = JPEG.create_file("test", "string")
jpeg.jpeg_method()

another_picture: JPEG = File.create_file("test", "string")  # error
