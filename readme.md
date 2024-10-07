# Download this model.
https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite

```
$ git lfs install
$ git clone https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite
```

# Then, execute following commands in PowerShell.
```
$ docker build -t vectorization_lambda:latest
$ docker run -p 9000:8080 vectorization_lambda:latest
$ Invoke-RestMethod -Method Post -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Body (Get-Content -Raw -Path .\event.json) -ContentType "application/json"
```