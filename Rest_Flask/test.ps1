# URL base do seu servidor Flask
$baseUrl = "http://localhost:5500/users"

# Função para exibir respostas com separador
function Show-Response($response) {
    Write-Host "==============================="
    Write-Host $response
    Write-Host "==============================="
}

# 1️⃣ Criar usuário
$createBody = '{ "name": "John Doe", "email": "johndoe@example.com" }'
$response = & "C:\Windows\System32\curl.exe" -s -X POST -H "Content-Type: application/json" -d $createBody $baseUrl
Show-Response $response

# 2️⃣ Listar todos os usuários
$response = & "C:\Windows\System32\curl.exe" -s $baseUrl
Show-Response $response

# 3️⃣ Atualizar o usuário (assumindo id=1)
$updateBody = '{ "name": "John Updated", "email": "johnupdated@example.com" }'
$response = & "C:\Windows\System32\curl.exe" -s -X PUT -H "Content-Type: application/json" -d $updateBody "$baseUrl/1"
Show-Response $response

# 4️⃣ Listar novamente todos os usuários
$response = & "C:\Windows\System32\curl.exe" -s $baseUrl
Show-Response $response

# 5️⃣ Deletar o usuário (id=1)
$response = & "C:\Windows\System32\curl.exe" -s -X DELETE "$baseUrl/1"
Show-Response $response

# 6️⃣ Listar todos os usuários após deleção
$response = & "C:\Windows\System32\curl.exe" -s $baseUrl
Show-Response $response
