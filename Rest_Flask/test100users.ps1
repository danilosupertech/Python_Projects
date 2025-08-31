$baseUrl = "http://localhost:5500/users"

# Lista de 100 usuários fictícios
$users = @(
    @{ name="John Doe"; email="johndoe@example.com" },
    @{ name="Jane Smith"; email="janesmith@example.com" },
    @{ name="Alice Johnson"; email="alicejohnson@example.com" },
    @{ name="Bob Brown"; email="bobbrown@example.com" },
    @{ name="Charlie Williams"; email="charliewilliams@example.com" },
    @{ name="Diana Jones"; email="dianajones@example.com" },
    @{ name="Edward Garcia"; email="edwardgarcia@example.com" },
    @{ name="Fiona Miller"; email="fionamiller@example.com" },
    # ... continue até completar 100 usuários
    @{ name="George Clark"; email="georgeclark@example.com" },
    @{ name="Helen Lewis"; email="helenlewis@example.com" }
)

# Exemplo completo com 100 usuários fictícios
# Para simplificar, podemos repetir alguns nomes até chegar em 100

while ($users.Count -lt 100) {
    foreach ($u in $users.Clone()) {
        if ($users.Count -ge 100) { break }
        $users += @{ name=$u.name; email=("copy" + $users.Count + "_" + $u.email) }
    }
}

# Enviar cada usuário para o Flask
$i = 1
foreach ($user in $users) {
    $body = $user | ConvertTo-Json
    $response = Invoke-RestMethod -Uri $baseUrl -Method POST -ContentType "application/json" -Body $body
    Write-Host "[$i] Usuário criado: $($user.name) <$($user.email)>"
    $i++
}
