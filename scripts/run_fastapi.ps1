param(
    [string]$Host = '0.0.0.0',
    [int]$Port = 8000
)

Push-Location "$PSScriptRoot\.."
try {
    python -m uvicorn axe_thrill_qenetix.api:app --reload --host $Host --port $Port
}
finally {
    Pop-Location
}
