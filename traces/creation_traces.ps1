for ($p=1; $p -le 12; $p++) {
  foreach ($algo in "no","bh") {
    python ../code/main.py --auto inputs/input$p-$algo.txt > traces/NEW3-6-trace$p-$algo.txt
    Write-Host "Trace générée : NEW3-6-trace$p-$algo.txt"
  }
}
