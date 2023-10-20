import subprocess

# Execute o flake8 no código-fonte
flake8_result = subprocess.call(["flake8", "main.py", "calculadora_estatistica.py", "calculadora_mediana.py"])

# Execute os testes unitários
unittest_result = subprocess.call(["python", "-m", "unittest", "discover", "-s", "tests"])

if flake8_result != 0 or unittest_result != 0:
    exit(1)  # Encerre o script com um código de saída não zero se houver falhas
