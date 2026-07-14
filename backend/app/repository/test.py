from app.repository.scanner import RepositoryScanner

scanner = RepositoryScanner()

files = scanner.scan(".")

for file in files:
    print(file.path)
    print(file.language)
    print()