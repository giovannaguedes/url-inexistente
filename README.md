# url-inexistente
Testar se a página web existe ou não.

⚠️ Uso exclusivo para fins educacionais • Desenvolvido por M!ss s3c

📝 Guia: Criando e executando seu script para verificar sites

1. Criar o arquivo do script

No terminal, crie o arquivo:

nano script9.1.py

2. Adicionar o código Python

Cole o seguinte código:

#!/usr/bin/python3
# Verificação de site em Python
# Uso: python3 script9.1.py

import requests

# Teste com URL (pode usar uma inexistente)
site = requests.get("http://nome do site aqui.com.br")
status = site.status_code

if status == 200:
    print("Página existe")
else:
    print("Página inexistente")


⚠️ Observação: Para fins educativos, você pode testar com URLs inexistentes sem causar problemas.

3. Executar o script
python3 script9.1.py

4. Exemplo de execução

URL existente:

Página existe


URL inexistente:

Página inexistente

👉 O que você aprendeu aqui

requests.get() → faz uma requisição HTTP ao site.

.status_code → retorna o código de status HTTP (200 → OK, 404 → Not Found, etc.).

if → verifica condições e executa ações diferentes dependendo do resultado.
