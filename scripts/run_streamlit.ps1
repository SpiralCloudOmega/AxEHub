param(
    [string]$Path = 'axe_thrill_qenetix/browser_ui.py'
)

Push-Location "$PSScriptRoot\.."
try {
    streamlit run $Path
}
finally {
    Pop-Location
}
