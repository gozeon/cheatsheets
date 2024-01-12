## glob

```py
from pathlib import Path

for path_file in Path.cwd().glob("*"):
    print(path_file)
```

## 常用

```py
print(Path.home())
print(Path.cwd())
```

## parse

```py
print(Path(r"/home"))
print(Path(r"/home/test"))

print(f"You can find me here: {Path(__file__).parent}!")
```

## join

```py
Path.home().joinpath("python", "scripts", "test.py")

Path.home() / "python" / "test.py"
```

## attr

```py
test_path = Path("~/go/pkg/mod/golang.org/x/tools/gopls@v0.11.0/main.go")

print(test_path.name) # main.go
print(test_path.stem) # main
print(test_path.suffix) # .go
print(test_path.parent) # ~/go/pkg/mod/golang.org/x/tools/gopls@v0.11.0
```

## Checking 

```py
Path("/asd").exists()
Path("/asd").is_file()
Path("/asd").is_dir()

Path('..').is_absolute() # False

Path("/etc/ssh").is_relative_to("/etc") # True
```
